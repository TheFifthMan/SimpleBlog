from django.contrib import admin
from .models import Category,Post,Tag
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','author','excerpt','category','created_timestamp','modified_timestamp']

admin.site.register(Category)
admin.site.register(Post,PostAdmin)
admin.site.register(Tag)
