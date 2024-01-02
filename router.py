from modules.events.controller import events_api


def configure_routes(app):
    app.register_blueprint(events_api, url_prefix="/api")
