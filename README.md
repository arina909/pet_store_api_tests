# pet_store_api_tests
project with autotests for Petstore server https://petstore.swagger.io/v2

Input parametrs: OAS3 specification stored at ./service_info/petstore.yaml

Test project based on:
- Python3
- Pytest   (https://github.com/pytest-dev/pytest)
- requests (https://github.com/psf/requests)

Prerequisites and Setup istructions:
1. Python 3.10 (https://www.python.org/downloads/)
2. Install requirements ```pip install -r requirements.txt```

Test run:
1. Run tests (example: ```py.test tests_user_section.py --alluredir=reports```)
2. Collect allure report (```allure serve reports```) and enjoy the results!
