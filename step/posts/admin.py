from django.contrib import admin
from .models import Post, PostLikes, Comments
# Register your models here.


admin.site.register(Post)
admin.site.register(PostLikes)
admin.site.register(Comments)
