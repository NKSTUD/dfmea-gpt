import json
import tiktoken

from django.http import StreamingHttpResponse
from bs4 import BeautifulSoup
from django.urls import reverse

from django_htmx.http import HttpResponseClientRedirect

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import openai

import prompts
from chatgpt.models import Table
from decouple import config

openai.api_key = config("OPENAI_API_KEY")


@csrf_exempt
def home(request):
    tables = Table.objects.all()
    return render(request, 'chatgpt/home.html', {"tables": tables})


@csrf_exempt
def prompt(request):
    data = json.loads(request.body)
    messages = data.get("message")
    messages.remove("Generating...")
    conversations = build_conversation_dict(messages)
    event_stream_data = event_stream(conversations)
    return StreamingHttpResponse(event_stream_data, content_type="text/event-stream")


def limit_context_length(context_messages):
    encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
    num_tokens = len(encoding.encode("".join([message.get("content") for message in context_messages])))
    print(num_tokens)
    if num_tokens > 14000:
        context_messages = context_messages[:2] + context_messages[-2:]
    return context_messages


def build_conversation_dict(messages: list) -> list[dict]:
    context_messages = [

        {
            "role": "user" if i % 2 == 0 else "assistant",
            "content": message
        }
        for i, message in enumerate(messages)
    ]

    return [

        {"role": "system",
         "content": prompts.context
         },

    ] + prompts.example + limit_context_length(context_messages)


def extract_table_content(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    tables = soup.find_all('table')
    tables = [table.prettify() for table in tables]
    return tables or None


def event_stream(conversations: list[dict]) -> str:
    code = ""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=conversations,
        stream=True,

    )
    for line in response:
        if content := line.choices[0].delta.get("content", ""):
            yield content
            code += content
    if tables := extract_table_content(code):
        part_name = conversations[-1].get("content")
        if tables:
            code = tables[1] if len(tables) > 1 else None
            relevant_informations = tables[0] if len(tables) > 0 else None
            Table.objects.create(code=code, part_name=part_name, relevant_informations=relevant_informations)


@csrf_exempt
def delete_table(request, pk):
    table = Table.objects.get(pk=pk)
    table.delete()
    return HttpResponseClientRedirect(reverse('home'))


if __name__ == '__main__':
    conversation = build_conversation_dict(
        ["Transmission", "Engine", "Brake"])
    elements = ["Steering", "Suspension", "Wheels", "Tires", "Body", "Interior", "Exterior",
                "Electrical", "HVAC", "Safety", "Security", "Other"]
    for text in event_stream(conversation):
        print(text)
