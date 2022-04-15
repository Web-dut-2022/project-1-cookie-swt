from django.urls import path
from django.conf import settings
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path('entryPage/', views.click2Entry,name="entryPage"),
    path('entry', views.search2Entry),
    path('newPage/',views.addNew,name="new"),
    path('random',views.randomEntry,name="random"),
    path('MDedit',views.editMD),
    path('saveMD',views.saveMD),
    path('saveNewMD',views.saveNewMD)
]
