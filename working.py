# This is working well 04-11-24
import os
import json
import requests  # Ensure requests is installed by running `pip install requests`

# Specify the directory containing folders with JSON files
doctype_dir = "report"

# API endpoint to which data should be sent
api_endpoint = "http://127.0.0.1:8000/document"  # Replace with the actual API URL

# Define the allowed field types based on your field_mapping dictionary
valid_field_types = {
    "Data", "Text", "Autocomplete", "Attach", "AttachImage", "Barcode", "Check", "Code",
    "Color", "Currency", "Date", "Datetime", "Duration", "DynamicLink", "Float", "HTMLEditor",
    "Int", "JSON", "Link", "LongText", "MarkdownEditor", "Password", "Percent", "Phone", 
    "ReadOnly", "Rating", "Select", "SmallText", "TextEditor", "Time", "Table", "TableMultiSelect"
}

# Walk through each subfolder in the doctype directory
for root, dirs, files in os.walk(doctype_dir):
    for file in files:
        # Check if the file has a .json extension
        if file.endswith(".json"):
            file_path = os.path.join(root, file)
            try:
                # Open and read the JSON file
                with open(file_path, 'r') as f:
                    json_data = json.load(f)
                    
                    # Prepare minimal data structure
                    minimal_data = {
                        "app": "report",  # Static value as per your example
                        "doc_type_name": os.path.splitext(file)[0],
                        "fields": []
                    }
                    
                    # Populate fields with required properties only if field_type is valid
                    if "fields" in json_data:
                        for field in json_data["fields"]:
                            field_type = field.get("fieldtype", "")
                            if field_type.replace(" ", "") in valid_field_types:
                                minimal_field = {
                                    "name": field.get("fieldname", ""),
                                    "field_type": field_type.replace(" ", ""),
                                    "label": field.get("label", "")
                                }
                                minimal_data["fields"].append(minimal_field)
                            else:
                                print(f"Skipping invalid field_type '{field_type}' for field '{field.get('fieldname', '')}'")

                    # Send the minimal data to the API
                    response = requests.post(api_endpoint, json=minimal_data)
                    
                    # Check for success and detailed error handling
                    if response.status_code == 200:
                        print(f"Successfully sent data for {minimal_data['doc_type_name']}")
                    else:
                        # Log detailed error information
                        print(f"Failed to send data for {minimal_data['doc_type_name']}: Status Code {response.status_code}")
                        try:
                            # Attempt to parse and print the error response JSON
                            error_details = response.json()
                            print("Error details:", json.dumps(error_details, indent=4))
                        except json.JSONDecodeError:
                            # If response is not JSON, print raw text
                            print("Error response (non-JSON):", response.text)

            except json.JSONDecodeError:
                print(f"Error decoding JSON in file: {file_path}")
            except requests.RequestException as e:
                print(f"An HTTP error occurred while sending data for {file_path}: {e}")
            except Exception as e:
                print(f"An unexpected error occurred with file {file_path}: {e}")