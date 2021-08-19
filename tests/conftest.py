"""pytest plugin configuration.

https://docs.pytest.org/en/latest/writing_plugins.html#conftest-py-plugins
"""

import pytest


@pytest.fixture
def match_list():
    """Return list of matched username, password, and hashes."""
    return [
        {
            "user": "Bill",
            "hash": "d739c6021d574f5f19822feecae9db15",
            "password": "p@ssword",
        },
        {"user": "Jane", "hash": "4c604a4431bf49c1bdcd3b1f458efdd4", "password": "doe"},
        {"user": "John", "hash": "4c604a4431bf49c1bdcd3b1f458efdd4", "password": "doe"},
        {
            "user": "Frank",
            "hash": "50f57adca07aca56d165aaf2d958e03c",
            "password": "YellowFin32!",
        },
        {
            "user": "Jill",
            "hash": "dc35d01a6d8140dd5bf978ea3ab7c3d2",
            "password": "Wash3r",
        },
        {
            "user": "Mike",
            "hash": "d739c6021d574f5f19822feecae9db15",
            "password": "p@ssword",
        },
        {
            "user": "John",
            "hash": "d739c6021d574f5f19822feecae9db15",
            "password": "p@ssword",
        },
        {
            "user": "Sam",
            "hash": "d739c6021d574f5f19822feecae9db15",
            "password": "p@ssword",
        },
        {
            "user": "You",
            "hash": "c8137e7842466aa292c143a9be887755",
            "password": "",
        },
        {
            "user": "Charlie",
            "hash": "fa19f8748a9b52a1138470b446969633",
            "password": "YankyRoad1@",
        },
    ]