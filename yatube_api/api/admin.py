from django.contrib import admin

from posts.models import Comment, Follow, Group, Post


class CommetnAdmin(admin.TabularInline):
    model = Comment
    fields = ('author', 'post', 'text', 'created')
    readonly_fields = ('created',)
    extra = 0


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'pub_date', 'author', 'group')
    fields = ('text', ('author', 'group'), 'image', 'pub_date')
    readonly_fields = ('pub_date',)
    search_fields = ('text',)
    list_display_links = ('text',)
    list_filter = ('pub_date', 'group')
    list_editable = ('group',)
    inlines = (CommetnAdmin,)


admin.site.register(Group)
admin.site.register(Follow)
