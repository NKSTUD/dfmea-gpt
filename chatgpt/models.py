from django.db import models


class Table(models.Model):
    code = models.TextField(null=True, blank=True)
    part_name = models.TextField(max_length=100)
    relevant_informations = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.part_name
