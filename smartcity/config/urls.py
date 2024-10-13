from django.urls import path
from .views import config_list_create_api_view, config_detail_api_view, config_delete_api_view, config_update_api_view

urlpatterns = [
    path('', config_list_create_api_view, name='config-list-create'),
    path('<int:pk>', config_detail_api_view, name='config-detail'),
    path('<int:pk>/delete', config_delete_api_view, name='config-delete'),
    path('<int:pk>/update', config_update_api_view, name='config-update'),
]