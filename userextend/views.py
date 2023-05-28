from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView
from userextend.forms import UserExtendForm


class UserExtendCreateView(CreateView):
    template_name = 'userextend/create_user.html'
    model = User
    form_class = UserExtendForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        if form.is_valid() and not form.errors:
            new_user = form.save(commit=True)
            new_user.is_active = True
            new_user.save()
