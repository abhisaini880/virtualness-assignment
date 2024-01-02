from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Database configuration
DATABASE_URI = "sqlite:///virtualness.db"

engine = create_engine(DATABASE_URI)
db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)

Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    # Import all modules here that might define models so that
    # they will be registered properly on the metadata. Otherwise
    # you will have to import them first before calling init_db()
    import modules.events.model as EventModel
    import modules.rules.model as RulesModel

    Base.metadata.create_all(bind=engine)


def close_db_session(exception=None):
    db_session.remove()
