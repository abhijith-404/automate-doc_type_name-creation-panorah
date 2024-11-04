import os
import json
import requests  # Make sure to import requests for API calls

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
                    
                    # Add the file name (without .json extension) as doctype_name
                    doctype_name = os.path.splitext(file)[0]
                    json_data["doctype_name"] = doctype_name
                    if "fields" in json_data:
                        for field in json_data["fields"]:
                            if "fieldname" in field:
                                field["name"] = field.pop("fieldname")
                            # Rename fieldtype to field_type
                            if "fieldtype" in field:
                                field["field_type"] = field.pop("fieldtype")

                    json_data["app"] = "core"
                    
                    # Send the modified data to the API
                    response = requests.post(api_endpoint, json=json_data)
                    if response.status_code == 200:
                        print(f"Successfully sent data for {doctype_name}")
                    else:
                        print(f"Failed to send data for {doctype_name}: {response.status_code}")
            
            except json.JSONDecodeError:
                print(f"Error decoding JSON in file: {file_path}")
            except Exception as e:
                print(f"An error occurred with file {file_path}: {e}")
