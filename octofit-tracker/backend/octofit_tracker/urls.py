from rest_framework import routers
from django.urls import path, include
from rest_framework.response import Response
from rest_framework.decorators import api_view
from octofit.views import UserViewSet, TeamViewSet, ActivityViewSet, WorkoutViewSet, LeaderboardViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'activity', ActivityViewSet)
router.register(r'workouts', WorkoutViewSet)
router.register(r'leaderboard', LeaderboardViewSet)

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': request.build_absolute_uri('users/'),
        'teams': request.build_absolute_uri('teams/'),
        'activity': request.build_absolute_uri('activity/'),
        'workouts': request.build_absolute_uri('workouts/'),
        'leaderboard': request.build_absolute_uri('leaderboard/'),
    })

urlpatterns = [
    path('', api_root, name='api-root'),
    path('api/', include(router.urls)),
]
