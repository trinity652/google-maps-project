from django.urls import include, path

from .views import create_record,RecordAPIView,record_map

urlpatterns = [

    path('create/', create_record, name="create_record"),
    path('api/', RecordAPIView.as_view(), name="record API"),
    path('view/', record_map, name="record map"),

]