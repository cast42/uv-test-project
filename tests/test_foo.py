from uv_test_project.foo import foo


def test_foo():
    assert foo("foo") == "foo"
