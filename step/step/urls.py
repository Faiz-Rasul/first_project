"""step URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from celery.schedules import crontab


from users.tasks import add_monthly_fee

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("main.urls") ),
    path('', include("users.urls")),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]


urlpatterns = urlpatterns+static(settings.MEDIA_URL,
document_root=settings.MEDIA_ROOT)


CELERY_BEAT_SCHEDULE = {
    'add-monthly-fee':{
    'task': 'fees.tasks.add_monthly_fee',
    'schedule': crontab(day_of_month='1')
    },
}