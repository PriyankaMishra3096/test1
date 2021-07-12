import os
import pytest

import main


@pytest.fixture
def client():
    main.app.testing = True
    return main.app.test_client()


def test_handler_no_env_variable(client):
    r = client.get("/")

    assert r.data.decode() == "Hello World!"
    assert r.status_code == 200


def test_handler_with_env_variable(client):
    os.environ["NAME"] = "Priyanka"
    r = client.get("/")

    assert r.data.decode() == "Hello Priyanka!"
    assert r.status_code == 200

# def test_handler_with_env_variable():
#     os.environ["arg1"] = 10
#     os.environ["arg2"] = 20
#     response = requests.post(url, json=data)
#     print(response)
#     res_data = json.loads(response.text)
#     assert int(res_data["Sum"]) == 10


