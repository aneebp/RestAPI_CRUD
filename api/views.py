from django.shortcuts import render
from .models import BlogPost
from django.http import HttpResponse
from .serializers import BlogPostSerialzers
# Create your views here.

def Home(request):
    blog = BlogPost(id=1,title="welcome",content="hallleo eveeeong",published_date="1222-23-2")
    serializer = BlogPostSerialzers(blog)
    print(serializer)
    return HttpResponse(serializer)