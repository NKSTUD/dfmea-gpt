function cloneAnswerBlock() {
    const output = document.getElementById('gpt-output');
    const template = document.getElementById('chat-template');
    const clone = template.cloneNode(true);
    clone.id = "";
    output.appendChild(clone);
    clone.classList.remove('hidden');
    return clone.querySelector(".message");
}

function addToLog(message) {
    let answerBlock = cloneAnswerBlock();
    answerBlock.innerText = message;
    return answerBlock;

}

function getChatHistory() {
    const messageBlocks = document.querySelectorAll(".message:not(#chat-template .message)");
    return Array.from(messageBlocks).map((block) => block.innerHTML);
}

async function fetchPromptResponse() {
    const response = await fetch("/prompt", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({"message": getChatHistory()}),
    },)

    return response.body.getReader();
}

async function readPromptResponse(reader, answerBlock) {
    const decoder = new TextDecoder();
    const converter = new showdown.Converter();

    let chunks = "";
    while (true) {
        const {done, value} = await reader.read();
        if (done) {
            break;
        }
        chunks += decoder.decode(value);
        answerBlock.innerHTML = converter.makeHtml(chunks);
    }
}


document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('prompt-form');
    const spinner = document.getElementById('spinner');


    form.addEventListener('submit', async (event) => {
        event.preventDefault();
        spinner.classList.remove('htmx-indicator');
        prompt = form.elements.prompt.value;
        addToLog(prompt);
        try {
            const answerBlocks = addToLog("Generating...");
            answerBlocks.classList.add('ia-message');
            const reader = await fetchPromptResponse();
            await readPromptResponse(reader, answerBlocks);
        } catch (error) {
            console.log(error);
        } finally {
            spinner.classList.add('htmx-indicator');
            form.elements.prompt.value = "";
            hljs.highlightAll();

        }

    });
});