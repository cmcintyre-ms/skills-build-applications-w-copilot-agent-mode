# Test data for populating octofit_db

# This file is used by the management command in octofit_tracker/management/commands/populate_db.py
TEST_USERS = [
    {"email": "alice@example.com", "name": "Alice", "password": "alicepass"},
    {"email": "bob@example.com", "name": "Bob", "password": "bobpass"},
    {"email": "carol@example.com", "name": "Carol", "password": "carolpass"}
]

TEST_TEAMS = [
    {"name": "Team Alpha", "members": ["alice@example.com", "bob@example.com"]},
    {"name": "Team Beta", "members": ["carol@example.com"]}
]

TEST_WORKOUTS = [
    {"name": "Pushups", "description": "Do 20 pushups"},
    {"name": "Running", "description": "Run for 15 minutes"}
]

TEST_ACTIVITIES = [
    {"user": "alice@example.com", "activity_type": "Running", "duration": 30, "points": 10},
    {"user": "bob@example.com", "activity_type": "Pushups", "duration": 10, "points": 5},
    {"user": "carol@example.com", "activity_type": "Running", "duration": 20, "points": 8}
]

TEST_LEADERBOARD = [
    {"user": "alice@example.com", "points": 10, "rank": 1},
    {"user": "bob@example.com", "points": 5, "rank": 2},
    {"user": "carol@example.com", "points": 8, "rank": 3}
]
