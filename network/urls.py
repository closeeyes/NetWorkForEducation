from django.conf.urls import patterns, include, url
from network import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'networkForEducation.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$',views.showMain,name='showMain'),
    url(r'^video/',views.showVideo,name='showVideo'),
    url(r'^articles/',views.showArticles,name='showArticles'),
    url(r'^score/',views.showScore,name='showScore'),
    url(r'^personinfo/',views.showPersonInfo,name='showPersonInfo'),
    url(r'^userinfo/',views.showUserInfo,name='showUserInfo'),
)
