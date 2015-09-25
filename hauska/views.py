from hauska import app,get_db
from flask import render_template

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/refs")
def refs():
    db=get_db()
    cur = db.execute('select refid,title from refs ORDER BY refid asc')
    refs = [dict(refid=row[0], title=row[1]) for row in cur.fetchall()]
    return render_template("refs.html",refs=refs)
