import json
from http import HTTPStatus
from Homework_17.restapi_lesson.api.users_api import UsersApi
from Homework_17.restapi_lesson.class_object.user_data_class import User


def test_get_single_user_response():
    response = UsersApi().get_user(user_id=2)
    assert response.reason == 'OK'
    assert response.status_code == HTTPStatus.OK, f'\nStatus code is not as expected\nActual: {response.status_code}' \
                                                  f'\nExpected: {HTTPStatus.OK}'


def test_get_single_user_not_found_error():
    response = UsersApi().get_user(user_id=23)
    assert response.status_code == HTTPStatus.NOT_FOUND, f'\nStatus code is not as expected' \
                                                         f'\nActual: {response.status_code}' \
                                                         f'\nExpected: {HTTPStatus.NOT_FOUND}'


def test_get_response_json_fixture(create_user):
    response = UsersApi().get_user(user_id=2)
    json_user = json.loads(response.text)['data']
    expected_user = create_user
    actual_user = User(json_user['email'], json_user['first_name'], json_user['last_name'])
    assert actual_user == expected_user, f"\nPerson is not as expected"


def test_post_create_new_person():
    response = UsersApi().post_user()
    assert response.reason == 'Created'
    assert json.loads(response.text)['name'] == 'Pavlo'
    assert response.status_code == HTTPStatus.CREATED, f'\nStatus code is not as expected\nActual: {response.status_code}' \
                                                  f'\nExpected: {HTTPStatus.Created}'


def test_put_update_name_person():
    response = UsersApi().put_user()
    assert json.loads(response.text)['name'] == 'Pavlo_Yeshchenko'
    assert response.reason == 'OK'
    assert response.status_code == HTTPStatus.OK, f'\nStatus code is not as expected\nActual: {response.status_code}' \
                                                  f'\nExpected: {HTTPStatus.OK}'


def test_patch_update_name_person():
    response = UsersApi().patch_user()
    assert response.reason == 'OK'
    assert json.loads(response.text)['name'] == 'Yeshchenko'
    assert response.status_code == HTTPStatus.OK, f'\nStatus code is not as expected\nActual: {response.status_code}' \
                                                  f'\nExpected: {HTTPStatus.OK}'


def test_delete_person():
    response = UsersApi().delete_user()
    assert response.reason == 'No Content'
    assert response.status_code == HTTPStatus.NO_CONTENT, f'\nStatus code is not as expected\nActual: {response.status_code}' \
                                                  f'\nExpected: {HTTPStatus.NO_CONTENT}'
