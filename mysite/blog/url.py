from django.urls import path
from .views import HomeView, ArticleDetail, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView, AddCommentView,LikeView

urlpatterns = [
    path('',HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetail.as_view(), name='article_detail'),
    path('addpost/', AddPostView.as_view(), name='add_post'),
    path('addcategory/', AddCategoryView.as_view(), name='add_category'),
    path('article/edit/<int:pk>',UpdatePostView.as_view(), name='update_post' ),
    path('article/remove/<int:pk>',DeletePostView.as_view(), name='delete_post' ),
    path('category/<cats>/', CategoryView, name='category'),
    path('article/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),
    path('like/<int:pk>', LikeView, name='like_post'),
]