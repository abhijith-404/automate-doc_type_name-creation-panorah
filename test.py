import json
import requests

# Get values from the user
app = input("Enter the app name: ")
doc_type_name = input("Enter the DocType name: ")

# Initialize an empty list for fields
fields = []

# Ask the user to input field details
while True:
    print("\nEnter field details:")
    field_name = input("Field name: ")
    field_type = input("Field type (e.g., Data, Text): ")
    field_label = input("Field label: ")

    # Append the field information to the fields list
    fields.append({
        "name": field_name,
        "field_type": field_type,
        "label": field_label
    })

    # Ask if the user wants to add another field
    add_another = input("Do you want to add another field? (y/n): ")
    if add_another.lower() != 'y':
        break

# Create the JSON structure
data = {
    "app": app,
    "doc_type_name": doc_type_name,
    "fields": fields
}

# Specify the API endpoint
api_url = "http://127.0.0.1:8000/document"

# Send the JSON data to the API endpoint
try:
    response = requests.post(api_url, json=data)

    # Check if the request was successful
    if response.status_code == 200:
        print("\nData sent successfully!")
        print("Response:", response.json())
    else:
        print("\nFailed to send data.")
        print("Status Code:", response.status_code)
        print("Response:", response.text)

except requests.exceptions.RequestException as e:
    print("An error occurred:", e)
