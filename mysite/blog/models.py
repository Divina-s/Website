from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime,date
from ckeditor.fields import RichTextField

# Create your models here.



STATUS=[
    (0,'publish'),
    (1,'draft')
]

class Category(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('home')


class Post(models.Model):
    title=models.CharField(max_length=200)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    #body=models.TextField()
    body=RichTextField(blank=True, null=True)
    article_snippet=models.CharField(max_length=255)
    status=models.IntegerField(choices=STATUS, default='1')
    post_date=models.DateField(auto_now_add=True)
    category=models.CharField(max_length=200, default='uncategorized')
    likes=models.ManyToManyField(User, related_name='blog_posts')



    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('home')
    
class Comment(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")    
    name=models.CharField(max_length=300)
    body=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return '%s -%s' % (self.post.title, self.name)
