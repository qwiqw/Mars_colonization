import requests

# праивльный гет запрос
print(requests.get('http://127.0.0.1/api/v2/users/1').json())
# праильный делит запрос
print(requests.delete('http://127.0.0.1/api/v2/users/1').json())
# правильный пост запрос
user = {
    'surname': 'surname',
    'name': 'name',
    'age': 2,
    'position': 'position',
    'speciality': 'speciality',
    'address': 'address',
    'email': 'email',
    'hashed_password': 'hashed_password',
}
print(requests.post('http://127.0.0.1/api/v2/users', json=user).json())
# неправильный гет запрос
print(requests.get('http://127.0.0.1/api/v2/users/-1').json())
# непраильный делит запрос
print(requests.delete('http://127.0.0.1/api/v2/users/-1').json())
# неправильный пост запрос
user1 = {}
print(requests.post('http://127.0.0.1/api/v2/users', json=user).json())
