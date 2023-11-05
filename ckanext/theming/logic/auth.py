import ckan.plugins.toolkit as tk


@tk.auth_allow_anonymous_access
def theming_get_sum(context, data_dict):
    return {"success": True}


def get_auth_functions():
    return {
        "theming_get_sum": theming_get_sum,
    }