from flask import Flask, request, jsonify
from db_connector import init_db, close_db_session
from router import configure_routes

app = Flask(__name__)

# Initialize the database (create tables, etc.)
init_db()

# Configure routes
configure_routes(app)


@app.teardown_appcontext
def shutdown_session(exception=None):
    close_db_session(exception)


if __name__ == "__main__":
    app.run(debug=True)
