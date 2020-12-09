import os
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from .app import db, create_app
# from .models import user_model, diary_model

app = create_app(os.getenv("FLASK_ENV") or "dev")
app.app_context().push()

manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command("db", MigrateCommand)


@manager.command
def run():
    app.run(debug=False)


if __name__ == "__main__":
    manager.run()
