from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages


@login_required
@csrf_exempt
def discord_link(request):
    bot_link = 'https://discord.com/api/oauth2/authorize?client_id=1095629386050449449&permissions=1394522273792&' \
               'redirect_uri=https%3A%2F%2Frole-master-2.herokuapp.com&response_type=code&scope=bot%20messages.' \
               'read%20guilds.join%20gdm.join%20guilds%20guilds.members.read%20role_connections.write%20dm_channels.' \
               'read%20relationships.read%20applications.commands.permissions.update'

    if request.method == 'POST':
        # Copy button clicked, show success message
        messages.success(request, 'Link copied successfully!')

    return render(request, 'bot_invite/discord_link.html', {'bot_link': bot_link})
