# -*- encoding: utf-8 -*-
from contextlib import closing
import sqlite3
from hauska import app

#NOTE(markus): en keksinyt muuta keinoa initialisoida tietokantaa joten tein tälläisen
#tämä init_db oli kopioitu http://flask.pocoo.org/docs/0.10/tutorial/dbinit/ sivulta

def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

init_db()