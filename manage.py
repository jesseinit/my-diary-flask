import os
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import app, db
from models import user_model, diary_model


manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command("db", MigrateCommand)


@manager.command
def run():
    app.run()


if __name__ == "__main__":
    manager.run()
