from django.core.management.base import BaseCommand
from octofit_tracker.test_data import TEST_USERS, TEST_TEAMS, TEST_WORKOUTS, TEST_ACTIVITIES, TEST_LEADERBOARD
from octofit.models import User, Team, Activity, Workout, Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data.'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Populating users...'))
        user_objs = {}
        for user in TEST_USERS:
            obj, _ = User.objects.get_or_create(email=user['email'], defaults={
                'name': user['name'],
                'password': user['password']
            })
            user_objs[user['email']] = obj

        self.stdout.write(self.style.SUCCESS('Populating teams...'))
        for team in TEST_TEAMS:
            members = [user_objs[email] for email in team['members'] if email in user_objs]
            obj, _ = Team.objects.get_or_create(name=team['name'])
            obj.members.set(members)
            obj.save()

        self.stdout.write(self.style.SUCCESS('Populating workouts...'))
        for workout in TEST_WORKOUTS:
            Workout.objects.get_or_create(name=workout['name'], defaults={
                'description': workout['description']
            })

        self.stdout.write(self.style.SUCCESS('Populating activities...'))
        for activity in TEST_ACTIVITIES:
            user = user_objs.get(activity['user'])
            if user:
                Activity.objects.get_or_create(user=user, activity_type=activity['activity_type'], defaults={
                    'duration': activity['duration'],
                    'points': activity['points']
                })

        self.stdout.write(self.style.SUCCESS('Populating leaderboard...'))
        for entry in TEST_LEADERBOARD:
            user = user_objs.get(entry['user'])
            if user:
                Leaderboard.objects.get_or_create(user=user, defaults={
                    'points': entry['points'],
                    'rank': entry['rank']
                })

        self.stdout.write(self.style.SUCCESS('Test data population complete.'))
