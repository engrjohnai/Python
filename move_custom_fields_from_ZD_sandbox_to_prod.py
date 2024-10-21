import requests
from requests.auth import HTTPBasicAuth


# Replace with your details
sandbox_subdomain = ''
production_subdomain = ''
email_address = ''
sandbox_api_token = ''
production_api_token = ''
custom_field_ids = []


# Headers for the requests
headers = {
    "Content-Type": "application/json",
}


# Authentication for sandbox and production using HTTPBasicAuth
sandbox_auth = HTTPBasicAuth(f'{email_address}/token', sandbox_api_token)
production_auth = HTTPBasicAuth(f'{email_address}/token', production_api_token)

# Zendesk API URLs
sandbox_url_template = f'https://{sandbox_subdomain}.zendesk.com/api/v2/ticket_fields/{{}}.json'
production_url = f'https://{production_subdomain}.zendesk.com/api/v2/ticket_fields.json'


# Store retrieved custom fields
custom_fields = []

#Step 1: Retrieve each custom field by ID from the sandbox
print("Retrieving custom fields from sandbox...")
for field_id in custom_field_ids:
    sandbox_url = sandbox_url_template.format(field_id)
    response = requests.get(sandbox_url, auth=sandbox_auth, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        field_data = response.json().get('ticket_field')
        if field_data:
            custom_fields.append(field_data)
            print(f"Retrieved field with ID {field_id}: {field_data['title']}")
        else:
            print(f"No 'ticket_field' data found for ID {field_id}. Response content: {response.json()}")
    else:
        print(f"Failed to retrieve field with ID {field_id}. Status code: {response.status_code}")
        print("Error message:", response.text)

# Step 2: Create retrieved custom fields in the production environment
print("\nCreating custom fields in production...")
for field in custom_fields:
    # Prepare the data for creating a new field in production
    field_data = {
        'ticket_field': {
            'type': field['type'],
            'title': field['title'],
            'description': field['description'],
            'position': field['position'],
            'custom_field_options': field.get('custom_field_options', []),
            'required': field.get('required', False),
            'active': field.get('active', True)
        }
    }

    # Create the custom field in production
    prod_response = requests.post(production_url, json=field_data, auth=production_auth, headers=headers)

    # Check if the field creation was successful
    if prod_response.status_code == 201:
        print(f"Custom field '{field['title']}' created successfully in production.")
    else:
        print(f"Failed to create custom field '{field['title']}'. Status code: {prod_response.status_code}")
        print("Error message:", prod_response.text)
