
import json
import time

import requests

api_endpoint = "http://127.0.0.1:8001/document"

with open('metajson.json', 'r') as f:
    context = json.load(f)

failed_meta = {}
success_meta = {}
exception_meta = {}
auth_token = 'eyJhbGciOiJSUzI1NiIsImtpZCI6IjgxYjUyMjFlN2E1ZGUwZTVhZjQ5N2UzNzVhNzRiMDZkODJiYTc4OGIiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vcGFub3JhaC02YjM2ZiIsImF1ZCI6InBhbm9yYWgtNmIzNmYiLCJhdXRoX3RpbWUiOjE3MzgzMTI5NzcsInVzZXJfaWQiOiJ1MHdId1FxcGxZUGREU0k2RnhxcEgzWW9tTXIyIiwic3ViIjoidTB3SHdRcXBsWVBkRFNJNkZ4cXBIM1lvbU1yMiIsImlhdCI6MTczODMxMjk3NywiZXhwIjoxNzM4MzE2NTc3LCJlbWFpbCI6InRlc3RAdXNlci5jb20iLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsImZpcmViYXNlIjp7ImlkZW50aXRpZXMiOnsiZW1haWwiOlsidGVzdEB1c2VyLmNvbSJdfSwic2lnbl9pbl9wcm92aWRlciI6InBhc3N3b3JkIn19.kRjrCIblyTQvJl1hFeGFtx9Uz-mc2jBQIXom1wZvFjnFvrghAGIKRSxTpHzfWnBIXbTNyZR0AnZbUoiLTIOA2C9lPhOx8H0aCZV2RYs7b5zyP0V-Y6kE4XM0iInu3O0tmtRCcGimGbL9fu5mkM6Snpu9t12r8ksRBGgXJwf7eyY5XVx5-b_FsZwilYQUjb8ap6ay3dvp0U2YDpLum7QiZPDwiVtBTBOH9lQ_Aw4W0P68iWZbQrTj80Msu43rp5yk_Fms1Y8XXYawGl1g4AXnzGWPWQzCTTPbPJN7up2QmadSXYRP-40YBKnAK6esJN3QX9OqFb0zGr0debIzcujlfg'
headers = {'Authorization': f'Bearer {auth_token}'}


for key, value in context.items():
    try:
        response = requests.post(api_endpoint, json=value, headers=headers)

        # Check for success and detailed error handling
        if response.status_code == 201:
            success_meta[key] = value
            print(f"Successfully sent data for {key}")
        else:
            failed_meta[key] = value
            # Log detailed error information
            print(f"Failed to send data for {key}: Status Code {response.status_code}")
    except Exception as e:
        exception_meta[key] = value
        print(f"An unexpected error occurred with file {key}: {e}")

with open('create_doctype/failed_meta.json', 'w') as f:
    json.dump(failed_meta, f, indent=4)

with open('create_doctype/exception_meta.json', 'w') as f:
    json.dump(exception_meta, f, indent=4)

with open('create_doctype/success_meta.json', 'w') as f:
    json.dump(success_meta, f, indent=4)

