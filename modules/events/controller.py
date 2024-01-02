from flask import Blueprint, request, jsonify
from services.eventProcessor import process_event
from .model import add_event, get_last_events
from jsonschema import validate, ValidationError

events_api = Blueprint("events_api", __name__)


# JSON schema for event validation
event_schema = {
    "type": "object",
    "properties": {
        "userid": {"type": "integer"},
        "verb": {"type": "string"},
        "noun": {"type": "string"},
        "timestamp": {"type": "number"},
        "properties": {
            "type": "object",
            "properties": {
                "mode": {"type": "string"},
                "bank": {"type": "string"},
                "merchantid": {"type": "integer"},
                "value": {"type": "number"},
                "currency": {"type": "string"},
            },
            "required": ["value", "currency"],
        },
    },
    "required": ["userid", "verb", "noun", "timestamp", "properties"],
}


@events_api.route("/events", methods=["POST"])
def receive_event():
    try:
        event = request.get_json()
        validate(instance=event, schema=event_schema)

        add_event(event)

        process_event(event)
        return jsonify({"status": "success"}), 200
    except ValidationError as ve:
        return (
            jsonify({"error": "Invalid JSON data", "message": str(ve)}),
            400,
        )
    except Exception as e:
        return (
            jsonify({"error": "Internal server error", "message": str(e)}),
            500,
        )


@events_api.route("/events", methods=["GET"])
def get_recent_events():
    try:
        events = get_last_events(10)  # Get the last 10 events
        return jsonify(events), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
