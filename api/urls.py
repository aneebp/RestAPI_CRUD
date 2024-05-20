from django.urls import path
from . import views


urlpatterns = [
    path('blogposts/',views.BlogPostListCreate.as_view(),name="blog-post-list"),
    path('blogposts/<int:pk>/', views.BlogPostRetriveUpdateDelete.as_view(),name="updatedelete"),
    #laibrary
    path('laibrary/',views.LaibraryListCreate.as_view()),
    path('laibrary/<int:pk>/', views.LaibraryRetriveUpdateDelete.as_view()),
]
