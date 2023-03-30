from django.contrib import admin
from .models import Post,Comment,Category,Profile
 

admin.site.register(Post) 
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Profile)

# Register your models here.
