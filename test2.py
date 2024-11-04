import os
import json
import random

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
                    if "fields" in json_data:
                        # json_data["fields"]["name"] = json_data["fields"].pop("fieldname")
                        print('----------\n\n\n')
                        print(json_data["fields"])
                        for i in json_data["fields"]:
                            if "fieldname" in i:
                                # json_data["fields"]["name"] = json_data["fields"].pop("fieldname")
                                print('jjjjj')
                                
                                print('jjjjj2222')
                                i["name"] = i.pop("fieldname")
                    combined_data.append(json_data)
            except json.JSONDecodeError:
                print(f"Error decoding JSON in file: {file_path}")
            except Exception as e:
                print(f"An error occurred with file {file_path}: {e}")
    if random.randint(1, 10) == 1:
        break

# Specify the output file for the combined JSON data
output_file = "combined_data.json"

# Write the combined data to a single JSON file
with open(output_file, "w") as f:
    json.dump(combined_data, f, indent=4)

print(f"All JSON data has been combined and saved to '{output_file}'")
