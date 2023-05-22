import allure
import pytest

from sections.base import ResponseStatusCode
from sections.pet import Pet, PetStatus

INVALID_PET_ID = 'cat'

"""Pet section related tests for PetStore server"""


@pytest.mark.parametrize('status', PetStatus)
@allure.description('Test checks that only pets with requested status are shown')
def test_only_pets_with_requested_status_shown(status: PetStatus):
    response = (pet := Pet()).find_pets_by_status(status)
    pet.check_pets_only_with_requested_status_shown(response, status)


@pytest.mark.xfail(reason='If pet id has wrong format 400 response status (bad request) '
                          'should be returned but actual is 404 (not found)')
@allure.description('Test checks that invalid response status value returned '
                    'if pet id has not int type')
def test_invalid_response_status_if_invalid_pet_id():
    response = (pet := Pet()).find_pet_by_id(INVALID_PET_ID)
    pet.check_response_status_code(response, ResponseStatusCode.BAD_REQUEST)
