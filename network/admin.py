#encoding=utf-8

from django.contrib import admin
from network.models import Video,Articles,Questions,History,PersonInfo,Score,UserInfo,Comment
# Register your models here.

class VideoAdmin(admin.ModelAdmin):
	#list_display = ('title', 'category', 'url')
	prepopulated_fields={'slug':('name',)}

admin.site.register(Video,VideoAdmin)
admin.site.register(Articles)
admin.site.register(Questions)
admin.site.register(History)
admin.site.register(PersonInfo)
admin.site.register(Score)
admin.site.register(UserInfo)
admin.site.register(Comment)
