from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import resolve_url

from django.http import HttpResponse
from django.http import HttpRequest
from django.http import Http404
from django.http import HttpResponseBadRequest

from django.urls import reverse_lazy
from django.urls import reverse

from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from django.conf import settings

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from django.contrib.sites.shortcuts import get_current_site

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth import get_user_model
from django.template.loader import render_to_string
from django.core.mail import BadHeaderError, send_mail

from .forms import UserUpdateForm


class OnlyYouMixin(UserPassesTestMixin):
    raise_exception = True
    
    def test_func(self):
        user = self.request.user
        return user.pk == self.kwargs['pk'] or user.is_superuser


class UserDetailView(OnlyYouMixin, SuccessMessageMixin, DetailView):
    model = get_user_model()
    template_name = 'user/user_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "ユーザ情報"
        return context


class UserUpdateView(OnlyYouMixin, SuccessMessageMixin, UpdateView):
    model = get_user_model()
    form_class = UserUpdateForm
    template_name = 'user/user_update.html'
    success_message = "ユーザー情報を更新しました"
    
    def get_success_url(self):
        return resolve_url('user:user_detail', pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "ユーザ更新"
        return context

