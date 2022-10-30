from django.urls import path
from .views import *


urlpatterns=[
    path('', blogs, name='blogs'),
    path('book', book, name='book'),

    path('post-blog/', postblog, name='postblog'),
    path('like/<int:id>/', LikeBlog.as_view() , name='like'),
    path('update/<str:id>/', edit_blog, name='edit_blog'),
    path('delete/<str:id>/', delete_blog , name='delete_blog'),
    path('dislike/<int:id>/', DislikeBlog.as_view() , name='dislike'),
    path('comment/', blog_comment, name='comment'),
    path('approve/<int:id>/', approve_blog, name='approve_blog'),


    
]

