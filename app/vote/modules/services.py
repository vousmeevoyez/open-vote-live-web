"""
    Services
    ________________
    this is where we communicate with server
"""
import requests
import json

from app.config.config import Config

BASE_URL = Config.BASE_URL
ROUTES = Config.ROUTES
TIMEOUT = Config.TIMEOUT

class VoteServices:

    def __init__(self, username=None, password=None, token=None):
        if username and password:
            self._token = self.get_token(username, password)
        else:
            self._token = token

    def remote_call(self, routes, payload=None, identifier=None):
        """ remote call"""
        # append identifier to URL
        status = True

        if identifier is not None:
            url = BASE_URL + ROUTES[routes]
            url = url.format(identifier)
        else:
            url = BASE_URL + ROUTES[routes]

        # set token only if its not login
        if routes != "LOGIN":
            headers = {
                "Authorization" : "Bearer {}".format(self._token)
            }
        else:
            headers = {}

        if payload is not None:
            response = requests.post(
                url,
                data=payload,
                timeout=TIMEOUT,
                headers=headers
            )
        else:
            response = requests.get(
                url,
                timeout=TIMEOUT,
                headers=headers
            )
        if not response.ok:
            status = False
        
        response = response.json()
        return status, response

    def get_token(self, username, password):
        routes = "LOGIN"
        payload = {
            "username" : username,
            "password" : password
        }
        status, response = self.remote_call(routes, payload)
        access_token = response["data"]["access_token"]
        return access_token

    def get_candidates(self, election_id):
        routes = "CANDIDATES"
        status, response = self.remote_call(routes, None, election_id)
        return status, response