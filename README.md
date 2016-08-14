# kilometer-python

This is the official Kilometer.io Python library. This library allows for
server-side integration of Kilometer.


Installation
------------

The library can be installed using pip::

    pip install kilometer


Getting Started
---------------

Typical usage usually looks like this::


```python
import kilometer

kilometer = kilometer.EventsAPIClient('<<<APP_ID>>>')

# Transmit an event with certain properties
kilometer.add_event("<<<USER-ID>>>", "user_billed", {"amount": 100.00})

# Update a user's properties
kilometer.update_user_properties("<<<USER-ID>>>", {"status": "active", "name": "<<<JOHN WHITE>>>"})
```

You can use an instance of the Kilometer class for sending all of your events
and manage users.


Documentation
-------------
* <a href="https://kilometer.readme.io/" target="_blank">Full API Reference</a>
