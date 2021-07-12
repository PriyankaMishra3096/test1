import pytest
import requests
import json


@pytest.mark.parametrize("a,b", [(6, 4)])
def test_first(a, b):
    url = "http://0.0.0.0:8080/gcp_demo"
    data = {"first_arg": a, "second_arg": b}
    response = requests.post(url, json=data)
    print(response)
    res_data = json.loads(response.text)
    assert int(res_data["Sum"]) == 10


def test2():
    url = "http://0.0.0.0:8080/gcp_demo_2"
    # req_data = {"first_arg": 4, "second_arg": 6}
    response = requests.get(url)
    print(response)
    res_data = json.loads(response.text)
    assert int(res_data["Sum"]) == 30
