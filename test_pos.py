import requests

# правильный запрос
job = {
    'team_leader': 1,
    "job": 'pilot',
    'work_size': 8,
    'collaborators': '1, 2, 3',
    'is_finished': True,
}
print(requests.post('http://127.0.0.1/api/jobs', json=job).json())
# запрос с не всеми необходимыми ключами
job1 = {
    'team_leader': 1,
    "job": 'pilot',
    'work_size': 8,
    'is_finished': True,
}
print(requests.post('http://127.0.0.1/api/jobs', json=job1).json())

# запрос с полями неправильного типа
job2 = {
    'team_leader': '22',
    "job": 23,
    'work_size': 8,
    'collaborators': 'qw',
    'is_finished': 52,
}
print(requests.post('http://127.0.0.1/api/jobs', json=job2).json())
