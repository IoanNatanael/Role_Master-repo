from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView

from info_page.forms import InfoPostForm
from info_page.models import InfoModel


class InfoTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'info_page/info_page.html'

    def get_context_data(self, **kwargs):
        context = super(InfoTemplateView, self).get_context_data(**kwargs)
        context['posts'] = InfoModel.objects.all()
        return context


@login_required
def info_post_list(request):
    posts = InfoModel.objects.all().order_by('-created_at')
    return render(request, 'info_page/info_page.html', {'posts': posts})


@login_required
def info_post_create(request):
    if request.method == 'POST':
        form = InfoPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('info_post_list')
    else:
        form = InfoPostForm()
    return render(request, 'info_page/info_post_create.html', {'form': form})


@login_required
def info_post_delete(request, post_id):
    info_post = get_object_or_404(InfoModel, id=post_id)

    if request.method == 'POST':
        info_post.delete()
        return redirect('info_post_list')

    return render(request, 'info_page/info_post_confirm_delete.html', {'info_post': info_post})


@login_required
def info_post_edit(request, post_id):
    info_post = get_object_or_404(InfoModel, id=post_id)

    if request.method == 'POST':
        form = InfoPostForm(request.POST, instance=info_post)
        if form.is_valid():
            form.save()
            return redirect('info_post_list')
    else:
        form = InfoPostForm(instance=info_post)

    return render(request, 'info_page/info_post_edit.html', {'form': form, 'info_post': info_post})