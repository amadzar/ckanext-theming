"""Tests for validators.py."""

import pytest

import ckan.plugins.toolkit as tk

from ckanext.theming.logic import validators


def test_theming_reauired_with_valid_value():
    assert validators.theming_required("value") == "value"


def test_theming_reauired_with_invalid_value():
    with pytest.raises(tk.Invalid):
        validators.theming_required(None)
