import json

import pytest
from rest_framework.reverse import reverse
from user.models import User

pytestmark = pytest.mark.django_db


@pytest.mark.django_db
class TestSprint:
    def test_the_add_sprint(self, client):
        user = User.objects.create_superuser("sunanda",
                                             password="1234",
                                             email="ssunanda02@gmail.com")
        user.save()
        data = {
            "username": "sunanda",
            "password": "1234"
        }
        url = reverse("login")
        response = client.post(url, data)
        json_data = json.loads(response.content)
        token = json_data.get('data').get("token")
        # adding sprint
        sprint_data = {
            "sprint_name": "task",
            "entry_date": "2022-02-2 06:00",
            "expiry_date": "2022-02-22"
        }
        url = reverse("add-sprint")
        header = {
            "HTTP_AUTHORIZATION": token,
        }
        response = client.post(url, sprint_data, **header)
        assert response.status_code == 201

    def test_the_add_sprint_with_blank_sprint_name(self, client):
        user = User.objects.create_superuser("sunanda",
                                             password="1234",
                                             email="ssunanda02@gmail.com")
        user.save()
        data = {
            "username": "sunanda",
            "password": "1234"
        }
        url = reverse("login")
        response = client.post(url, data)
        json_data = json.loads(response.content)
        token = json_data.get('data').get("token")
        # adding sprint
        sprint_data = {
            "sprint_name": "",
            "entry_date": "2022-02-2 06:00",
            "expiry_date": "2022-02-22"
        }
        url = reverse("add-sprint")
        header = {
            "HTTP_AUTHORIZATION": token,
        }
        response = client.post(url, sprint_data, **header)
        assert response.status_code == 400

    def test_the_add_sprint_with_no_token(self, client):
        user = User.objects.create_superuser("sunanda",
                                             password="1234",
                                             email="ssunanda02@gmail.com")
        user.save()
        data = {
            "username": "sunanda",
            "password": "1234"
        }
        url = reverse("login")
        response = client.post(url, data)
        json_data = json.loads(response.content)
        # adding sprint
        sprint_data = {
            "sprint_name": "task",
            "entry_date": "2022-02-2 06:00",
            "expiry_date": "2022-02-22"
        }
        url = reverse("add-sprint")
        response = client.post(url, sprint_data)
        assert response.status_code == 400

    def test_fetch_sprint(self, client):
        user = User.objects.create_superuser("sunanda",
                                             password="1234",
                                             email="ssunanda02@gmail.com")
        user.save()
        data = {
            "username": "sunanda",
            "password": "1234"
        }
        url = reverse("login")
        response = client.post(url, data)
        json_data = json.loads(response.content)
        token = json_data.get('data').get("token")
        # adding sprint
        sprint_data = {
            "sprint_name": "task",
            "entry_date": "2022-02-2 06:00",
            "expiry_date": "2022-02-22"
        }
        url = reverse("add-sprint")
        header = {
            "HTTP_AUTHORIZATION": token,
        }
        response = client.get(url, sprint_data, **header)
        assert response.status_code == 200

    def test_fetch_sprint_without_token(self, client):
        user = User.objects.create_superuser("sunanda",
                                             password="1234",
                                             email="ssunanda02@gmail.com")
        user.save()
        data = {
            "username": "sunanda",
            "password": "1234"
        }
        url = reverse("login")
        response = client.post(url, data)
        json_data = json.loads(response.content)
        token = json_data.get('data').get("token")
        # adding sprint
        sprint_data = {
            "sprint_name": "task",
            "entry_date": "2022-02-2 06:00",
            "expiry_date": "2022-02-22"
        }
        url = reverse("add-sprint")
        response = client.get(url, sprint_data)
        assert response.status_code == 400

    def test_fetch_sprint_with_blank_username(self, client):
        user = User.objects.create_superuser("sunanda",
                                             password="1234",
                                             email="ssunanda02@gmail.com")
        user.save()
        data = {
            "username": "",
            "password": "1234"
        }
        url = reverse("login")
        response = client.post(url, data)
        json_data = json.loads(response.content)
        token = json_data.get('data').get("token")
        # adding sprint
        sprint_data = {
            "sprint_name": "task",
            "entry_date": "2022-02-2 06:00",
            "expiry_date": "2022-02-22"
        }
        url = reverse("add-sprint")
        header = {
            "HTTP_AUTHORIZATION": token,
        }
        response = client.get(url, sprint_data, **header)
        assert response.status_code == 200

    def test_fetch_sprint_without_sprint_name(self, client):
        user = User.objects.create_superuser("sunanda",
                                             password="1234",
                                             email="ssunanda02@gmail.com")
        user.save()
        data = {
            "username": "sunanda",
            "password": "1234"
        }
        url = reverse("login")
        response = client.post(url, data)
        json_data = json.loads(response.content)
        token = json_data.get('data').get("token")
        # adding sprint
        sprint_data = {
            "sprint_name": "",
            "entry_date": "2022-02-2 06:00",
            "expiry_date": "2022-02-22"
        }
        url = reverse("add-sprint")
        header = {
            "HTTP_AUTHORIZATION": token,
        }
        response = client.get(url, sprint_data, **header)
        assert response.status_code == 200

    def test_update_sprint(self, client):
        user = User.objects.create_superuser("sunanda",
                                             password="1234",
                                             email="ssunanda02@gmail.com")
        user.save()
        data = {
            "username": "sunanda",
            "password": "1234"
        }
        url = reverse("login")
        response = client.post(url, data)
        json_data = json.loads(response.content)
        token = json_data.get('data').get("token")
        # adding sprint
        sprint_data = {
            "sprint_name": "task",
            "entry_date": "2022-02-2 06:00",
            "expiry_date": "2022-02-22"
        }
        url = reverse("sprint")
        header = {
            "HTTP_AUTHORIZATION": token,
        }
        response = client.get(url, sprint_data, **header)
        json_data = json.loads(response.content)
        update_sprint = {
            "sprint_name": "taskquo",
            "entry_date": "2022-02-2 06:00",
            "expiry_date": "2022-02-22"
        }
        response = client.put(url, update_sprint, **header)
        assert response.status_code == 200


@pytest.mark.django_db
class TestVotingParameter:
    def test_the_add_parameter(self, client):
        user = User.objects.create_superuser("sunanda",
                                             password="1234",
                                             email="ssunanda02@gmail.com")
        user.save()
        data = {
            "username": "sunanda",
            "password": "1234"
        }
        url = reverse("login")
        response = client.post(url, data)
        json_data = json.loads(response.content)
        token = json_data.get('data').get("token")
        # adding parameter
        parameter_data = {
            "parameter_name": "Help"
        }
        url = reverse("voting-param")
        header = {
            "HTTP_AUTHORIZATION": token,
        }
        response = client.post(url, parameter_data, **header)
        assert response.status_code == 201

    def test_the_add_parameter_without_parameter_name(self, client):
        user = User.objects.create_superuser("sunanda",
                                             password="1234",
                                             email="ssunanda02@gmail.com")
        user.save()
        data = {
            "username": "sunanda",
            "password": "1234"
        }
        url = reverse("login")
        response = client.post(url, data)
        json_data = json.loads(response.content)
        token = json_data.get('data').get("token")
        # adding parameter
        parameter_data = {
            "parameter_name": ""
        }
        url = reverse("voting-param")
        header = {
            "HTTP_AUTHORIZATION": token,
        }
        response = client.post(url, parameter_data, **header)
        assert response.status_code == 400

    def test_the_add_parameter_with_no_token(self, client):
        user = User.objects.create_superuser("sunanda",
                                             password="1234",
                                             email="ssunanda02@gmail.com")
        user.save()
        data = {
            "username": "sunanda",
            "password": "1234"
        }
        url = reverse("login")
        response = client.post(url, data)
        json_data = json.loads(response.content)
        token = json_data.get('data').get("token")
        # adding parameter
        parameter_data = {
            "parameter_name": "Help"
        }
        url = reverse("voting-param")
        response = client.post(url, parameter_data)
        assert response.status_code == 400

    def test_fetch_parameter(self, client):
        user = User.objects.create_superuser("sunanda",
                                             password="1234",
                                             email="ssunanda02@gmail.com")
        user.save()
        data = {
            "username": "sunanda",
            "password": "1234"
        }
        url = reverse("login")
        response = client.post(url, data)
        json_data = json.loads(response.content)
        token = json_data.get('data').get("token")
        # adding parameter
        parameter_data = {
            "parameter_name": "Help"
        }
        url = reverse("voting-param")
        header = {
            "HTTP_AUTHORIZATION": token,
        }
        response = client.get(url, parameter_data, **header)
        assert response.status_code == 200

    def test_fetch_parameter_without_token(self, client):
        user = User.objects.create_superuser("sunanda",
                                             password="1234",
                                             email="ssunanda02@gmail.com")
        user.save()
        data = {
            "username": "sunanda",
            "password": "1234"
        }
        url = reverse("login")
        response = client.post(url, data)
        json_data = json.loads(response.content)
        # adding parameter
        parameter_data = {
            "parameter_name": "Help"
        }
        url = reverse("voting-param")
        response = client.get(url, parameter_data)
        assert response.status_code == 400

    def test_update_parameter(self, client):
        user = User.objects.create_superuser("sunanda",
                                             password="1234",
                                             email="ssunanda02@gmail.com")
        user.save()
        data = {
            "username": "sunanda",
            "password": "1234"
        }
        url = reverse("login")
        response = client.post(url, data)
        json_data = json.loads(response.content)
        token = json_data.get('data').get("token")
        # adding parameter
        parameter_data = {
            "parameter_name": "Help"
        }
        url = reverse("voting-param")
        header = {
            "HTTP_AUTHORIZATION": token,
            "content_type": 'application/json'
        }
        response = client.post(url, parameter_data, **header)
        json_data = json.loads(response.content)
        id = json_data.get('data').get('id')
        update_parameter = {
            "parameter_name": "productivity",
            "id": int(id)
        }
        response = client.put(url, update_parameter, **header)
        assert response.status_code == 200

    def test_update_parameter_content_type_missing(self, client):
        user = User.objects.create_superuser("sunanda",
                                             password="1234",
                                             email="ssunanda02@gmail.com")
        user.save()
        data = {
            "username": "sunanda",
            "password": "1234"
        }
        url = reverse("login")
        response = client.post(url, data)
        json_data = json.loads(response.content)
        token = json_data.get('data').get("token")
        # adding parameter
        parameter_data = {
            "parameter_name": "Help"
        }
        url = reverse("voting-param")
        header = {
            "HTTP_AUTHORIZATION": token,
        }
        response = client.post(url, parameter_data, **header)
        json_data = json.loads(response.content)
        id = json_data.get('data').get('id')
        update_parameter = {
            "parameter_name": "productivity",
            "id": int(id)
        }
        response = client.put(url, update_parameter, **header)
        assert response.status_code == 200

    def test_update_parameter_without_id_providing(self, client):
        user = User.objects.create_superuser("sunanda",
                                             password="1234",
                                             email="ssunanda02@gmail.com")
        user.save()
        data = {
            "username": "sunanda",
            "password": "1234"
        }
        url = reverse("login")
        response = client.post(url, data)
        json_data = json.loads(response.content)
        token = json_data.get('data').get("token")
        # adding parameter
        parameter_data = {
            "parameter_name": "Help"
        }
        url = reverse("voting-param")
        header = {
            "HTTP_AUTHORIZATION": token,
            "content_type": 'application/json'
        }
        response = client.post(url, parameter_data, **header)
        json_data = json.loads(response.content)
        id = json_data.get('data').get('id')
        update_parameter = {
            "parameter_name": "productivity",
        }
        response = client.put(url, update_parameter, **header)
        assert response.status_code == 500

    def test_update_parameter_with_wrong_token(self, client):
        user = User.objects.create_superuser("sunanda",
                                             password="1234",
                                             email="ssunanda02@gmail.com")
        user.save()
        data = {
            "username": "sunanda",
            "password": "1234"
        }
        url = reverse("login")
        response = client.post(url, data)
        json_data = json.loads(response.content)
        token = json_data.get('data').get("to")
        # adding parameter
        parameter_data = {
            "parameter_name": "Help"
        }
        url = reverse("voting-param")
        header = {
            "HTTP_AUTHORIZATION": token,
            "content_type": 'application/json'
        }
        response = client.post(url, parameter_data, **header)
        json_data = json.loads(response.content)
        id = json_data.get('data').get('id')
        update_parameter = {
            "parameter_name": "productivity",
            "id": int(id)
        }
        response = client.put(url, update_parameter, **header)
        assert response.status_code == 500

    def test_delete_parameter(self, client):
        user = User.objects.create_superuser("sunanda",
                                             password="1234",
                                             email="ssunanda02@gmail.com")
        user.save()
        data = {
            "username": "sunanda",
            "password": "1234"
        }
        url = reverse("login")
        response = client.post(url, data)
        json_data = json.loads(response.content)
        token = json_data.get('data').get("token")
        # adding parameter
        parameter_data = {
            "parameter_name": "Help"
        }
        url = reverse("voting-param")
        header = {
            "HTTP_AUTHORIZATION": token,
            "content_type": 'application/json'
        }
        response = client.post(url, parameter_data, **header)
        json_data = json.loads(response.content)
        id = json_data.get('data').get('id')
        delete_parameter = {
            "id": int(id)
        }
        response = client.delete(url, delete_parameter, **header)
        assert response.status_code == 200

    def test_delete_parameter_without_token(self, client):
        user = User.objects.create_superuser("sunanda",
                                             password="1234",
                                             email="ssunanda02@gmail.com")
        user.save()
        data = {
            "username": "sunanda",
            "password": "1234"
        }
        url = reverse("login")
        response = client.post(url, data)
        json_data = json.loads(response.content)
        token = json_data.get('data').get("token")
        # adding parameter
        parameter_data = {
            "parameter_name": "Help"
        }
        url = reverse("voting-param")
        header = {
            "HTTP_AUTHORIZATION": token,
            "content_type": 'application/json'
        }
        response = client.post(url, parameter_data, **header)
        json_data = json.loads(response.content)
        id = json_data.get('data').get('id')
        delete_parameter = {
            "id": int(id)
        }
        response = client.delete(url, delete_parameter, **header)
        assert response.status_code == 200

    def test_delete_parameter_without_providing_id(self, client):
        user = User.objects.create_superuser("sunanda",
                                             password="1234",
                                             email="ssunanda02@gmail.com")
        user.save()
        data = {
            "username": "sunanda",
            "password": "1234"
        }
        url = reverse("login")
        response = client.post(url, data)
        json_data = json.loads(response.content)
        token = json_data.get('data').get("token")
        # adding parameter
        parameter_data = {
            "parameter_name": "Help"
        }
        url = reverse("voting-param")
        header = {
            "HTTP_AUTHORIZATION": token,
            "content_type": 'application/json'
        }
        response = client.post(url, parameter_data, **header)
        json_data = json.loads(response.content)
        delete_parameter = {
        }
        response = client.delete(url, delete_parameter, **header)
        assert response.status_code == 500
