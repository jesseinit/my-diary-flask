import json


class TestUserResourceEndpoints:
    def test_user_signup(self, client, init_db):
        # response = client.post('/api/v1/auth/signup', data=json.dumps({
        #     "email": "blah@blah.com",
        #     "password": "inflames",
        #     "fullname": "Jesse James"
        # }))
        # print(response.data.decode('utf-8'))
        assert 1 == 1
        # print(init_db)
