
from django.shortcuts import render
import requests
import datetime
# Create your views here.
def get_player_data(request):
    api_key = "4d8dc09514907ea887cae91d0a8544bca127096ef1df1c6c1b80344a993045ac"
    if request.method == "POST":
        player_id = request.POST.get('player_id')
    else:
        player_id = 0
    if request.method == "POST":
        player_name = request.POST.get('player_name')
    else:
        player_name = 0
    url = "https://apiv2.apifootball.com/"

    querystring = {"action": "get_players", 'player_id': player_id, 'player_name': player_name,
                   "APIkey": api_key}


    payload = ""

    response = requests.request(
        "GET", url, data=payload, params=querystring)
    response = response.json()
    length = len(response)

    player_data = []
    player_error = {}

    try:
        for i in range(length):
            player = {
                "player_key": response[i]['player_key'],
                "player_name": response[i]['player_name'],
                "player_number": response[i]['player_number'],
                "player_country": response[i]['player_country'],
                "player_type": response[i]['player_type'],
                "player_age": response[i]['player_age'],
                "player_match_played": response[i]['player_match_played'],
                "player_goals": response[i]['player_goals'],
                "player_yellow_cards": response[i]['player_yellow_cards'],
                "player_red_cards": response[i]['player_red_cards'],
                "team_name": response[i]['team_name'],
                "team_key": response[i]['team_key'],
            }
            player_data.append(player)
    except:
        player_error = {
            'message': response['message']
        }

    return render(request, 'footballstats/player.html', context={'player_data': player_data, 'player_error': player_error})

def player_details(request, player_key):
    api_key = "4d8dc09514907ea887cae91d0a8544bca127096ef1df1c6c1b80344a993045ac"
    url = "http://apiv2.apifootball.com/"

    querystring = {"action": "get_players", "player_key": player_key,
                   "APIkey": api_key}

    payload = ""

    response = requests.request(
        "GET", url, data=payload, params=querystring)
    response = response.json()

    length = len(response)

    player_info = {
        "player_key": response[0]['player_key'],
        "player_name": response[0]['player_name'],
        "player_number": response[0]['player_number'],
        "player_country": response[0]['player_country'],
        "player_type": response[0]['player_type'],
        "player_age": response[0]['player_age'],
        "player_match_played": response[0]['player_match_played'],
        "player_goals": response[0]['player_goals'],
        "player_yellow_cards": response[0]['player_yellow_cards'],
        "player_red_cards": response[0]['player_red_cards'],
        "team_name": response[0]['team_name'],
        "team_key": response[0]['team_key'],
    }
    return render(request, 'footballstats/players.html', context={'player_info': player_info})