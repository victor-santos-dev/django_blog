from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse


class Post(models.Model):

    author =  models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    published_date = models.DataTimeField(blank=True,null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def approve_comments(self):
        return self.comments.filter(approved_comments=True)
    
    def __str__(self):
        return self.title

class Comment(models.Model):

    post = models.ForeignKey('blog.post',related_name='comments')
    author = models.ForeignKey(max_length=200)
    text = models.TextField()
    create_date = models.DataTimeField(default=timezone.now())
    approved_comment = models.BooleanField(default=False)