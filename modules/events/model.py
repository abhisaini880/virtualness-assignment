from sqlalchemy import (
    Column,
    Integer,
    String,
    JSON,
)
from db_connector import Base, db_session


class Event(Base):
    __tablename__ = "events"

    eventid = Column(Integer, primary_key=True)
    userid = Column(Integer)
    verb = Column(String)
    noun = Column(String)
    timestamp = Column(Integer)
    properties = Column(JSON)

    def __repr__(self):
        return f"<Event(userid='{self.userid}', verb='{self.verb}', noun='{self.noun}')>"

    def to_dict(self):
        return {
            "eventid": self.eventid,
            "userid": self.userid,
            "verb": self.verb,
            "noun": self.noun,
            "timestamp": self.timestamp,
            "properties": self.properties,
        }


def add_event(event_data):
    new_event = Event(**event_data)
    db_session.add(new_event)
    db_session.commit()


def get_last_events(limit):
    events = (
        db_session.query(Event)
        .order_by(Event.timestamp.desc())
        .limit(limit)
        .all()
    )
    return [event.to_dict() for event in events]
