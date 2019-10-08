import os
from app import create_app

application = create_app(os.getenv("FLASK_ENV") or "prod")
application.app_context().push()

if __name__ == "__main__":
    application.run()
