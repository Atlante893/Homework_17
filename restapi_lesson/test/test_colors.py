import json
from http import HTTPStatus

from Homework_17.restapi_lesson.api.colors_api import ColorsAPI
from Homework_17.restapi_lesson.class_object.color_class import Color


def test_get_color_response():
    response = ColorsAPI().get_color(color_id=2)
    assert response.reason == 'OK'
    assert response.status_code == HTTPStatus.OK, f'\nStatus code is not as expected\nActual: {response.status_code}' \
                                                  f'\nExpected: {HTTPStatus.OK}'


def test_get_color_fixture_description(create_color):
    response = ColorsAPI().get_color(color_id=3)
    json_color = json.loads(response.text)['data']
    expected_color = create_color
    actual_color = Color(json_color['id'], json_color['name'], json_color['year'], json_color['color'], json_color['pantone_value'])
    assert actual_color == expected_color, f"\nColor is not as expected"


def test_get_color_name():
    response = ColorsAPI().get_color(color_id=4)
    json_color = json.loads(response.text)['data']['name']
    assert json_color == 'aqua sky', f"\nColor is not as expected"



