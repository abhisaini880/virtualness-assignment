# Virtualness Assignment

This application is designed to ingest a stream of user activity events and apply business rules to trigger operational alerts and actions.

## Assumptions

- Rules will be accessed from database and for the project returns hardcoded values.
- Rules conditions will be checked by the service and for project only returing true for one condition.
  - Returning True if verb is buy and rule_id is 1
- Printing the Notifications and not calling any actual service.

## Features

- REST API to ingest event data.
- Business rules engine to process events based on custom rules.
- Mock actions for demonstration (e.g., sending notifications, alerting operators).

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Flask
- SQLAlchemy
- jsonschema (for JSON validation)

### Installation

1. Clone the repository:
   ```
   git clone [repository link]
   ```
2. Navigate to the project directory:
   ```
   cd virtaulness-assignment
   ```
3. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```

### Running the Application

1. Start the Flask application:
   ```
   python main.py
   ```
2. The API will be available at `http://localhost:5000`.

## Project Structure

- `main.py`: The entry point of the Flask application.
- `/modules`: Contains the application modules.
- `/tests`: Unit tests for the application.
- `/services`: Contains the business logic.
- `requirements.txt`: List of Python package dependencies.

## API Endpoints

- POST `/events`: Endpoint to receive and process event data.
- GET `/events`: Endpoint to check 10 latest events data.

## Testing

Run the unit tests with the following command:

```
python -m unittest discover
```
