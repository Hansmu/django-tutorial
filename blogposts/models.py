from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=250)
    published_date = models.DateTimeField()
    image = models.ImageField(upload_to='media/')
    body = models.TextField()

    # Used in the admin page to display the text for an entity
    def __str__(self):
        return self.title

    def formatted_published_date(self):
        return self.published_date.strftime('%a %b %Y')

    def summary(self):
        return self.body[:100]
