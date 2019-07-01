from django.db import models

class Blog(models.Model):

    def __str__(self):
        return self.title

    title = models.CharField(max_length=200)
    text = models.TextField()
    pub_date = models.DateTimeField()
    category = models.CharField(max_length=100)

    def cut(self):
        split = self.text.split()
        desc = ' '.join(split[:15])
        return desc

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

class Header(models.Model):
    def __str__(self):
        return self.title

    title = models.CharField(max_length=200)
    summary = models.CharField(max_length=300)

