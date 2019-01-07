from django.contrib import admin

from core.forms import VideoForm, ThemeForm, CommentForm, ThumbForm
from core.models import Video, Theme, Thumb, Comment

# Register your models here.

class VideoAdmin(admin.ModelAdmin):
    form = VideoForm

class ThemeAdmin(admin.ModelAdmin):
    form = ThemeForm

class ThumbAdmin(admin.ModelAdmin):
    form = ThumbForm
    
class CommentAdmin(admin.ModelAdmin):
    form = CommentForm
      
admin.site.register(Video, VideoAdmin)
admin.site.register(Theme, ThemeAdmin)
admin.site.register(Thumb, ThumbAdmin)
admin.site.register(Comment, CommentAdmin)