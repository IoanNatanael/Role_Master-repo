from django.db import models


class InfoModel(models.Model):
    post_id = models.IntegerField(null=True)
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
