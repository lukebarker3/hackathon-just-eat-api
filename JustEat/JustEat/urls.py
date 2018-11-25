"""JustEat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from Myapp import views
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^idealweight/',views.IdealWeight),
    url(r'^api-auth/', include('rest_framework.urls'))

    # ENDPOINTS TO BE IMPLEMENTED
    url(r'^login/', views.login)
    url(r'^register/', views.register)
    url(r'^account-details/<int:num>/', views.getAccountDetails)
    url(r'^update-account/<int:num>/', views.updateAccountDetails)
    url(r'^requests/<int:num>/', views.getRequests)
    #url(r'^')
]
#The line url(r^idealweight/,views.IdealWeight)
#basically tells us that the IdealWeight method will be called using the url http://<server ip>/idealweight/
