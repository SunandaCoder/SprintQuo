import pytest
from rest_framework.reverse import reverse
from user.models import User

pytestmark = pytest.mark.django_db


@pytest.mark.django_db
class TestUser:
    def test_user_registration(self, client):
        # test case create their own database to test the views
        url = reverse("user_registration")
        user = {
            "username": "sunanda",
            "password": "root",
            "email": "ssunanda02@gmail.com",
            "mobile": "7578061886",
            "first_name": "sunanda",
            "last_name": "shil",
        }
        response = client.post(url, user)
        assert response.status_code == 201

    def test_user_registration_wrong_url(self, client):
        # test case create their own database to test the views
        url = reverse("user_registration1345xd")
        user = {
            "username": "sunanda",
            "password": "root",
            "email": "ssunanda02@gmail.com",
            "mobile": "7578061886",
            "first_name": "sunanda",
            "last_name": "shil",
        }
        response = client.post(url, user)
        assert response.status_code == 201

    def test_user_registration_blank_username(self, client):
        # test case for blank username
        url = reverse("user_registration")
        user = {
            "username": "",
            "password": "root",
            "email": "ssunanda02@gmail.com",
            "mobile": "7578061886",
            "first_name": "sunanda",
            "last_name": "shil",
        }
        response = client.post(url, user)
        assert response.status_code == 400

    def test_user_registration_blank_password(self, client):
        # test case for blank username
        url = reverse("user_registration")
        user = {
            "username": "",
            "password": "",
            "email": "ssunanda02@gmail.com",
            "mobile": "7578061886",
            "first_name": "sunanda",
            "last_name": "shil",
        }
        response = client.post(url, user)
        assert response.status_code == 400

    def test_user_is_verified_should_login(self, client):
        # test the login
        user = User.objects.create_user("sunanda",
                                        password="root",
                                        email="ssunanda02@gmail.com",
                                        first_name="sunanda",
                                        last_name="shil",
                                        )
        user.save()
        data = {
            "username": "sunanda",
            "password": "root",
        }
        url = reverse("login")
        response = client.post(url, data)
        assert response.status_code == 200

    def test_login_with_wrong_username(self, client):
        # test the login with wrong username
        user = User.objects.create_user("sunanda",
                                        password="root",
                                        email="ssunanda02@gmail.com",
                                        first_name="sunanda",
                                        last_name="shil",
                                        )
        user.save()
        data = {
            "username": "sono",
            "password": "root",
        }
        url = reverse("login")
        response = client.post(url, data)
        assert response.status_code == 404

    def test_login_with_wrong_password(self, client):
        # test the login with wrong password
        user = User.objects.create_user("sunanda",
                                        password="root",
                                        email="ssunanda02@gmail.com",
                                        first_name="sunanda",
                                        last_name="shil",
                                        )
        user.save()
        data = {
            "username": "sunanda",
            "password": "1234",
        }
        url = reverse("login")
        response = client.post(url, data)
        assert response.status_code == 404
