from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='dc', description='DC Superheroes')

        # Create Users
        tony = User.objects.create(email='tony@stark.com', name='Tony Stark', team='marvel')
        steve = User.objects.create(email='steve@rogers.com', name='Steve Rogers', team='marvel')
        bruce = User.objects.create(email='bruce@wayne.com', name='Bruce Wayne', team='dc')
        clark = User.objects.create(email='clark@kent.com', name='Clark Kent', team='dc')

        # Create Workouts
        iron_workout = Workout.objects.create(name='Iron Endurance', description='Stark-level endurance training', suggested_for='marvel')
        shield_workout = Workout.objects.create(name='Shield Circuit', description='Rogers-style circuit', suggested_for='marvel')
        bat_workout = Workout.objects.create(name='Bat Strength', description='Wayne strength routine', suggested_for='dc')
        super_workout = Workout.objects.create(name='Super Flight', description='Kent flying drills', suggested_for='dc')

        # Create Activities
        Activity.objects.create(user=tony, type='run', duration=30, date=timezone.now().date())
        Activity.objects.create(user=steve, type='cycle', duration=45, date=timezone.now().date())
        Activity.objects.create(user=bruce, type='swim', duration=60, date=timezone.now().date())
        Activity.objects.create(user=clark, type='fly', duration=120, date=timezone.now().date())

        # Create Leaderboard
        Leaderboard.objects.create(user=tony, score=150)
        Leaderboard.objects.create(user=steve, score=120)
        Leaderboard.objects.create(user=bruce, score=200)
        Leaderboard.objects.create(user=clark, score=180)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
