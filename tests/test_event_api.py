import unittest
from flask import json
from main import app
from unittest.mock import patch


class EventsApiTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_post_event(self):
        # Create a sample valid event JSON
        valid_event = {
            "userid": 1,
            "verb": "buy",
            "noun": "nft",
            "timestamp": 1656613800,
            "properties": {"value": 4500, "currency": "INR"},
        }
        response = self.app.post(
            "/api/events",
            data=json.dumps(valid_event),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)

    def test_get_recent_events(self):
        response = self.app.get("/api/events")
        self.assertEqual(response.status_code, 200)

    def test_post_event_invalid_schema(self):
        # Create a sample invalid event JSON
        invalid_event = {
            "userid": "not-an-integer",
            "verb": 123,
            "noun": "nft",
            "timestamp": "invalid-timestamp",
            "properties": {"value": "not-a-number", "currency": 123},
        }
        response = self.app.post(
            "/api/events",
            data=json.dumps(invalid_event),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 400)


if __name__ == "__main__":
    unittest.main()
