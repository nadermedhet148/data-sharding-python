from django.shortcuts import render
from .models import Post
from ShardingDataManger.ShardManger import ShardManger
# Create your views here.

def create(request):
    p = Post(name='test2',content='content')
    s = ShardManger()
    print(s.pickup_db('rest2'))

