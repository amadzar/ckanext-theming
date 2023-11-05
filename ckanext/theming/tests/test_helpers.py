"""Tests for helpers.py."""

import ckanext.theming.helpers as helpers


def test_theming_hello():
    assert helpers.theming_hello() == "Hello, theming!"
