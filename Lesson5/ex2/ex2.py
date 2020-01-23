import pytest
import requests


def test_status_code_get(status_code, expected_result, status_url):
    url = status_url+str(status_code)
    result = requests.get(url)
    assert int(result.status_code) == int(expected_result)


def test_status_code_delete(status_code, expected_result, status_url, basic_auth):
    url = status_url+str(status_code)
    result = requests.delete(url)
    assert int(result.status_code) == int(expected_result)
