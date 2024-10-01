import pytest
import source.service as service
import unittest.mock as  mock

@mock.patch("source.service.get_user_from_db")
def test_get_user_from_db(mock_get_user_from_db):
    mock_get_user_from_db.return_value =  {
        id: "1ab23c09d456ef6",
        name: "Mocked Goat Matata",
        email: "goatmatata@goatpodcast.co.ke",
        phone_number: "+254701234567",
        age: 30,
        address: {
            street: "123 Goat St",
            city: "Nairobi",
            county: "NBI",
            postal_code: "00100"  
        },
        hobbies: ["rock climbing", "goating"],
        companies_owned: [
            "9876543210fedcba", "9876543210fedcba", "9876543210fed",
        ],
    }
    user = service.get_user_from_db("1ab23c09d456ef6")

    assert user["name"] == "Mocked Goat Matata"
    assert user["email"] == "goatmatata@goatpodcast.co.ke"
    assert user["phone_number"] == "+254701234567"
    assert len(user["companies_owned"]) == 3


@mock.patch("requests.get")
def test_get_users_from_api(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock.response.json.return_value = {
        "return_value" : {
            "id": "a1b23cd09e456f6",
            "name": "Dada Ng'ombe",
            "email": "dadangombe@chiziaboutcheese.co.ke",
            "phone_number": "+254712345678",
            "companies_owned": [
                "9874563210fedcba", "9876523410fedcba", "9876345210fed",
            ],
        },
    }
    mock_get.return_value = mock_response
    data = service.get_users_from_api()["return_value"]

    assert data["name"] == "Dada Ng'ombe"
    assert data["email"] == "dadangombe@chiziaboutcheese.co.ke"
    assert data["phone_number"] == "+254712345678"
    assert len(data["companies_owned"]) == 3

@mock.patch("requests.get")
def test_get_users_from_api_error(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 400
    mock_get.return_value = mock_response
    with pytest.raises(requests.HTTPError) as e:
        service.get_users_from_api()
    # assert str(e.value) == "Failed to fetch users from API"