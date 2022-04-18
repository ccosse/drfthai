from django.db import models

class Phrase(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    owner = models.ForeignKey('auth.User', related_name='phrases', on_delete=models.CASCADE,null=True,blank=True)
    data = models.JSONField()

    class Meta:
        ordering = ['title']
