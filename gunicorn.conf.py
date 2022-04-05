import os

bind = "0.0.0.0:5000"
wsgi_app = "app:app"
reload = os.getenv("HEALTH_TOOLS_DEBUG", "false").lower() == "true"
workers = os.getenv("HEALTH_TOOLS_GUNICORN_WORKERS", "1")
loglevel = os.getenv("HEALTH_TOOLS_GUNICORN_LOGLEVEL", "info")
