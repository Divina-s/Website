from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category,Comment
from .forms import PostForm, EditForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
# Create your views here.
class HomeView(ListView):
    model=Post
    template_name='home.html'
    ordering=['-post_date']
    

    def get_context_data(self, *args, **kwargs):
        cat_menu=Category.objects.all()
        context=super(HomeView, self).get_context_data( *args, **kwargs)
        context["cat_menu"]= cat_menu
        return context
class ArticleDetail(DetailView):
    model=Post
    template_name='article_detail.html'
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
    fields='__all__'
class AddCommentView(CreateView):
    model=Comment
    form_class=PostForm
    template_name='add_comment.html'        
def CategoryView(request, cats):
    category_posts= Post.objects.filter(category=cats.replace('-',' '))
    return render(request,'categories.html', {'cats': cats.title().replace('-',' '), 'category_posts':category_posts})
def LikeView(request,pk):
    post=get_object_or_404(Post, id=request.POST.get('post.id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('article_detail', args=[str(pk)]))
