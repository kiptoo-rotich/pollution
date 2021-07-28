from django.conf import settings
from django.urls import path

from . import views

urlpatterns =[
    path('',views.index,name='index'),
    path('new_case/',views.newPost,name='new_case'),
    path('single_case/<id>/',views.Reactions_view,name='responses'),
    path('cleanup/',views.cleanup,name='cleanup'),
    path('cleanup/events/',views.cleanupquery,name='events'),
    path('clean_up/reactions/<id>/',views.Cleanup_reviews,name='cleanup_reviews'),
]