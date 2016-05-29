from django.contrib import admin
from network.models import Video,Articles,Questions,History,PersonInfo,Score,UserInfo,Comment
# Register your models here.

admin.site.register(Video)
admin.site.register(Articles)
admin.site.register(Questions)
admin.site.register(History)
admin.site.register(PersonInfo)
admin.site.register(Score)
admin.site.register(UserInfo)
admin.site.register(Comment)
