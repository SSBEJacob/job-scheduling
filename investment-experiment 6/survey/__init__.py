import random
from otree.api import *

class C(BaseConstants):
    NAME_IN_URL = 'survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    FIVE_CHOICES = [
            'Strongly Agree',
            'Agree',
            'Neither Agree or Disagree',
            'Disagree',
            'Strongly Disagree'
        ]
    SEVEN_CHOICES = [
            'Strongly Agree',
            'Agree',
            'Somewhat Agree',
            'Neither Agree or Disagree',
            'Somewhat Disagree',
            'Disagree',
            'Strongly Disagree'
        ]

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    
    question1 = models.StringField(
        choices=C.FIVE_CHOICES,
        label="I avoided jobs that required a lot of workers."
    )

    question2 = models.StringField(
        choices=C.FIVE_CHOICES,
        label="I avoided jobs that needed to be worked on immediately after accepting."
    )

    question3 = models.StringField(
        choices=C.FIVE_CHOICES,
        label="I avoided jobs that had a low Rate."
    )

    question4 = models.StringField(
        choices=C.FIVE_CHOICES,
        label="I took jobs just because they had a high Payment."
    )

    question5 = models.StringField(
        choices=C.FIVE_CHOICES,
        label="I took jobs just because they had a high Rate."
    )

    question6 = models.StringField(
        choices=C.FIVE_CHOICES,
        label="I took any job if I wasn't utilizing all my workers."
    )

    question7 = models.StringField(
        choices=C.FIVE_CHOICES,
        label="I only took a job if I was certain I could complete it."
    )

    question8 = models.StringField(
        choices=C.FIVE_CHOICES,
        label="I avoided very long jobs."
    )

    question9 = models.StringField(
        choices=C.FIVE_CHOICES,
        label="I avoided having more jobs than I could work on at the same time."
    )

    question10 = models.StringField(
        choices=C.SEVEN_CHOICES,
        label="It was very important that I used all 10 workers."
    )

    question11 = models.StringField(
        choices=C.SEVEN_CHOICES,
        label="It was very important that I worked on jobs closest to completing."
    )

    question12 = models.StringField(
        choices=C.SEVEN_CHOICES,
        label="It was very important that I worked on the highest Payment jobs."
    )

    question13 = models.StringField(
        choices=C.SEVEN_CHOICES,
        label="It was very important that I worked on the highest Rate jobs."
    )

    question14 = models.StringField(
        choices=C.SEVEN_CHOICES,
        label="It was very important that I worked on the jobs most at risk of being late."
    )

    question15 = models.StringField(
        choices=C.SEVEN_CHOICES,
        label="It was very important that I worked on the jobs at the top of the list (those with the nearest deadline)."
    )

    question16 = models.StringField(
        choices=C.SEVEN_CHOICES,
        label="I gave up on jobs."
    )


class Survey(Page):
    form_model = 'player'
    form_fields = ['question'+str(i) for i in range(1,17)]

# set this page as the first one to be displayed
page_sequence = [Survey]