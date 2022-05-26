from django.contrib import admin
from .models import Movie, Review, Comment

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'vote_average',)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'review_score', 'title', 'created_at',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'content', 'created_at',)


admin.site.register(Movie, MovieAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)