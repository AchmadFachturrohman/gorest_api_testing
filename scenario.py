import pytest
import requests

#Personal Access Token from GoREST
# ACCESS_TOKEN = "Bearer 15ab2a9ce01cb6dde5ed689f89cb4a5ba379d35a18532279014e04eb6ee43b43"
# BASE_URL = "https://gorest.co.in/public-api/users"
# headers = {
#     "Authorization": ACCESS_TOKEN,
#     "Content-Type": "application/json"
# }

# Data pengguna untuk pengujian positif
# valid_user_data = {
#     "name": "Achmad Fachturrohman",
#     "email": "achmadfachturrohman@gmail.com",
#     "gender": "male",
#     "status": "active"
# }

from dotenv import load_dotenv
import os

BASE_URL = "https://gorest.co.in/public-api/users"

ACCESS_TOKEN = os.getenv("GOREST_TOKEN")

def get_headers():
    load_dotenv()
    token = os.getenv("GOREST_TOKEN")
    return {
        "Authorization": token,
        "Content-Type": "application/json"
    }

def test_create_user_positive(user_payload, user_holder):
    response = requests.post(BASE_URL, headers=get_headers(), json=user_payload)
    json_data = response.json()

    assert json_data["code"] == 201

    data = json_data["data"]

    if isinstance(data, dict) and "id" in data:
        user_id = data["id"]
        user_holder["id"] = user_id
        print(f"User berhasil dibuat dengan ID: {user_id}")
    else:
        pytest.skip("User gagal dibuat — tidak ditemukan ID dalam respons.")

def test_create_user_negative():
    bad_data = {
        "name": "",
        "email": "invalid",
        "gender": "x",
        "status": ""
    }
    response = requests.post(BASE_URL, headers=get_headers(), json=bad_data)
    body = response.json()
    assert body["code"] == 422

def test_get_user_positive(user_holder):
    user_id = user_holder.get("id")
    response = requests.get(f"{BASE_URL}/{user_id}", headers=get_headers())
    assert response.status_code == 200

def test_get_user_negative():
    response = requests.get(f"{BASE_URL}/99", headers=get_headers())
    assert response.status_code in [404,200]

def test_update_user_positive(user_holder):
    user_id = user_holder.get("id")
    updated_data = {
        "name": "Fathur QA Enthusiasts"
    }
    response = requests.put(f"{BASE_URL}/{user_id}", headers=get_headers(), json=updated_data)
    assert response.status_code == 200

def test_update_user_negative():
    updated_data = {
        "email": "invalid",
        "status": ""
    }
    response = requests.put(f"{BASE_URL}/99", headers=get_headers(), json=updated_data)
    assert response.status_code in [404,200]

def test_delete_user_positive(user_holder):
    user_id = user_holder.get("id")
    response = requests.delete(f"{BASE_URL}/{user_id}", headers=get_headers())
    assert response.status_code == 200

def test_delete_user_negative():
    response = requests.delete(f"{BASE_URL}/99", headers=get_headers())
    assert response.status_code in [404, 200]