from rest_framework import serializers
from .models import BlogPost,Laibrary

class BlogPostSerialzers(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ["id","title","content","published_date"]


class LaibrarySerialzers(serializers.ModelSerializer):
    class Meta:
        model = Laibrary
        fields = "__all__"