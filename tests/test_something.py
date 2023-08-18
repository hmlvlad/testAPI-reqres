import requests
from configuration import SERVICE_URL
from src.enums.global_enums import GlobalErrorMessages


def test_get_list_user():
    response = requests.get(url=SERVICE_URL)
    assert response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value
    print(response.json())

