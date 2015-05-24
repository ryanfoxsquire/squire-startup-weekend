from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
import os

from catseverywhere import app, db
#app.config.from_object(os.environ['APP_SETTINGS'])
APP_SETTINGS="config.DevelopmentConfig"  # "config.ProductionConfig"
app.config.from_object(APP_SETTINGS)

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()