from django.db import models


class DiscordBotPage(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    bot_url = models.URLField()

    def __str__(self):
        return self.name
