import json
import os

"""
Is_child not handled
"""
version = "v2"
APP_NAME = "inv2"

rootdir = 'inventory'
field_type_keys = (
    "Data", "Text", "Autocomplete", "Attach", "AttachImage", "Barcode",
    "Check", "Code", "Color", "Currency", "Date", "Datetime", "Duration",
    "DynamicLink", "Float", "HTMLEditor", "Int", "JSON", "Link", "LongText",
    "MarkdownEditor", "Navbutton", "Password", "Percent", "Phone", "ReadOnly",
    "Rating", "Select", "SmallText", "TextEditor", "Time", "Table",
    "TableMultiSelect"
)

def get_field_type(field):

    fields = {
        "name": field.get("fieldname"),
        "field_type": field.get("fieldtype"),
        "label": field.get("label"),
        "hidden": field.get("hidden", 0),
        "read_only": field.get("read_only", 0),
        "in_list_view": field.get("in_list_view", 0),
        "in_filter": field.get("in_filter", 1),
        "bold": field.get("bold", 0),
        "allow_in_quick_entry": field.get("allow_in_quick_entry", 0),
        "in_preview": field.get("in_preview", 0),
        "unique": field.get("unique", 0),
        "options": field.get("options").replace(" ", "_").lower() if field.get("fieldtype") in ["Link", "Table"] else field.get("options"),
        }
    return fields

def set_metadata(meta):
    naming = {
            "name": "naming_series",
            "field_type": "Select",
            "label": "Naming series",
            "options": "INV-{MM}-{####}"
        }
    return {
        "app": APP_NAME,
        "doc_type_name": meta.get("name").replace(" ", "_").lower() + "_v1",
        "fields": [get_field_type(i) for i in content["fields"] if (i["fieldtype"] in field_type_keys) and (i["fieldname"] != "naming_series")] + [naming],
        "naming_rule": {"naming_rule": "naming_series", "naming_series": "INV-{MM}-{####}"},
        "view_layout_type": 0,
        "show_print_button": 1,
        "show_create": 1
    }


whole_json = {}
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        if file.endswith(".json"):
            with open(os.path.join(subdir, file), 'r') as f:
                content = json.load(f)
            whole_json[content["name"].replace(" ", "_").lower()] = set_metadata(content)
            # whole_json[content["name"].replace(" ", "_").lower()] = [get_field_type(i) for i in content["fields"] if i["fieldtype"] in field_type_keys]

with open(f'for_meta/{version}/metajson.json', 'w') as f:
    json.dump(whole_json, f, indent=4)
