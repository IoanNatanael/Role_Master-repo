import datetime

import uuid

from django.core.mail import EmailMessage

from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.views.generic import CreateView

from Role_Master.settings import EMAIL_HOST_USER
# from djangoProject.settings import EMAIL_HOST_USER
from userextend.forms import UserExtendForm
from userextend.models import UserToken
from django.core.exceptions import ObjectDoesNotExist


# from userextend.models import UserToken


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

            get_token = uuid.uuid4().hex
            UserToken.objects.create(token=get_token, user_id=new_user.id, created_at=datetime.datetime.now())

            # Trimiterea de mail CU template
            get_token_user = UserToken.objects.get(user_id=new_user.id).token

            details_user = {
                'fullname': f'{new_user.first_name}  {new_user.last_name}',
                'username': new_user.username,
                'url': f'https://role-master-2.herokuapp.com/activate-user/{new_user.id}/{get_token_user}/',
            }

            subject = 'Created a new account'
            message = get_template('mail.html').render(details_user)
            mail = EmailMessage(subject, message, EMAIL_HOST_USER, [new_user.email])
            mail.content_subtype = 'html'
            mail.send()

            return redirect('login')

        return super().form_invalid(form)


def activate_user(request, pk, token):
    try:
        user_token = UserToken.objects.get(token=token, user_id=pk)
        user = user_token.user
        user.is_active = True
        user.save()
    except ObjectDoesNotExist:
        # Handle the case when the UserToken does not exist
        # You can redirect to an appropriate error page or take any other action
        return redirect('error')

    return redirect('login')


def error_view(request):
    return render(request, 'userextend/error.html')
