from django.db import models

# Create your models here.


class Player(models.Model):
    player_key = models.CharField(max_length=256, blank=True, null=True)
    player_name = models.CharField(max_length=256, blank=True, null=True)
    player_number = models.CharField(max_length=256, blank=True, null=True)
    player_country = models.CharField(max_length=256, blank=True, null=True)
    player_age = models.CharField(max_length=256, blank=True, null=True)
    player_match_played = models.CharField(
        max_length=256, blank=True, null=True)
    player_goals = models.CharField(max_length=256, blank=True, null=True)
    player_yellow_cards = models.CharField(
        max_length=256, blank=True, null=True)
    player_red_cards = models.CharField(max_length=256, blank=True, null=True)
    team_name = models.CharField(max_length=256, blank=True, null=True)
    team_key = models.CharField(max_length=256, blank=True, null=True)

    def __str__(self):
        return f"{self.player_name}"



class Match(models.Model):
    match_id = models.CharField(max_length=256, blank=True, null=True)
    match_status = models.CharField(max_length=256, blank=True, null=True)
    match_date = models.CharField(max_length=256, blank=True, null=True)
    match_time = models.CharField(max_length=256, blank=True, null=True)
    match_hometeam_name = models.CharField(
        max_length=256, blank=True, null=True)
    match_hometeam_score = models.CharField(
        max_length=256, blank=True, null=True)
    match_awayteam_name = models.CharField(
        max_length=256, blank=True, null=True)
    match_awayteam_score = models.CharField(
        max_length=256, blank=True, null=True)

    def __str__(self):
        return f"{self.match_id}"