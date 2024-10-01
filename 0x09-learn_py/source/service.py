import requests

database = [
    {
        "id": "1ab23c09d456ef6",
        "name": "Goat Matata",
        "email": "goatmatata@goatpodcast.co.ke",
        "phone_number": "+254701234567",
        "age": 30,
        "address": {
            "street": "123 Goat St",
            "city": "Nairobi",
            "county": "NBI",
            "postal_code": "00100"  
        },
        "hobbies": ["rock climbing", "goating"],
        "companies_owned": [
            "9876543210fedcba", "9876543210fedcba", "9876543210fed",
        ],
    },
    {
        "id": "a1b23cd09e456f6",
        "name": "Dada Ng'ombe",
        "email": "dadangombe@chiziaboutcheese.co.ke",
        "phone_number": "+254712345678",
        "age": 30,
        "address": {
            "street": "234 Cheesy Av",
            "city": "Nakuru",
            "county": "NKU",
            "postal_code": "20100"  
        },
        "hobbies": ["gardening", "cowing"],
        "companies_owned": [
            "9874563210fedcba", "9876523410fedcba", "9876345210fed",
        ],
    }
]

def get_user_from_db(user_id):
    user = [database[i] for i in range(len(database)) if user_id == database[i]["id"]]
    return user[0] if user else None

def get_users_from_api():
    res = requests.get(
        "jsonplaceholder.typicode.com/users"
    )

    if res.status_code == 200:
        return res.json()

    raise requests.HTTPError