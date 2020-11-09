from .models import Post
from ShardingDataManger.ShardManger import ShardManger
# Create your views here.

def create(request):

    posts = [
        {
            "name": "new artcal",
            "content": "content",
        },
        {
            "name": "old artcal",
            "content": "content",
        },
        {
            "name": "future artcal",
            "content": "content",
        }
    ]
    shard_manger = ShardManger()

    for post in posts:
        print(post)
        db = shard_manger.pickup_db(post['name'])
        unique_id = shard_manger.unique_id_generator(post['name'])
        p = Post(name=post['name'], content=post['content'],unique_id=unique_id)
        p.save(using=db)


