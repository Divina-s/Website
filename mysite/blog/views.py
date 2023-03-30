from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post,Comment,Category
from .forms import PostForm, EditForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
# Create your views here.
class HomeView(ListView):
    model=Post
    template_name='home.html'
    ordering=['-post_date']

#def detail(request, slug):
    #post=Post.objects.get(slug=slug)
   # context={
       # 'post':post
   # }
    #return render(request, 'post_detail.html', context)
class PostDetailView(DetailView):
   model =Post
   template_name ="post_detail.html"
    
def get_context_data(self, *args ,**kwargs):
        context=super(PostDetailView, self).get_context_data(*args, **kwargs)
        stuff=get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes=stuff.total_likes()
        context["total_likes"]=total_likes
class AddPostView(CreateView):
    model=Post
    form_class=PostForm
    template_name='add_post.html'   
    #fields='__all__' 
class AddCategoryView(CreateView):
    model=Category
    #form_class=PostForm
    template_name='add_category.html'   
    fields='__all__' 
class UpdatePostView(UpdateView):
    model=Post   
    form_class=EditForm 
    template_name='update_post.html'
class DeletePostView(DeleteView):
    model=Post
    template_name='delete_post.html'
    success_url= reverse_lazy('home') 
    #fields='__all__'
class AddCommentView(CreateView):
    model=Comment
    form_class=CommentForm
    template_name='add_comment.html' 
    #fields='__all__' 
    success_url= reverse_lazy('home') 

    def form_valid(self, form):
      form.instance.post_id=self.kwargs['pk']
      return super().form_valid(form)

         
def CategoryView(request, cats):
    category_posts=Post.objects.filter(category=cats.replace('-',' '))   
    return render(request,'categories.html', {'cats':cats.title().replace('-',' ') ,'category_posts': category_posts})


