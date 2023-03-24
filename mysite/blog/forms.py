from django import forms
from .models import Post, Category

#CHOICES=[
    ##('coding','coding'),
    #('sports','sports'),
    #('entertainment', 'entertainment')
    #]
choices= Category.objects.all().values_list('name','name')
 
choice_list=[]
for item in choices:
   choice_list.append(item)
class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title', 'author', 'body', 'article_snippet', 'category', 'status')
        widgets={
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'author': forms.TextInput(attrs={'class':'form-control', 'value':'', 'id':'user','type':'hidden'}),
            #'author': forms.Select(attrs={'class':'form-control'}),  
            'body': forms.Textarea(attrs={'class':'form-control'}),
            'article_snippet':forms.Textarea(attrs={'class':'form-control'}),
            'category':forms.Select(choices=choice_list ,attrs={'class':'form-control'}), 
            'status': forms.Select(attrs={'class':'form-control'}),

        }
class EditForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title',  'body', 'article_snippet','category', 'status')
        widgets={
            'title': forms.TextInput(attrs={'class':'form-control'}),  
            'body': forms.Textarea(attrs={'class':'form-control'}),
            'article_snippet':forms.Textarea(attrs={'class':'form-control'}),
            'category': forms.Select(choices=choice_list ,attrs={'class':'form-control'}),
            'status': forms.Select(attrs={'class':'form-control'}),

        }        