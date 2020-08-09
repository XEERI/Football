from django.shortcuts import render
import requests
import datetime

# Wyszukiwanie graczy
def get_player_data(request):
    api_key = "215d2a4f7def255ca30c33fe48d98853aa3c7e21071f36a0b999f7c7da30623c"
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
    api_key = "215d2a4f7def255ca30c33fe48d98853aa3c7e21071f36a0b999f7c7da30623c"
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
    api_key = "215d2a4f7def255ca30c33fe48d98853aa3c7e21071f36a0b999f7c7da30623c"

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

    r = requests.request("GET", url, data=load, params=querystring)
    r = r.json()
    length = len(r)

    match_data = []
    match_error = {}

    try:
        for i in range(length):
            match = {
                'match_id': r[i]['match_id'],
                "match_status": r[i]['match_status'],
                'match_date': r[i]['match_date'],
                'match_time':  r[i]['match_time'],
                'home_team': r[i]['match_hometeam_name'],
                'home_team_score': r[i]['match_hometeam_score'],
                'away_team': r[i]['match_awayteam_name'],
                'away_team_score': r[i]['match_awayteam_score'],
                'team_home_badge': r[i]['team_home_badge'],
                'team_away_badge': r[i]['team_away_badge'],
                'score_fulltime': int(r[i]['match_hometeam_score']) + int(r[i]['match_awayteam_score']),
                'score_over05': int(r[i]['match_hometeam_score']) + int(r[i]['match_awayteam_score']) > 0.5,
                'score_over15': int(r[i]['match_hometeam_score']) + int(r[i]['match_awayteam_score']) > 1.5,
                "score_over25": int(r[i]['match_hometeam_score']) + int(r[i]['match_awayteam_score']) > 2.5,
                "score_below05":int(r[i]['match_hometeam_score']) + int(r[i]['match_awayteam_score']) < 0.5,
                "score_below15":int(r[i]['match_hometeam_score']) + int(r[i]['match_awayteam_score']) < 1.5,
                "score_below25":int(r[i]['match_hometeam_score']) + int(r[i]['match_awayteam_score']) < 2.5,
            }
            match_data.append(match)
    except:
        match_error = {
            'message': r['message']
        }

    scorecount = {}
    for x in match_data:
        for k, v in x.items():
            if k in scorecount.keys():
                scorecount[k] += v
            elif "score_" in k:
                scorecount[k] = v
    # print(scorecount)
    return render(request, 'footballstats/mecz.html', context={'match_data': match_data, 'match_error': match_error,"data":scorecount})

def match_details(request, match_id):

        api_key = "215d2a4f7def255ca30c33fe48d98853aa3c7e21071f36a0b999f7c7da30623c"
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

        events = []

        timeline = ["1'", "2'", "3'", "4'", "5'", "6'", "7'", "8'", "9'", "10'", "11'", "12'", "13'", "14'", "15'",
                    "16'", "17'", "18'", "19'", "20'", "21'", "22'", "23'", "24'", "25'", "26'", "27'", "28'", "29'",
                    "30'", "31'", "32'", "33'", "34'", "35'", "36'", "37'", "38'", "39'", "40'", "41'", "42'", "43'",
                    "44'", "45'", "46'", "47'", "48'", "49'", "50'", "51'", "52'", "53'", "54'", "55'", "56'", "57'",
                    "58'", "59'", "60'", "61'", "62'", "63'", "64'", "65'", "66'", "67'", "68'", "69'", "70'", "71'",
                    "72'", "73'", "74'", "75'", "76'", "77'", "78'", "79'", "80'", "81'", "82'", "83'", "84'", "85'",
                    "86'", "87'", "88'", "89'", "90'", "91'", "92'", "93'", "94'", "95'",
                    "96'"]
        for i in range(len(timeline)):
            if timeline[i] == "90'":
                event = {
                    "average_score_halftime": (int(match_info['match_hometeam_halftime_score']) + int(match_info['match_awayteam_halftime_score'])) /2,
                    "average_score_fulltime": (int(match_info['match_hometeam_score']) + int(match_info['match_awayteam_score'])) / 2,
                    "score_halftime": int(match_info['match_hometeam_halftime_score']) + int(match_info['match_awayteam_halftime_score']),
                    "score_fulltime": int(match_info['match_hometeam_score']) + int(match_info['match_awayteam_score']),

                }
                events.append(event)
        return render(request, 'footballstats/mecz_statystyki.html', context={'match_info': match_info, 'goalscorer':goalscorer, 'events': events})















































        # gole = {}
        # try:
        #     match_score_count = (match_info['match_hometeam_score'] + ['match_awayteam_score'])
        #     if len(match_score_count) == 0:
        #        gole ={
        #            'two': int(match_score_count[0]) + 1,
        #            'three': int(match_score_count[0]) + 1 + int(match_score_count[1]),
        #            'four': int(match_score_count[0]) + 1 + int(match_score_count[1]) + int(match_score_count[2]),
        #        }
        # except:
        #     print("home format not found!")
        #
        #
        #
        #
        #
        # # a = int(request.GET['home_team_score'])
        # # b = int(request.GET['home_away_score'])
        # # c = a + b


