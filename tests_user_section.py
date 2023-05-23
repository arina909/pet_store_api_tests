import allure

from sections.base import ResponseStatusCode
from sections.user import User

NEW_USER = {'user_id': 111,
            'username': 'johnny',
            'first_name': 'Johnny',
            'last_name': 'Depp',
            'email': 'johnny@gmail.com',
            'password': 'strongpassword',
            'phone': '911',
            'user_status': 1}
UPDATED_USER = {'user_id': 111,
                'username': 'johnny',
                'first_name': 'John',
                'last_name': 'Depp',
                'email': 'johnny@gmail.com',
                'password': 'strongpassword',
                'phone': '911',
                'user_status': 2}

"""User section related tests for PetStore server"""


@allure.description('Test checks inability to delete the same user twice: '
                    'user should be not found')
def test_delete_user_request_cant_performed_twice():
    (user := User()).create_user(**NEW_USER)
    user.log_in_user(NEW_USER['username'], NEW_USER['password'])
    user.delete_user(NEW_USER['username'])
    response = user.delete_user(NEW_USER['username'])
    user.check_response_status_code(response, ResponseStatusCode.NOT_FOUND)


@allure.description('Test checks that user info is changed after performed changes')
def test_user_info_changed_after_changes():
    (user := User()).create_user(**NEW_USER)
    user.log_in_user(NEW_USER['username'], NEW_USER['password'])
    updated_user_info, response = user.change_user_info(**UPDATED_USER)
    user.check_response_status_code(response, ResponseStatusCode.OK)
    response = user.get_user_info(UPDATED_USER['username'])
    user.check_response_body(response, updated_user_info)
