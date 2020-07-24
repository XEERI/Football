
from django.shortcuts import render
import requests
import datetime

# Create your views here.



# Wyszukiwanie graczy
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


    load = ""

    response = requests.request(
        "GET", url, data=load, params=querystring)
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

def player_details(request, player_id):
    api_key = "4d8dc09514907ea887cae91d0a8544bca127096ef1df1c6c1b80344a993045ac"
    url = "http://apiv2.apifootball.com/"

    querystring = {"action": "get_players", "player_id": player_id,
                   "APIkey": api_key}

    load = ""

    response = requests.request(
        "GET", url, data=load, params=querystring)
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

# Wyszukiwanie meczy
def get_match_data(request):
    api_key = "4d8dc09514907ea887cae91d0a8544bca127096ef1df1c6c1b80344a993045ac"
    if request.method == "POST":
        league_id = request.POST.get('league_id')
    else:
        league_id = 148
    if request.method == "POST":
        from_date = request.POST.get('from_date')
    else:
        from_date = datetime.datetime.now().date()
    if request.method == "POST":
        to_date = request.POST.get('to_date')
    else:
        to_date = datetime.datetime.now().date()


    url = "https://apiv2.apifootball.com/"

    querystring = {"action": "get_events", 'league_id': league_id,
                   "from": from_date, "to": to_date, "APIkey": api_key}

    load = ""

    response = requests.request(
        "GET", url, data=load, params=querystring)
    response = response.json()
    length = len(response)

    match_data = []
    match_error = {}

    try:
        for i in range(length):
            match = {
                'match_id': response[i]['match_id'],
                "match_status": response[i]['match_status'],
                'match_date': response[i]['match_date'],
                'match_time':  response[i]['match_time'],
                'home_team': response[i]['match_hometeam_name'],
                'home_team_score': response[i]['match_hometeam_score'],
                'away_team': response[i]['match_awayteam_name'],
                'away_team_score': response[i]['match_awayteam_score'],
                'team_home_badge': response[i]['team_home_badge'],
                'team_away_badge': response[i]['team_away_badge']
            }
            match_data.append(match)
    except:
        match_error = {
            'message': response['message']
        }

    querystring = {"action": "get_leagues", "APIkey": api_key}

    load = ""

    response = requests.request(
        "GET", url, data=load,params=querystring)
    response = response.json()
    length = len(response)

    competitions = []

    for i in range(length):
        league_details = {
            'league_id': response[i]['league_id'],
            'league_name': response[i]['league_name']
        }
        competitions.append(league_details)

    return render(request, 'footballstats/mecz.html', context={'match_data': match_data, 'match_error': match_error, 'competitions': competitions})




def match_details(request, match_id):
        api_key = "4d8dc09514907ea887cae91d0a8544bca127096ef1df1c6c1b80344a993045ac"
        url = "http://apiv2.apifootball.com/"

        querystring = {"action": "get_events", "match_id": match_id,
                       "APIkey": api_key}

        payload = ""

        response = requests.request(
            "GET", url, data=payload, params=querystring)
        response = response.json()

        length = len(response)

        match_info = {
            "match_id": response[0]['match_id'],
            "country_id": response[0]['country_id'],
            "country_name": response[0]['country_name'],
            "league_id": response[0]['league_id'],
            "league_name": response[0]['league_name'],
            "match_date": response[0]['match_date'],
            "match_status": response[0]['match_status'],
            "match_time": (response[0]['match_date'], response[0]['match_time']),
            "match_hometeam_name": response[0]['match_hometeam_name'],
            "match_hometeam_score": response[0]['match_hometeam_score'],
            "match_awayteam_name": response[0]['match_awayteam_name'],
            "match_awayteam_score": response[0]['match_awayteam_score'],
            "match_hometeam_halftime_score": response[0]['match_hometeam_halftime_score'],
            "match_awayteam_halftime_score": response[0]['match_awayteam_halftime_score'],
            "match_hometeam_extra_score": response[0]['match_hometeam_extra_score'],
            "match_awayteam_extra_score": response[0]['match_awayteam_extra_score'],
            "match_hometeam_penalty_score": response[0]['match_hometeam_penalty_score'],
            "match_awayteam_penalty_score": response[0]['match_awayteam_penalty_score'],
            "match_hometeam_system": response[0]['match_hometeam_system'],
            "match_awayteam_system": response[0]['match_awayteam_system'],
            "match_live": response[0]['match_live'],
            'team_home_badge': response[0]['team_home_badge'],
            'team_away_badge': response[0]['team_away_badge']
        }

        length = len(response[0]['goalscorer'])
        goalscorer = []

        for i in range(length):
            scorer = {
                "time": response[0]['goalscorer'][i]['time'],
                "home_scorer": response[0]['goalscorer'][i]['home_scorer'],
                "score": response[0]['goalscorer'][i]['score'],
                "away_scorer": response[0]['goalscorer'][i]['away_scorer']

            }
            goalscorer.append(scorer)
        return render(request, 'footballstats/mecz_statystyki.html', context={'match_info': match_info, 'goalscorer':goalscorer})

