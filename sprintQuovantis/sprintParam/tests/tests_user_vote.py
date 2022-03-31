import pytest
import json
from rest_framework.reverse import reverse
from user.models import User

pytestmark = pytest.mark.django_db


@pytest.mark.django_db
class TestVote:
    def test_to_add_votes(self, client):
        user_list = [
            {
                "username": "sachin",
                "password": "1234",
                "email": "sachinkore7@gmail.com"
            },
            {
                "username": "sunanda",
                "password": "1234",
                "email": "sunanda@gmail.com"
            }
        ]
        for users in user_list:
            user = User.objects.create_user(users.get("username"),
                                            password=users.get("password"),
                                            email=users.get("email"),
                                            )
            user.save()
            data = {
                "username": "sachin",
                "password": "1234",
            }
            url = reverse("user-login")
            response = client.post(url, data)
            assert response.status_code == 200
        json_data = json.loads(response.content)
        token = json_data.get('data').get("token")
        # adding notes
        sprint_data = {
            "sprint_name": "tata app",
            "entry_date": "2022-02-2 06:00",
            "expiry_date": "2022-02-22"
        }
        url = reverse("add-sprint")
        header = {
            "HTTP_AUTHORIZATION": token,
        }
        response = client.post(url, sprint_data, **header)
        assert response.status_code == 201
        parameter_list = ["help", "productivity", "innovation", "discipline", "design"]
        for parameters in parameter_list:
            parameter_data = {
                "parameter_name": parameters
            }

            url = reverse("voting-param")
            response = client.post(url, parameter_data, **header)
            assert response.status_code == 201
        vote_data = {
            "vote_table":[
                {
                    "parameter_id": 1,
                    "vote_for": 2
                },
                {
                    "parameter_id": 2,
                    "vote_for": 2
                },
                {
                    "parameter_id": 3,
                    "vote_for": 2
                },
                {
                    "parameter_id": 4,
                    "vote_for": 2
                }
            ]
        }
        url = reverse("user-votes", kwargs={'id': 1})
        response = client.post(url, vote_data, **header, content_type='application/json')
        assert response.status_code == 201

    def test_to_vote_for_self(self, client):
        user_list = [
            {
                "username": "sachin",
                "password": "1234",
                "email": "sachinkore7@gmail.com"
            },
            {
                "username": "sunanda",
                "password": "1234",
                "email": "sunanda@gmail.com"
            }
        ]
        for users in user_list:
            user = User.objects.create_user(users.get("username"),
                                            password=users.get("password"),
                                            email=users.get("email"),
                                            )
            user.save()
            data = {
                "username": "sachin",
                "password": "1234",
            }
            url = reverse("user-login")
            response = client.post(url, data)
            assert response.status_code == 200
        json_data = json.loads(response.content)
        token = json_data.get('data').get("token")
        # adding notes
        sprint_data = {
            "sprint_name": "tata app",
            "entry_date": "2022-02-2 06:00",
            "expiry_date": "2022-02-22"
        }
        url = reverse("add-sprint")
        header = {
            "HTTP_AUTHORIZATION": token,
        }
        response = client.post(url, sprint_data, **header)
        assert response.status_code == 201
        parameter_list = ["help", "productivity", "innovation", "discipline", "design"]
        for parameters in parameter_list:
            parameter_data = {
                "parameter_name": parameters
            }

            url = reverse("voting-param")
            response = client.post(url, parameter_data, **header)
            assert response.status_code == 201
        vote_data ={
            "vote_table":[
                {
                    "parameter_id": 1,
                    "vote_for": 1
                },
                {
                    "parameter_id": 2,
                    "vote_for": 1
                },
                {
                    "parameter_id": 3,
                    "vote_for": 1
                },
                {
                    "parameter_id": 4,
                    "vote_for": 1
                }
            ]
        }
        url = reverse("user-votes", kwargs={'id': 1})
        response = client.post(url, vote_data, **header, content_type='application/json')
        assert response.status_code == 400

    def test_to_invalidate_credentials(self, client):
        user_list = [
            {
                "username": "sachin",
                "password": "1234",
                "email": "sachinkore7@gmail.com"
            },
            {
                "username": "sunanda",
                "password": "1234",
                "email": "sunanda@gmail.com"
            }
        ]
        for users in user_list:
            user = User.objects.create_user(users.get("username"),
                                            password=users.get("password"),
                                            email=users.get("email"),
                                            )
            user.save()
            data = {
                "username": "sachin",
                "password": "1234",
            }
            url = reverse("user-login")
            response = client.post(url, data)
            assert response.status_code == 200
        json_data = json.loads(response.content)
        token = json_data.get('data').get("token")
        # adding notes
        sprint_data = {
            "sprint_name": "tata app",
            "entry_date": "2022-02-2 06:00",
            "expiry_date": "2022-02-22"
        }
        url = reverse("add-sprint")
        header = {
            "HTTP_AUTHORIZATION": token,
        }
        response = client.post(url, sprint_data, **header)
        assert response.status_code == 201
        parameter_list = ["help", "productivity", "innovation", "discipline", "design"]
        for parameters in parameter_list:
            parameter_data = {
                "parameter_name": parameters
            }

            url = reverse("voting-param")
            response = client.post(url, parameter_data, **header)
            assert response.status_code == 201
        vote_data = {
            "vote_table":[
                {
                    "parameter_id": 8,
                    "vote_for": 10
                },
                {
                    "parameter_id": 2,
                    "vote_for": 8
                },
                {
                    "parameter_id": 3,
                    "vote_for": 2
                },
                {
                    "parameter_id": 4,
                    "vote_for": 2
                }
            ]
        }
        url = reverse("user-votes", kwargs={'id': 1})
        response = client.post(url, vote_data, **header, content_type='application/json')
        assert response.status_code == 400

    def test_to_get_result_details_from_user(self, client):
        user_list = [
            {
                "username": "sachin",
                "password": "1234",
                "email": "sachinkore7@gmail.com"
            },
            {
                "username": "sunanda",
                "password": "1234",
                "email": "sunanda@gmail.com"
            }
        ]
        for users in user_list:
            user = User.objects.create_user(users.get("username"),
                                            password=users.get("password"),
                                            email=users.get("email"),
                                            )
            user.save()
            data = {
                "username": "sachin",
                "password": "1234",
            }
            url = reverse("user-login")
            response = client.post(url, data)
            assert response.status_code == 200
        json_data = json.loads(response.content)
        token = json_data.get('data').get("token")
        # adding notes
        sprint_data = {
            "sprint_name": "tata app",
            "entry_date": "2022-02-2 06:00",
            "expiry_date": "2022-02-22"
        }
        url = reverse("add-sprint")
        header = {
            "HTTP_AUTHORIZATION": token,
        }
        response = client.post(url, sprint_data, **header)
        assert response.status_code == 201
        parameter_list = ["help", "productivity", "innovation", "discipline", "design"]
        for parameters in parameter_list:
            parameter_data = {
                "parameter_name": parameters
            }

            url = reverse("voting-param")
            response = client.post(url, parameter_data, **header)
            assert response.status_code == 201
        vote_data = {
            "vote_table":[
                {
                    "parameter_id": 1,
                    "vote_for": 2
                },
                {
                    "parameter_id": 2,
                    "vote_for": 2
                },
                {
                    "parameter_id": 3,
                    "vote_for": 2
                },
                {
                    "parameter_id": 4,
                    "vote_for": 2
                }
            ]
        }
        url = reverse("user-votes", kwargs={'id': 1})
        response = client.post(url, vote_data, **header, content_type='application/json')
        assert response.status_code == 201
        url = reverse("user-votes", kwargs={'id': 1})
        response = client.get(url, **header, content_type='application/json')
        assert response.status_code == 200

    def test_to_user_result_details_not_found(self, client):
        user_list = [
            {
                "username": "sachin",
                "password": "1234",
                "email": "sachinkore7@gmail.com"
            },
            {
                "username": "sunanda",
                "password": "1234",
                "email": "sunanda@gmail.com"
            },
            {
                "username": "rahul",
                "password": "1234",
                "email": "sunanda@gmail.com"
            }
        ]
        for users in user_list:
            user = User.objects.create_user(users.get("username"),
                                            password=users.get("password"),
                                            email=users.get("email"),
                                            )
            user.save()
            data = {
                "username": "sachin",
                "password": "1234",
            }
            url = reverse("user-login")
            response = client.post(url, data)
            assert response.status_code == 200
        json_data = json.loads(response.content)
        token = json_data.get('data').get("token")
        # adding notes
        sprint_data = {
            "sprint_name": "tata app",
            "entry_date": "2022-02-2 06:00",
            "expiry_date": "2022-02-22"
        }
        url = reverse("add-sprint")
        header = {
            "HTTP_AUTHORIZATION": token,
        }
        response = client.post(url, sprint_data, **header)
        assert response.status_code == 201
        parameter_list = ["help", "productivity", "innovation", "discipline", "design"]
        for parameters in parameter_list:
            parameter_data = {
                "parameter_name": parameters
            }

            url = reverse("voting-param")
            response = client.post(url, parameter_data, **header)
            assert response.status_code == 201
        vote_data = {
            "vote_table":[
                {
                    "parameter_id": 1,
                    "vote_for": 2
                },
                {
                    "parameter_id": 2,
                    "vote_for": 2
                },
                {
                    "parameter_id": 3,
                    "vote_for": 2
                },
                {
                    "parameter_id": 4,
                    "vote_for": 2
                }
            ]
        }
        url = reverse("user-votes", kwargs={'id': 1})
        response = client.post(url, vote_data, **header, content_type='application/json')
        assert response.status_code == 201
        url = reverse("user-votes", kwargs={'id': 2})
        response = client.get(url, **header, content_type='application/json')
        assert response.status_code == 404

    def test_to_user_update_details(self, client):
        user_list = [
            {
                "username": "sachin",
                "password": "1234",
                "email": "sachinkore7@gmail.com"
            },
            {
                "username": "sunanda",
                "password": "1234",
                "email": "sunanda@gmail.com"
            },
            {
                "username": "rahul",
                "password": "1234",
                "email": "rahul@gmail.com"
            }
        ]
        for users in user_list:
            user = User.objects.create_user(users.get("username"),
                                            password=users.get("password"),
                                            email=users.get("email"),
                                            )
            user.save()
            data = {
                "username": "sachin",
                "password": "1234",
            }
            url = reverse("user-login")
            response = client.post(url, data)
            assert response.status_code == 200
        json_data = json.loads(response.content)
        token = json_data.get('data').get("token")
        # adding notes
        sprint_data = {
            "sprint_name": "tata app",
            "entry_date": "2022-02-2 06:00",
            "expiry_date": "2022-02-22"
        }
        url = reverse("add-sprint")
        header = {
            "HTTP_AUTHORIZATION": token,
        }
        response = client.post(url, sprint_data, **header)
        assert response.status_code == 201
        parameter_list = ["help", "productivity", "innovation", "discipline", "design"]
        for parameters in parameter_list:
            parameter_data = {
                "parameter_name": parameters
            }

            url = reverse("voting-param")
            response = client.post(url, parameter_data, **header)
            assert response.status_code == 201
        vote_data = {
            "vote_table":[
                {
                    "parameter_id": 1,
                    "vote_for": 2
                },
                {
                    "parameter_id": 2,
                    "vote_for": 2
                },
                {
                    "parameter_id": 3,
                    "vote_for": 2
                },
                {
                    "parameter_id": 4,
                    "vote_for": 2
                }
            ]
        }
        url = reverse("user-votes", kwargs={'id': 1})
        response = client.post(url, vote_data, **header, content_type='application/json')
        assert response.status_code == 201
        vote_update_data = {
            "vote_table":[
                {
                    "parameter_id": 1,
                    "vote_for": 3
                },
                {
                    "parameter_id": 2,
                    "vote_for": 3
                },
                {
                    "parameter_id": 3,
                    "vote_for": 3
                },
                {
                    "parameter_id": 4,
                    "vote_for": 3
                }
            ]
        }
        url = reverse("user-votes", kwargs={'id': 1})
        response = client.put(url, vote_update_data, **header, content_type='application/json')
        assert response.status_code == 200

    def test_to_user_not_update_details_your_self(self, client):
        user_list = [
            {
                "username": "sachin",
                "password": "1234",
                "email": "sachinkore7@gmail.com"
            },
            {
                "username": "sunanda",
                "password": "1234",
                "email": "sunanda@gmail.com"
            },
            {
                "username": "rahul",
                "password": "1234",
                "email": "rahul@gmail.com"
            }
        ]
        for users in user_list:
            user = User.objects.create_user(users.get("username"),
                                            password=users.get("password"),
                                            email=users.get("email"),
                                            )
            user.save()
            data = {
                "username": "sachin",
                "password": "1234",
            }
            url = reverse("user-login")
            response = client.post(url, data)
            assert response.status_code == 200
        json_data = json.loads(response.content)
        token = json_data.get('data').get("token")
        # adding notes
        sprint_data = {
            "sprint_name": "tata app",
            "entry_date": "2022-02-2 06:00",
            "expiry_date": "2022-02-22"
        }
        url = reverse("add-sprint")
        header = {
            "HTTP_AUTHORIZATION": token,
        }
        response = client.post(url, sprint_data, **header)
        assert response.status_code == 201
        parameter_list = ["help", "productivity", "innovation", "discipline", "design"]
        for parameters in parameter_list:
            parameter_data = {
                "parameter_name": parameters
            }

            url = reverse("voting-param")
            response = client.post(url, parameter_data, **header)
            assert response.status_code == 201
        vote_data = {
            "vote_table":[
                {
                    "parameter_id": 1,
                    "vote_for": 2
                },
                {
                    "parameter_id": 2,
                    "vote_for": 2
                },
                {
                    "parameter_id": 3,
                    "vote_for": 2
                },
                {
                    "parameter_id": 4,
                    "vote_for": 2
                }
            ]
        }
        url = reverse("user-votes", kwargs={'id': 1})
        response = client.post(url, vote_data, **header, content_type='application/json')
        assert response.status_code == 201
        vote_update_data = {
            "vote_table":[
                {
                    "parameter_id": 1,
                    "vote_for": 1
                },
                {
                    "parameter_id": 2,
                    "vote_for": 1
                },
                {
                    "parameter_id": 3,
                    "vote_for": 1
                },
                {
                    "parameter_id": 4,
                    "vote_for": 1
                }
            ]
        }
        url = reverse("user-votes", kwargs={'id': 1})
        response = client.put(url, vote_update_data, **header, content_type='application/json')
        assert response.status_code == 400

    def test_to_update_details_invalidate(self, client):
        user_list = [
            {
                "username": "sachin",
                "password": "1234",
                "email": "sachinkore7@gmail.com"
            },
            {
                "username": "sunanda",
                "password": "1234",
                "email": "sunanda@gmail.com"
            },
            {
                "username": "rahul",
                "password": "1234",
                "email": "rahul@gmail.com"
            }
        ]
        for users in user_list:
            user = User.objects.create_user(users.get("username"),
                                            password=users.get("password"),
                                            email=users.get("email"),
                                            )
            user.save()
            data = {
                "username": "sachin",
                "password": "1234",
            }
            url = reverse("user-login")
            response = client.post(url, data)
            assert response.status_code == 200
        json_data = json.loads(response.content)
        token = json_data.get('data').get("token")
        # adding notes
        sprint_data = {
            "sprint_name": "tata app",
            "entry_date": "2022-02-2 06:00",
            "expiry_date": "2022-02-22"
        }
        url = reverse("add-sprint")
        header = {
            "HTTP_AUTHORIZATION": token,
        }
        response = client.post(url, sprint_data, **header)
        assert response.status_code == 201
        parameter_list = ["help", "productivity", "innovation", "discipline", "design"]
        for parameters in parameter_list:
            parameter_data = {
                "parameter_name": parameters
            }

            url = reverse("voting-param")
            response = client.post(url, parameter_data, **header)
            assert response.status_code == 201
        vote_data = {
            "vote_table":[
                {
                    "parameter_id": 1,
                    "vote_for": 2
                },
                {
                    "parameter_id": 2,
                    "vote_for": 2
                },
                {
                    "parameter_id": 3,
                    "vote_for": 2
                },
                {
                    "parameter_id": 4,
                    "vote_for": 2
                }
            ]
        }
        url = reverse("user-votes", kwargs={'id': 1})
        response = client.post(url, vote_data, **header, content_type='application/json')
        assert response.status_code == 201
        vote_update_data = {
            "vote_table":[
                {
                    "parameter_id": 1,
                    "vote_for": 7
                },
                {
                    "parameter_id": 2,
                    "vote_for": 7
                },
                {
                    "parameter_id": 3,
                    "vote_for": 7
                },
                {
                    "parameter_id": 4,
                    "vote_for": 7
                }
            ]
        }
        url = reverse("user-votes", kwargs={'id': 1})
        response = client.put(url, vote_update_data, **header, content_type='application/json')
        assert response.status_code == 400


@pytest.mark.django_db
class TestResult:
    def test_to_votes_result(self, client):
        user_list = [
            {
                "username": "sachin",
                "password": "1234",
                "email": "sachinkore7@gmail.com"
            },
            {
                "username": "sunanda",
                "password": "1234",
                "email": "sunanda@gmail.com"
            }
        ]
        for users in user_list:
            user = User.objects.create_user(users.get("username"),
                                            password=users.get("password"),
                                            email=users.get("email"),
                                            )
            user.save()
            data = {
                "username": "sachin",
                "password": "1234",
            }
            url = reverse("user-login")
            response = client.post(url, data)
            assert response.status_code == 200
        json_data = json.loads(response.content)
        token = json_data.get('data').get("token")
        # adding notes
        sprint_data = {
            "sprint_name": "tata app",
            "entry_date": "2022-02-2 06:00",
            "expiry_date": "2022-02-22"
        }
        url = reverse("add-sprint")
        header = {
            "HTTP_AUTHORIZATION": token,
        }
        response = client.post(url, sprint_data, **header)
        assert response.status_code == 201
        parameter_list = ["help", "productivity", "innovation", "discipline", "design"]
        for parameters in parameter_list:
            parameter_data = {
                "parameter_name": parameters
            }

            url = reverse("voting-param")
            response = client.post(url, parameter_data, **header)
            assert response.status_code == 201
        vote_data = {
                "vote_table":[
                    {
                        "parameter_id": 1,
                        "vote_for": 2
                    },
                    {
                        "parameter_id": 2,
                        "vote_for": 2
                    },
                    {
                        "parameter_id": 3,
                        "vote_for": 2
                    },
                    {
                        "parameter_id": 4,
                        "vote_for": 2
                    }
            ]
        }
        url = reverse("user-votes", kwargs={'id': 1})
        response = client.post(url, vote_data, **header, content_type='application/json')
        assert response.status_code == 201
        url = reverse("sprint-result", kwargs={'id': 1})
        response = client.get(url, **header)
        assert response.status_code == 200

    def test_to_votes_result_sprint_not_found(self, client):
        user_list = [
            {
                "username": "sachin",
                "password": "1234",
                "email": "sachinkore7@gmail.com"
            },
            {
                "username": "sunanda",
                "password": "1234",
                "email": "sunanda@gmail.com"
            }
        ]
        for users in user_list:
            user = User.objects.create_user(users.get("username"),
                                            password=users.get("password"),
                                            email=users.get("email"),
                                            )
            user.save()
            data = {
                "username": "sachin",
                "password": "1234",
            }
            url = reverse("user-login")
            response = client.post(url, data)
            assert response.status_code == 200
        json_data = json.loads(response.content)
        token = json_data.get('data').get("token")
        # adding notes
        sprint_data = {
            "sprint_name": "tata app",
            "entry_date": "2022-02-2 06:00",
            "expiry_date": "2022-02-22"
        }
        url = reverse("add-sprint")
        header = {
            "HTTP_AUTHORIZATION": token,
        }
        response = client.post(url, sprint_data, **header)
        assert response.status_code == 201
        parameter_list = ["help", "productivity", "innovation", "discipline", "design"]
        for parameters in parameter_list:
            parameter_data = {
                "parameter_name": parameters
            }

            url = reverse("voting-param")
            response = client.post(url, parameter_data, **header)
            assert response.status_code == 201
        vote_data = {
                "vote_table":[
                    {
                        "parameter_id": 1,
                        "vote_for": 2
                    },
                    {
                        "parameter_id": 2,
                        "vote_for": 2
                    },
                    {
                        "parameter_id": 3,
                        "vote_for": 2
                    },
                    {
                        "parameter_id": 4,
                        "vote_for": 2
                    }
            ]
        }
        url = reverse("user-votes", kwargs={'id': 1})
        response = client.post(url, vote_data, **header, content_type='application/json')
        assert response.status_code == 201
        url = reverse("sprint-result", kwargs={'id': 2})
        response = client.get(url, **header)
        assert response.status_code == 404
