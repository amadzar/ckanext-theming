"""Tests for views.py."""

import pytest

import ckanext.theming.validators as validators


import ckan.plugins.toolkit as tk


@pytest.mark.ckan_config("ckan.plugins", "theming")
@pytest.mark.usefixtures("with_plugins")
def test_theming_blueprint(app, reset_db):
    resp = app.get(tk.h.url_for("theming.page"))
    assert resp.status_code == 200
    assert resp.body == "Hello, theming!"
