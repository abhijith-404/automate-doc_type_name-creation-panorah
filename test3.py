import os
import json

# Specify the directory containing folders with JSON files
doctype_dir = "doctype"

# Initialize a list to store data from each JSON file
combined_data = []

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
                    
                    # Append the modified data to the combined data list
                    combined_data.append(json_data)
            except json.JSONDecodeError:
                print(f"Error decoding JSON in file: {file_path}")
            except Exception as e:
                print(f"An error occurred with file {file_path}: {e}")

# Specify the output file for the combined JSON data
output_file = "combined_data4.json"

# Write the combined data to a single JSON file
with open(output_file, "w") as f:
    json.dump(combined_data, f, indent=4)

print(f"All JSON data has been combined and saved to '{output_file}' with 'doctype_name' added.")
