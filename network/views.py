#encoding=utf-8

from django.shortcuts import render
from network.models import Video,Articles,Questions,History,PersonInfo,Score,UserInfo,Comment
# Create your views here.

########.....................waiting  for  fullfill....................####
def showMain(request):   #显示主页,目前只显示前4个视频
	video_list=Video.objects.all()[:4]
	context_dict={'categories':video_list}
	return render(request,'network/index.html',context_dict)

def videoPage(request): #显示视频库页面,所有的视频
	video_list=Video.objects.all()
	context_dict={'categories':video_list}
	return render(request,'network/video.html',context_dict)

#跳转到被点击的视屏页面,后续补上 评论,
#这里是通过点击网页得到的video_name_slug
def videoPlay(request,video_name_slug): 
	context_dict={}
	try:
		videoItem=Video.objects.get(slug = video_name_slug)
		videoItem.count=videoItem.count+1
		videoItem.save()    # save count   666666666
		context_dict['video_name']=videoItem.name
		context_dict['video_urls']=videoItem.url
		context_dict['video']=videoItem
	except Video.DoesNotExist:
		print 'video none'
	return render(request,'network/videoPlay.html',context_dict)

def showArticles(request):
	return render(request,'network/articles.html')

def showScore(request):
	return render(request,'network/score.html')

def showPersonInfo(request):
	return render(request,'network/personinfo.html')

def showUserInfo(request):
	return render(request,'network/userinfo.html')

########.....................waiting  for  append ....................####