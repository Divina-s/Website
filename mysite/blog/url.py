from django.urls import path
from .views import HomeView, PostDetailView, AddPostView, UpdatePostView, DeletePostView, AddCommentView,  AddCategoryView, CategoryView

urlpatterns = [
    path('',HomeView.as_view(), name='home'),
    path('postdetail/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('addpost/', AddPostView.as_view(), name='add_post'),
    path('addcategory/', AddCategoryView.as_view(), name='add_category'),
    path('article/edit/<int:pk>',UpdatePostView.as_view(), name='update_post' ),
    path('article/<int:pk>/remove',DeletePostView.as_view(), name='delete_post' ),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('postdetail/<int:pk>/comment', AddCommentView.as_view(), name='add_comment'),
    
]