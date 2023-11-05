import ckan.plugins.toolkit as tk
import ckanext.theming.logic.schema as schema


@tk.side_effect_free
def theming_get_sum(context, data_dict):
    tk.check_access(
        "theming_get_sum", context, data_dict)
    data, errors = tk.navl_validate(
        data_dict, schema.theming_get_sum(), context)

    if errors:
        raise tk.ValidationError(errors)

    return {
        "left": data["left"],
        "right": data["right"],
        "sum": data["left"] + data["right"]
    }


def get_actions():
    return {
        'theming_get_sum': theming_get_sum,
    }
