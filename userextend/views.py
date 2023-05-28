from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from userextend.forms import UserExtendForm


class UserExtendCreateView(CreateView):
    template_name = 'userextend/create_user.html'
    model = User
    form_class = UserExtendForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        email = form.cleaned_data.get('email')  # Get the email from the form data
        if User.objects.filter(email=email).exists():
            # If a user with the same email already exists, raise a validation error
            form.add_error('email', 'This email is already registered.')
            return self.form_invalid(form)

        # Continue with the existing code if the email is valid
        new_user = form.save(commit=True)
        new_user.is_active = True
        new_user.save()

        return redirect('login')
