from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
import requests
from footballstats.models import Player, Match

# Create your views here.

def index(request):
    return render(request, 'loadapi/index.html')

def sendPlayer(request):
    res = requests.get("https://apiv2.apifootball.com/?action=get_players&player_name=ronaldo cristiano&APIkey=215d2a4f7def255ca30c33fe48d98853aa3c7e21071f36a0b999f7c7da30623c")
    data = res.json()
    return HttpResponse(data)

def sendMatch(request):
    res = requests.get("https://apiv2.apifootball.com/?action=get_events&from=2019-04-01&to=2019-04-038&APIkey=215d2a4f7def255ca30c33fe48d98853aa3c7e21071f36a0b999f7c7da30623c")
    data = res.json()
    return data

def importplayer(request):
    Player.objects.all().delete()
    data = sendPlayer(request)

    # loop through your data and save to model
    for i in data:
        new_entry = Player()
        new_entry.player_key=i['player_key']
        new_entry.player_name=i['player_name']
        new_entry.player_number=i['player_number']
        new_entry.player_country=i['player_country']
        new_entry.player_age=i['player_age']
        new_entry.player_match_played=i['player_match_played']
        new_entry.player_goals=i['player_goals']
        new_entry.player_yellow_cards=i['player_yellow_cards']
        new_entry.player_red_cards=i['player_red_cards']
        new_entry.team_name=i['team_name']
        new_entry.team_key=i['team_key']
        new_entry.save()
    return HttpResponse(f"Zaimportowano graczy do bazy")



def importmatch(request):
    Match.objects.all().delete()
    data = sendMatch(request)
    # loop through your data and save to model
    for i in data:
        new_entry = Match()
        new_entry.match_id=i['match_id']
        new_entry.match_status=i['match_status']
        new_entry.match_date=i['match_date']
        new_entry.match_time=i['match_time']
        new_entry.match_hometeam_name=i['match_hometeam_name']
        new_entry.match_hometeam_score=i['match_hometeam_score']
        new_entry.match_awayteam_name=i['match_awayteam_name']
        new_entry.match_awayteam_score=i['match_awayteam_score']
        new_entry.save()
    return HttpResponse(f"Zaimportowano mecze do bazy")


