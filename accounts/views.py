from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView
from django.views.generic.edit import ProcessFormView

from accounts.forms import AccountCreateForm, AccountUpdateForm, AccountProfileUpdateForm
from accounts.models import Profile


class AccountCreateView(CreateView):
    model = User
    template_name = 'registration.html'
    form_class = AccountCreateForm
    success_url = reverse_lazy('accounts:login')

    def form_valid(self, form):
        result = super().form_valid(form)
        # new_rec = UserActions.objects.create(
        #     user=self.request.user,
        #     action=UserActions.USER_ACTION.LOGIN,
        #     info='Some info'
        # )
        # new_rec.save()
        messages.info(self.request, f"New user has just been created!")
        return result

class AccountLoginView(LoginView):
    template_name = 'login.html'


    def get_redirect_url(self):
        if self.request.GET.get('next'):
            return self.request.GET.get('next')
        return reverse('core:index')

    def form_valid(self, form):
        result  = super().form_valid(form)

        try:
            profile = self.request.user.profile
        # except RelatedObjectDoesNotExist as ex:
        except Exception as ex:
            profile = Profile.objects.create(user=self.request.user)
            profile.save()

        messages.info(self.request, f'User {self.request.user} has been successfully logged in!')
        return result


class AccountLogoutView(LogoutView):
    template_name = 'logout.html'

    def get(self, request, *args, **kwargs):
        # RemovedInDjango40Warning: when the deprecation ends, replace with:
        #   context = self.get_context_data()
        result = super().get(request, *args, **kwargs)

        messages.info(self.request, f'User {self.request.user} has been logged out!')

        return result



class AccountUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'profile.html'
    form_class = AccountUpdateForm
    success_url = reverse_lazy('core:index')

    def get_object(self, queryset=None):
        return self.request.user


class AccountUpdateView(LoginRequiredMixin, ProcessFormView):
    # model = User
    # template_name = 'profile.html'
    # form_class = AccountUpdateForm
    # success_url = reverse_lazy('core:index')
    #
    # def get_object(self, queryset=None):
    #     return self.request.user

    def get(self, request, *args, **kwargs):
        user = self.request.user
        profile = self.request.user.profile

        user_form = AccountUpdateForm(instance=user)
        profile_form = AccountProfileUpdateForm(instance=profile)

        return render(
            request=request,
            template_name='profile.html',
            context={
                'user_form': user_form,
                'profile_form': profile_form,
            }
        )

    def post(self, request, *args, **kwargs):
        user = self.request.user
        profile = self.request.user.profile

        user_form = AccountUpdateForm(
            data=request.POST,
            instance=user
        )
        profile_form = AccountProfileUpdateForm(
            data=request.POST,
            files=request.FILES,
            instance=profile
        )

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return HttpResponseRedirect(reverse('accounts:profile'))

        return render(
            request=request,
            template_name='profile.html',
            context={
                'user_form': user_form,
                'profile_form': profile_form,
            }
        )