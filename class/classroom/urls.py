from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import FileFieldView,AddMoreFiles


urlpatterns = [
    path('join_room',views.join_room,name='join_room'),
    path('',views.home_page,name='home_page'),
    path('room/<str:room>/',views.room,name='room'),
    path('room/<str:room>/classwork/',views.room_classwork,name='room_classwork'),
    path("checkview",views.checkview,name='checkview'),
    path('create_room/',views.create_room,name='create_room'),
    path('create_task/',views.create_task,name='create_task'),
    path('task/<int:pk>',views.task,name='task'),
    path('add_homework/<int:pk>',FileFieldView.as_view(),name='add'),
    path('returned/<int:pk>',views.returned,name='returned'),
    path('returned_details/<int:pk>/<string>',views.returned_details,name='returned_details'),
    path('add_topic/<str:room>/',views.add_topic,name='add_topic'),
    path('add_more_files/<int:pk>',AddMoreFiles.as_view(),name='add_more_files'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)