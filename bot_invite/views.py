from django.shortcuts import render


def bot_link(request):
    link_url = "https://example.com"
    return render(request, 'my_template.html', {'link_url': link_url})
