from django.urls import path

from groups.views import group_edit, groups_list

app_name = 'groups'

urlpatterns = [
    path('', groups_list, name='list'),
    # path('create', GroupsCreateView.as_view(), name='create'),
    path('edit/<int:id>', group_edit, name='edit'),
    # path('delete/<int:pk>', GroupsDeleteView.as_view(), name='delete'),
]
