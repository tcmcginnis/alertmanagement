#!/usr/bin/python3
import os
import trace
from pdpyras import APISession
# basic REST API key
# Need to generate from PagerDuty at:
#   https://developer.pagerduty.com/api-reference/e65c5833eeb07-pager-duty-api
api_key="y_NbAkKc66ryYTWUXYEu"
session = APISession(api_key, default_from="https://api.pagerduty.com")
print("Session:",session)

# OAuth2
# oauth_token_here="y_NbAkKc66ryYTWUXYEu"
# session = APISession(oauth_token_here, auth_type='oauth2')
# print("Session:",session)


# Querying: Find a user exactly matching email address
user = session.find('users', 'tom@mclabs.us', attribute='email')
print("user:",user)

user = session.find('users', '')
print("user:",user)

services = session.list_all('services', params={'query': 'S'})
print("services:",services)
