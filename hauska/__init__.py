# -*- encoding: utf-8 -*-
import sqlite3

from flask import Flask


app = Flask("hauska")

app.config.from_object("hauska.default_settings")
# Tämä moduuli voi korvata oletusarvoja
app.config.from_envvar('HAUSKA_SETTINGS', silent=True)

# Tietokantatyökalut
_db = None

def db_connection():
    global _db

    if _db is None:
        _db = sqlite3.connect(app.config["DATABASE"])

    return _db

def init_db():
    """Alustaa (tyhjän) tietokannan SQL-tiedostosta pakettihakemistosta"""

    from contextlib import closing

    db = db_connection()

    with app.open_resource("schema.sql", mode="r") as f:
        db.cursor().executescript(f.read())

    db.commit()

# Kaikki view-moduulit pitää importtaa, jotta ne liitetään app-objektiin
import hauska.views
