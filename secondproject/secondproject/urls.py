"""secondproject URL Configuration

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
from demoapp import views as v1
from timeapp import views as v2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gm/',v1.gm_view),
    path('ge/',v1.ge_view),
    path('gn/',v1.gn_view),
    path('time/',v2.tellmetime),
    path(' /',v2.tellmetime),
  

]
