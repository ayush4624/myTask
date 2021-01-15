from django.contrib import admin
from django.urls import path,include
from home import views


admin.site.site_header="REGISTRATION"
admin.site.index_title="WELCOME TO DASHBOARD"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home')
    path('about',views.about,name='about')
    path('contact',views.contact,name='contact')
    path('project',views.project,name='project')

]
