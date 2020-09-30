from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse


def index(request):
    return render(
        request=request,
        template_name='index.html'
    )



class EditView:

    model = None
    form = None
    template_name = None
    redirect_url = None
    object_name = None
    pk_arg = 'id'


    def get_object(self, id):
        return self.model.objects.get(id=id)

    def get_context(self, **kwargs):
        return kwargs

    def edit_instance(self, request, id):

        try:
            instance = self.get_object(id)
        except self.model.DoesNotExist:
            return HttpResponse(f"{self.model.__name__} doesn't exist", status=404)

        if request.method == 'GET':

            form = self.form(instance=instance)

        elif request.method == 'POST':

            form = self.form(
                data=request.POST,
                instance=instance
            )

            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse(self.redirect_url))

        return render(
            request=request,
            template_name=self.template_name,
            context=self.get_context(**{
                'form': form,
                self.object_name: instance,
            })
        )

    def __call__(self, request, **kwargs):
        self.request = request
        if self.pk_arg in kwargs:
            kwargs['id'] = kwargs[self.pk_arg]
            if self.pk_arg != 'id':
                del kwargs[self.pk_arg]
        return self.edit_instance(request, **kwargs)
