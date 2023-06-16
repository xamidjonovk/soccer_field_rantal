from django.test import TestCase

# Create your tests here.
import requests
from django.contrib.gis.geos import Point

def sign_up():
    url = 'http://127.0.0.1:8000/v1/users/signup/'
    latitude = 10.1234
    longitude = 20.5678
    point = Point(longitude, latitude)

    data = {
        'username': 'john.doe5',
        'email': 'john.doe@example.com',
        'password': 'mypassword',
        'role': 'owner',  # Replace with the desired role: 'owner' or 'user'
        'language': 'uz',
        'phone_number': '998996789090',
        'location': point.wkt
    }

    response = requests.post(url, json=data)

    if response.status_code == 201:
        print('User signed up successfully!')
    else:
        print('Failed to sign up:', response.json())


def signin():
    import requests

    # Define the API endpoint URL
    url = 'http://127.0.0.1:8000/v1/users/signin/'


    # Define the request payload with the username and password
    data = {
        'username': 'john.doe5',
        'password': 'mypassword',
    }

    # Send the POST request to the sign-in endpoint
    response = requests.post(url, data=data)

    # Check the response status code
    if response.status_code == 200:
        # Sign-in successful
        json_response = response.json()
        access_token = json_response['access']
        refresh_token = json_response['refresh']
        print("access:", access_token)
        # Store the tokens or use them for further authenticated requests
    else:
        # Sign-in failed
        print('Failed to sign in. Response:', response.text)

# signin()
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg3MTc3ODU1LCJpYXQiOjE2ODcwOTE0NTUsImp0aSI6IjNlYTk2Yjk1NjRmYjQ3ODA5MzY5YzM3NDYyYTVmMzU3IiwidXNlcl9pZCI6MTB9.tZfBYvrIDTCGBGJvgjsD3isEV9ihu1SCukvqB5eB3dg"

def create_field():
    import requests

    # Define the API endpoint URL
    url = 'http://127.0.0.1:8000/v1/rental/fields/'
    latitude = 15.1234
    longitude = 21.5678
    point = Point(longitude, latitude)
    # Define the request payload with the field data
    data = {
        'name': 'Sport1',
        'address': 'Tashkent',
        'contact': '9989986773456',
        'price_per_hour': 10.0,
        'location': point.wkt,
        'owner':7

        # Include other field properties as needed
    }

    # Define the request headers with the JWT access token
    headers = {
        'Authorization': f'Bearer {token}',
    }

    # Send the POST request to create the field with the access token included in the headers
    response = requests.get(url, data=data, headers=headers)

    # Check the response status code
    if response.status_code == 201:
        # Field creation successful
        json_response = response.json()
        field_id = json_response['id']
        print(field_id)
    else:
        # Field creation failed
        print('Failed to create field. Response:', response.text)

# create_field()

def list_fields():
    import requests

    # Define the API endpoint URL for listing fields
    url = 'http://127.0.0.1:8000/v1/rental/fields/'
    params = {
        'start_time': '2023-06-20T10:00:00',
        'end_time': '2023-06-20T12:00:00'
    }

    # Define the request headers if needed (e.g., for authentication)
    headers = {
        'Authorization': f'Bearer {token}',
    }

    # Send the GET request to retrieve the list of fields
    response = requests.get(url, headers=headers, params=params)

    # Check the response status code
    if response.status_code == 200:
        # Fields retrieval successful
        json_response = response.json()
        fields = json_response['results']
        # Process the fields list or perform further actions
        print(fields)
    else:
        # Fields retrieval failed
        print('Failed to retrieve fields. Response:', response.text)

list_fields()


