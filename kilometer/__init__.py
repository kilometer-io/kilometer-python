# -*- coding: utf-8 -*-
"""
Copyright 2016 Kilometer.io

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
from __future__ import absolute_import, unicode_literals
import time

import requests


class EventsAPIClient(object):
    """
    Events API Client is used to transmit events and manage users data
    """
    HEADER_CUSTOMER_APP_ID = "Customer-App-Id"
    HEADER_TIMESTAMP = "Timestamp"
    HEADER_CLIENT_TYPE = "Client-Type"
    HEADER_CONTENT_TYPE = "Content-Type"
    CLIENT_TYPE = "python"
    CONTENT_TYPE = "application/json"

    def __init__(self, token, endpoint_url=None, request_timeout=None):
        """
        :param str token: Customers' token
        :param str endpoint_url: override the default Events API endpoint
        :raises KilometerException
        """
        self._token = token
        self._endpoint_url = endpoint_url or "https://events.kilometer.io"
        self._request_timeout = request_timeout

    def add_user(self, user_id, headers=None, endpoint_url=None):
        """
        Creates a new identified user if he doesn't exist.

        :param str user_id: identified user's ID
        :param dict headers: custom request headers (if isn't set default values are used)
        :param dict endpoint_url: where to send the request (if isn't set default value is used)
        :return: Response
        """
        endpoint_url = endpoint_url or self._endpoint_url

        url = endpoint_url + '/users'
        headers = headers or self._default_headers()
        payload = {"user_id": user_id}

        response = requests.post(url, headers=headers, json=payload)

        return response

    def add_event(self, user_id, event_name, event_properties=None, headers=None, endpoint_url=None):
        """
        Send an identified event. If a user doesn't exist it will create one.

        :param str user_id: identified user's ID
        :param str event_name: event name (e.g. "visit_website")
        :param dict event_properties: properties that describe the event's details
        :param dict headers: custom request headers (if isn't set default values are used)
        :param dict endpoint_url: where to send the request (if isn't set default value is used)
        :return: Response
        """
        endpoint_url = endpoint_url or self._endpoint_url

        url = endpoint_url + '/events'
        headers = headers or self._default_headers()

        event_properties = event_properties or {}
        payload = {
            "user_id": user_id,
            "event_name": event_name,
            "event_type": "identified",
            "event_properties": event_properties
        }

        response = requests.post(url, headers=headers, json=payload)

        return response

    def increase_user_property(self, user_id, property_name, value=0, headers=None, endpoint_url=None):
        """
        Increase a user's property by a value.

        :param str user_id: identified user's ID
        :param str property_name: user property name to increase
        :param number value: amount by which to increase the property
        :param dict headers: custom request headers (if isn't set default values are used)
        :param dict endpoint_url: where to send the request (if isn't set default value is used)
        :return: Response
        """
        endpoint_url = endpoint_url or self._endpoint_url

        url = endpoint_url + "/users/" + user_id + "/properties/" + property_name + "/increase/" + value.__str__()
        headers = headers or self._default_headers(content_type=None)

        response = requests.post(url, headers=headers)

        return response

    def decrease_user_property(self, user_id, property_name, value=0, headers=None, endpoint_url=None):
        """
        Decrease a user's property by a value.

        :param str user_id: identified user's ID
        :param str property_name: user property name to increase
        :param number value: amount by which to decrease the property
        :param dict headers: custom request headers (if isn't set default values are used)
        :param dict endpoint_url: where to send the request (if isn't set default value is used)
        :return: Response
        """
        endpoint_url = endpoint_url or self._endpoint_url

        url = endpoint_url + "/users/" + user_id + "/properties/" + property_name + "/decrease/" + value.__str__()
        headers = headers or self._default_headers(content_type=None)

        response = requests.post(url, headers=headers)

        return response

    def update_user_properties(self, user_id, user_properties, headers=None, endpoint_url=None):
        """
        Update a user's properties with values porovided in "user_properties" dictionary

        :param str user_id: identified user's ID
        :param dict user_properties: user properties to update with a new values
        :param dict headers: custom request headers (if isn't set default values are used)
        :param dict endpoint_url: where to send the request (if isn't set default value is used)
        :return: Response
        """
        endpoint_url = endpoint_url or self._endpoint_url

        url = endpoint_url + '/users/' + user_id + '/properties'
        headers = headers or self._default_headers()
        payload = user_properties

        response = requests.put(url, headers=headers, json=payload)

        return response

    def _default_headers(self, content_type=CONTENT_TYPE, token=None):
        """
        Get default headers for API request
        :param str content_type: HTTP request content type
        :param: str token: customer app ID
        :return: dictionary
        """
        headers = {
            self.HEADER_CLIENT_TYPE: self.CLIENT_TYPE,
            self.HEADER_TIMESTAMP: self._now(),
            self.HEADER_CUSTOMER_APP_ID: token or self._token
        }

        if content_type is not None:
            headers[self.HEADER_CONTENT_TYPE] = content_type

        return headers

    @staticmethod
    def _now():
        """
        :return: current timestamp in milliseconds
        """
        return int(time.time() * 1000)


class KilometerException(Exception):
    """
    Raised by EventsAPIClient
    """
    pass
