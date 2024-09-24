import requests


def create_ad(data: dict):
    files = None
    if 'image' in data:
        image_path = data.get('image')
        files = {
            'image': open(image_path, "rb"),
        }
        data.pop('image')
    
    response = requests.post('http://localhost:8000', data=data, files=files)
    print(response.json(), "\n")


ads = [
    {
        'title': 'Пупсик',
        'description': 'Милый пупсик',
        'kind': 'Dog',
        'breed': 'пуп',
        'age': 1,
        'gender': 'M',
        'location': 'Москва',
        'price': 16000,
        'image': 'pups.png'
    },
        {
        'title': 'Собака1',
        'description': 'Собака',
        'kind': 'Dog',
        'breed': 'красивая порода',
        'age': 4,
        'gender': 'M',
        'location': 'Томск',
        'price': 100,
        'image': 'cap.jpg'
    },
        {
        'title': 'Пуп',
        'description': 'Милая собака',
        'kind': 'Dog',
        'breed': 'красивая пуп',
        'age': 5,
        'gender': 'M',
        'location': 'Новосибирск',
        'price': 16500,
        'image': 'panda.jpg'
    },
        {
        'title': 'Пупсик',
        'description': 'Милый пупсик',
        'kind': 'Dog',
        'breed': 'пуп',
        'age': 1,
        'gender': 'M',
        'location': 'Москва',
        'price': 16000,
        'image': 'pups.png'
    },
        {
        'title': 'Пупсик',
        'description': 'Милый пупсик',
        'kind': 'Dog',
        'breed': 'пуп',
        'age': 1,
        'gender': 'M',
        'location': 'Москва',
        'price': 16000,
        'image': 'pups.png'
    },
        {
        'title': 'Пупсик',
        'description': 'Милый пупсик',
        'kind': 'Dog',
        'breed': 'пуп',
        'age': 1,
        'gender': 'M',
        'location': 'Москва',
        'price': 16000,
        'image': 'pups.png'
    },
        {
        'title': 'Пупсик',
        'description': 'Милый пупсик',
        'kind': 'Dog',
        'breed': 'пуп',
        'age': 1,
        'gender': 'M',
        'location': 'Москва',
        'price': 16000,
        'image': 'pups.png'
    },
        {
        'title': 'Пупсик',
        'description': 'Милый пупсик',
        'kind': 'Dog',
        'breed': 'пуп',
        'age': 1,
        'gender': 'M',
        'location': 'Москва',
        'price': 16000,
        'image': 'pups.png'
    },
        {
        'title': 'Пупсик',
        'description': 'Милый пупсик',
        'kind': 'Dog',
        'breed': 'пуп',
        'age': 1,
        'gender': 'M',
        'location': 'Москва',
        'price': 16000,
        'image': 'pups.png'
    },
        {
        'title': 'Пупсик',
        'description': 'Милый пупсик',
        'kind': 'Dog',
        'breed': 'пуп',
        'age': 1,
        'gender': 'M',
        'location': 'Москва',
        'price': 16000,
        'image': 'pups.png'
    }


]


for ad in ads:
    create_ad(ad)
        