import http.client
import os
import unittest
import requests
from urllib.request import urlopen


import pytest

BASE_URL = os.environ.get("BASE_URL")
DEFAULT_TIMEOUT = 2  # in secs


@pytest.mark.api
class TestApi(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(BASE_URL, "URL no configurada")
        self.assertTrue(len(BASE_URL) > 8, "URL no configurada")
# test api rest metodo add
    def test_api_add(self):
        url = f"{BASE_URL}/calc/add/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
    def test_api_add_bad_request(self):
        url = f"{BASE_URL}/calc/add/2/s"
        response = requests.get(url)
        assert response.status_code == http.client.BAD_REQUEST
# test api rest metodo substract
    def test_api_substract(self):
        url = f"{BASE_URL}/calc/substract/2/-4"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
    def test_api_substract_bad_request(self):
        url = f"{BASE_URL}/calc/substract/1/-s"
        response = requests.get(url)
        assert response.status_code == http.client.BAD_REQUEST
# test api rest metodo multiply
    def test_api_multiply(self):
        url = f"{BASE_URL}/calc/multiply/5/-4"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
    def test_api_multiply_bad_request(self):
        url = f"{BASE_URL}/calc/multiply/1/p"
        response = requests.get(url)
        assert response.status_code == http.client.BAD_REQUEST
# test api rest metodo divide
    def test_api_divide(self):
        url = f"{BASE_URL}/calc/divide/5/5"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
    def test_api_divide_bad_request(self):
        url = f"{BASE_URL}/calc/divide/1/0"
        response = requests.get(url)
        assert response.status_code == http.client.BAD_REQUEST
# test api rest metodo power
    def test_api_power(self):
        url = f"{BASE_URL}/calc/power/5/5"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
    def test_api_power_bad_request(self):
        url = f"{BASE_URL}/calc/power/1/r"
        response = requests.get(url)
        assert response.status_code == http.client.BAD_REQUEST
# test api rest metodo sqrt
    def test_api_sqrt(self):
        url = f"{BASE_URL}/calc/sqrt/5"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
    def test_api_sqrt_bad_request(self):
        url = f"{BASE_URL}/calc/sqrt/-3"
        response = requests.get(url)
        assert response.status_code == http.client.BAD_REQUEST
# test api rest metodo log10
    def test_api_log10(self):
        url = f"{BASE_URL}/calc/log10/10"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
    def test_api_log10_bad_request(self):
        url = f"{BASE_URL}/calc/log10/0"
        response = requests.get(url)
        assert response.status_code == http.client.BAD_REQUEST