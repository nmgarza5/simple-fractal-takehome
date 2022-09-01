
from flask.cli import AppGroup
from .model_generate import seed_companies, seed_records, undo_records, undo_companies
from .users import seed_users, undo_users

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    seed_users()
    seed_records()
    seed_companies()
    # Add other seed functions here


# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_users()
    undo_records()
    undo_companies()
    # Add other undo functions here
