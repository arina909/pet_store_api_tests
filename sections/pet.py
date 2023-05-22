from enum import Enum
import logging
import allure
import requests
from requests import Response

from sections.base import Base, BASE_URL

FIND_PETS_BY_STATUS = BASE_URL.format('/pet/findByStatus/')
FIND_PETS_BY_ID = BASE_URL.format('/pet/{}')


class PetStatus(Enum):
    """Status values for pets filter"""
    AVAILABLE = 'available'
    PENDING = 'pending'
    SOLD = 'sold'


class Pet(Base):
    """Pet section related methods"""

    @allure.step('Find pets by status')
    def find_pets_by_status(self, status: PetStatus) -> Response:
        logging.info('Finding pets by status')
        request_params = {'status': status.value}
        return requests.get(FIND_PETS_BY_STATUS, params=request_params)

    @allure.step('Check pets only with requested status are shown')
    def check_pets_only_with_requested_status_shown(self,
                                                    response: Response,
                                                    status: PetStatus) -> None:
        logging.info('Checking if pets only with requested status are shown')
        if response.json():  # could be empty if there are no pets with requested status
            for pet_info in response.json():
                assert pet_info['status'] == status.value

    @allure.step('Find pet by id')
    def find_pet_by_id(self, pet_id: int | str) -> Response:
        logging.info('Finding pets by id')
        return requests.get(FIND_PETS_BY_ID.format(pet_id))
