import logging

import allure
import requests
from requests import Response

from sections.base import Base, BASE_URL

CREATE_USER_WITH_LIST = 'createWithList'
LOGIN_USER = 'login'


class User(Base):
    """User section related methods"""
    def __init__(self):
        self.url = BASE_URL.format('/user/{}')

    @staticmethod
    def _configurate_user_request_body(user_id: int,
                                       username: str,
                                       first_name: str,
                                       last_name: str,
                                       email: str,
                                       password: str,
                                       phone: str,
                                       user_status: int) -> dict:
        request_body = {
            'id': user_id,
            'username': username,
            'firstName': first_name,
            'lastName': last_name,
            'email': email,
            'password': password,
            'phone': phone,
            'userStatus': user_status
        }
        return request_body

    @allure.step('Create a new user')
    def create_user(self,
                    user_id: int,
                    username: str,
                    first_name: str,
                    last_name: str,
                    email: str,
                    password: str,
                    phone: str,
                    user_status: int) -> Response:
        logging.info('Creating a new user')
        request_body = self._configurate_user_request_body(user_id, username, first_name, last_name,
                                                           email, password, phone, user_status)
        return requests.post(self.url.format(CREATE_USER_WITH_LIST), json=[request_body])

    @allure.step('Log in user into the system')
    def log_in_user(self,
                    username: str,
                    password: str) -> Response:
        logging.info('Logging in user into the system')
        return requests.get(self.url.format(LOGIN_USER),
                            params={'username': username, 'password': password})

    @allure.step('Delete user')
    def delete_user(self, username: str) -> Response:
        logging.info('Deleting user from the system')
        return requests.delete(self.url.format(username))

    @allure.step('Change user info')
    def change_user_info(self,
                         user_id: int,
                         username: str,
                         first_name: str,
                         last_name: str,
                         email: str,
                         password: str,
                         phone: str,
                         user_status: int) -> tuple[dict, Response]:
        logging.info('Changing user info in the system')
        request_body = self._configurate_user_request_body(user_id, username, first_name, last_name,
                                                           email, password, phone, user_status)
        return request_body, requests.put(self.url.format(username), json=request_body)

    @allure.step('Get user info')
    def get_user_info(self, username: str):
        logging.info('Getting user info from the system')
        return requests.get(self.url.format(username))
