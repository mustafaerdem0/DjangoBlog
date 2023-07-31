"""djalistirma URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from dj_app.views import *

# settings getirdim
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path('kayit',kayitol, name="kayitol"),
    path('giris',girisyap, name="girisyap"),
    path('cikis',cikisyap, name="cikisyap"),
    path('notlar/<notId>',notdetaylari, name="notedetails"),
    path('notlar/<notId>/edit', notEdit,name="notedit"),
    path("not/ekle", notekle, name="notekle"),
    path('404',hata,name="404"),
    path('kontrol/', k_kontrol, name="kontrol"),
    path('blog',blog,name="blog"),
    path("notlar/<notId>/sil", notsil, name="notsil"),
    path("kullanici/<usernames>/<userid>",userprofile,name="userprofile"),
    path("kullanci/<int:userid>/edit", profileedit, name="profileedit"),
    path('notonaybekleme',notonaybekleme,name="notonaybekleme"),
    path("notonayla/<noteId>/onayla", notonay, name="notonayla"),
    path("banla/<userid>",banneduser,name="userbanla"),
    path('notsilbekleyen',notsilbekleyen,name='notsilbekleyen'),
    path('notsilonay<notId>',notsilonay,name='notsilonay')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
