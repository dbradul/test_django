from django.urls import path

from groups.views import groups_list, GroupEditView, GroupUpdateView

app_name = 'groups'

urlpatterns = [
    path('', groups_list, name='list'),
    # path('edit/<int:id>', GroupEditView(), name='edit'),
    path('edit/<int:id>', GroupUpdateView.as_view(), name='edit'),
]
