from django.shortcuts import render

# Create your views here.

########.....................waiting  for  fullfill....................####
def showMain(request):
	return render(request,'network/base.html')

def showVideo(request):
	return render(request,'network/video.html')

def showArticles(request):
	return render(request,'network/articles.html')

def showScore(request):
	return render(request,'network/score.html')

def showPersonInfo(request):
	return render(request,'network/personinfo.html')

def showUserInfo(request):
	return render(request,'network/userinfo.html')

########.....................waiting  for  append ....................####