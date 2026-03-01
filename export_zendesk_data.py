import requests
from requests.auth import HTTPBasicAuth
import json
import csv

# API endpoint for ticket fields
base_url = "https://{subdomain}.zendesk.com/api/v2/tickets.json?page="

# API authentication
email_address = '' # Enter your email address here
api_token = '' # Enter your api token key here

# Set headers
headers = {
    "Content-Type": "application/json",
}

# Use basic authentication
auth = HTTPBasicAuth(f'{email_address}/token', api_token)

# List to hold all ticket data
filtered_tickets = []

# Initialize the page counter
page = 1

while True:
    # Construct the URL for the current page
    url = f"{base_url}{page}"

    # Send the GET request to retrieve tickets
    response = requests.get(url, auth=auth, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse JSON response
        data = response.json()
        tickets = data.get('tickets', [])

        # Break the loop if there are no more tickets
        if not tickets:
            break

        # Iterate over the tickets and filter based on custom fields
        # You can add more fileds that is needed.
        for ticket in tickets:
            ticket_data = {
                'id': ticket.get('id'),
                'created_at': ticket.get('created_at'),
                'subject': ticket.get('subject'),
                'requester_id': ticket.get('requester_id'),
                'custom_fields': {}
            }

            # Initialize a flag to check if any relevant custom field has data
            has_custom_field_data = False

            # Extract the relevant custom fields based on specified IDs
            for custom_field in ticket.get('custom_fields', []):
                field_id = custom_field.get('id')
                field_value = custom_field.get('value')
                
                # Store the value if the custome_field ID matches one of the specified custom_fields IDs
                if field_id in {
                    1234567898 # Replace it with the appropriate custom_field ids
                } and field_value is not None:
                    ticket_data['custom_fields'][field_id] = field_value
                    has_custom_field_data = True  # Set flag to True if there is data

            # Only append to the results if there is data in any of the relevant custom fields
            if has_custom_field_data:
                filtered_tickets.append(ticket_data)

        # Check if there's a next page
        if not data.get('next_page'):
            break
        else:
            page += 1
    else:
        print(f"Failed to retrieve tickets: {response.status_code}")
        break

# Write the filtered ticket data to a CSV file
with open('filtered_tickets.csv', 'w', newline='') as csvfile:
    fieldnames = ['id', 'created_at', 'subject', 'requester_id'] + \
                 [f'custom_field_{field_id}' for field_id in [
                     12345678998 # Repalce it with the custom_fields IDs
                 ]]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for ticket in filtered_tickets:
        # Prepare row for the CSV
        row = {
            'id': ticket['id'],
            'created_at': ticket['created_at'],
            'subject': ticket['subject'],
            'requester_id': ticket['requester_id']
        }
        # Add custom fields to the row
        for field_id in ticket['custom_fields']:
            row[f'custom_field_{field_id}'] = ticket['custom_fields'][field_id]

        writer.writerow(row)

print("Filtered tickets data written to filtered_tickets.csv")
