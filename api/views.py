from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.response import Response
from .serializers import BlogPostSerialzers,LaibrarySerialzers
from .models import BlogPost,Laibrary

class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerialzers

    #delete complete record 
    def delete(self, request, *args, **kwargs):
        BlogPost.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BlogPostRetriveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerialzers
    lookup_field = "pk"



#laibrary data

class LaibraryListCreate(generics.ListCreateAPIView):
    queryset = Laibrary.objects.all()
    serializer_class = LaibrarySerialzers

class LaibraryRetriveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Laibrary.objects.all()
    serializer_class = LaibrarySerialzers
    lookup_field = "pk"