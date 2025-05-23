import os
import json
import requests  # Ensure requests is installed by running `pip install requests`

# Specify the directory containing folders with JSON files
doctype_dir = "doctype"

# API endpoint to which data should be sent
api_endpoint = "http://127.0.0.1:8000/document"  # Replace with the actual API URL

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
                        "app": "core",  # Static value as per your example
                        "doc_type_name": os.path.splitext(file)[0],
                        "fields": []
                    }
                    
                    # Populate fields with required properties only
                    if "fields" in json_data:
                        for field in json_data["fields"]:
                            minimal_field = {
                                "name": field.get("fieldname", ""),
                                "field_type": field.get("fieldtype", ""),
                                "label": field.get("label", "")
                            }
                            minimal_data["fields"].append(minimal_field)

                    # Send the minimal data to the API
                    response = requests.post(api_endpoint, json=minimal_data)
                    if response.status_code == 200:
                        print(f"Successfully sent data for {minimal_data['doc_type_name']}")
                    else:
                        print(f"Failed to send data for {minimal_data['doc_type_name']}: {response.status_code}")
            
            except json.JSONDecodeError:
                print(f"Error decoding JSON in file: {file_path}")
            except Exception as e:
                print(f"An error occurred with file {file_path}: {e}")
