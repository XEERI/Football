from django.contrib import admin
from .models import Player, Match
# Register your models here.





# class adminPlayer(admin.ModelAdmin):
#     list_display = ('player_key', 'player_name', 'player_number', 'player_country', 'player_age',
#                     'player_match_played', 'player_goals', 'player_yellow_cards','player_red_cards', 'team_name','team_key',)


admin.site.register(Player)


# class adminMatch(admin.ModelAdmin):
#     list_display = ('match_id', 'match_status', 'match_date', 'match_time', 'match_hometeam_name',
#                     'match_hometeam_score', 'match_awayteam_name', 'match_awayteam_score',)


admin.site.register(Match)