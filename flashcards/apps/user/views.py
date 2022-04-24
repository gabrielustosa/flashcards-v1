from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.views.generic import TemplateView


class ProfileRegisterView(TemplateView):
    template_name = 'registration/register.html'

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        self.form = UserCreationForm(request.POST or None)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form
        return context

    def post(self, request, *args, **kwargs):
        form = self.form

        if form.is_valid():
            form.save()
            account = authenticate(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password1')
            )
            login(request, account)
            return redirect('deck:index')
        else:
            messages.error(request, 'Algum dado do formulário foi preenchido incorretamente')
            return redirect('user:register')
