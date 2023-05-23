from logger import logger
from enum import Enum

import allure
from requests import Response

BASE_URL = 'https://petstore.swagger.io/v2{}'


class ResponseStatusCode(Enum):
    OK = 200
    BAD_REQUEST = 400
    NOT_FOUND = 404


class Base:
    """Class with common methods"""

    @allure.step('Check response status code value')
    def check_response_status_code(self, response: Response, expected: ResponseStatusCode):
        logger.info('Checking response status code value')
        assert response.status_code == expected.value

    @allure.step('Checking response body')
    def check_response_body(self, response: Response, expected: dict):
        logger.info('Checking response boby')
        assert response.json() == expected
