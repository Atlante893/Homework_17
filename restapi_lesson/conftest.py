import pytest

from Homework_17.restapi_lesson.class_object.user_data_class import User
from Homework_17.restapi_lesson.class_object.color_class import Color


@pytest.fixture
def create_user():
    return User("janet.weaver@reqres.in", "Janet", "Weaver")


@pytest.fixture
def create_color():
    return Color(3, "true red", 2002, "#BF1932", "19-1664")
