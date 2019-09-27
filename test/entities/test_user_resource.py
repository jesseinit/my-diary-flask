import json


class TestUserResourceEndpoints:
    def test_user_signup_successfull(self, client, ):
        '''' Test for a successful user signup'''

        response = client.post('/api/v1/auth/signup', data=json.dumps({
            "email": "blah@blah.com",
            "password": "inflames",
            "fullname": "Jesse James"
        }))

        resp = response.get_json()
        assert response.status_code == 201
        assert resp['message'] == "Your account has been created successfully"
        assert resp['data']['email'] == "blah@blah.com"
        assert resp['data']['fullname'] == "Jesse James"

    def test_user_login_successful(self, client):
        '''' Test for a successful user login'''

        response = client.post('/api/v1/auth/login', data=json.dumps({
            "email": "blah@blah.com",
            "password": "inflames",
        }))

        resp = response.get_json()
        assert response.status_code == 200
        assert resp['message'] == 'Logged in successfuly'
        assert 'token' in resp['data'].keys()
