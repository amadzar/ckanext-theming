import ckan.plugins.toolkit as tk


def theming_required(value):
    if not value or value is tk.missing:
        raise tk.Invalid(tk._("Required"))
    return value


def get_validators():
    return {
        "theming_required": theming_required,
    }
