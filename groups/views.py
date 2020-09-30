from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse

from core.views import EditView
from groups.forms import GroupCreateForm
from groups.models import Group


def groups_list(request):
    groups = Group.objects.all()

    if request.GET.get('name'):
        qs = groups.filter(name__startswith=request.GET.get('name'))

    if request.GET.get('course'):
        qs = groups.filter(course__contains=request.GET.get('course'))

    return render(
        request=request,
        template_name='groups-list.html',
        context={
            'groups': groups,
        }
    )


def group_edit(request, id):
    group = get_object_or_404(Group, id=id)

    if request.method == 'POST':
        form = GroupCreateForm(request.POST, instance=group)

        if form.is_valid():
            group = form.save()
            print(f'Group has been saved: {group}')
            return HttpResponseRedirect(reverse('groups:list'))
    else:
        form = GroupCreateForm(
            instance=group
        )

    return render(
        request=request,
        template_name='groups-edit.html',
        context={
            'form': form,
            'group': group,
            'students': group.students.all()
        }
    )


class GroupEditView(EditView):

    model = Group
    form = GroupCreateForm
    template_name = 'groups-edit.html'
    redirect_url = 'groups:list'
    object_name = 'group'

    def get_context(self, **kwargs):
        context = super().get_context(**kwargs)
        group = context[self.object_name]
        context['students'] = group.students.all()
        return context