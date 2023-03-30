from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime,date
from ckeditor.fields import RichTextField

# Create your models here.


class Category(models.Model):
    name=models.CharField(max_length=200)


    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('home')
class Profile(models.Model):
    user=models.OneToOneField(User,null=True, on_delete=models.CASCADE, blank=True)
    bio=models.TextField()
    profile_pic=models.ImageField(null=True, blank=True, upload_to="images/profile/")
    Github_url=models.CharField(max_length=200, null=True, blank=True)
    facebook_url=models.CharField(max_length=200, null=True, blank=True)
    twitter_url=models.CharField(max_length=200, null=True, blank=True)
    linkedIn_url=models.CharField(max_length=200, null=True, blank=True)


    def __str__(self):
        return str(self.user)
    def get_absolute_url(self):
        return reverse('home')
    
STATUS=[
    (0,'publish'),
    (1,'draft')
]



class Post(models.Model):
    title=models.CharField(max_length=200)
    author=models.ForeignKey(User, on_delete=models.CASCADE,blank=True)
    #body=models.TextField()
    body=RichTextField(blank=True, null=True)
    article_snippet=models.CharField(max_length=1000)
    status=models.IntegerField(choices=STATUS, default='1')
    post_date=models.DateField(auto_now_add=True)
    category=models.CharField(max_length=200, default='uncategorized')
    likes=models.ManyToManyField(User, related_name='blog_posts')
    Image=models.ImageField(null=True, blank=True, upload_to="images/")

    def total_likes(self):
        return self.likes.count()

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
