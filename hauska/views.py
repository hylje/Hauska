# -*- encoding: utf-8 -*-

from hauska import app,get_db
from flask import render_template, request, redirect
from wtforms import Form, IntegerField, TextField

@app.route("/")
def hello():
    return """<h1>Hello World!</h1>

    <p><a href="/refs">Selaa</a></p>
    <p><a href="/add">Lisää</a></p>
    """

@app.route("/refs")
def refs():
    db=get_db()
    cur = db.execute('select refid,title from refs ORDER BY refid asc')
    refs = [dict(refid=row[0], title=row[1]) for row in cur.fetchall()]
    print refs
    return render_template("refs.html",refs=refs)

class ArticleForm(Form):
    title = TextField("Otsikko")

@app.route("/add", methods=["GET", "POST"])
def add_article():
    db=get_db()
    form = ArticleForm(request.form)
    if request.method == "POST" and form.validate():
        cur = db.cursor()
        cur.execute("INSERT INTO refs (title) VALUES (?)", [form.title.data])
        db.commit()
        return redirect("/add/%d" % cur.lastrowid)
    return render_template("add_article.html", form=form)

class ReferenceForm(Form):
    author = TextField("Kirjoittaja")
    journal = TextField("Journal")
    year = IntegerField("Vuosi")
    volume = IntegerField("Vuosikerta")
    number = IntegerField("Numero")
    pages = TextField("Sivut")
    month = IntegerField("Kuukausi")
    note = TextField("Huomio")
    key = TextField("Key")

@app.route("/add/<int:refs_id>", methods=["GET", "POST"])
def add_reference(refs_id):
    db=get_db()
    form = ReferenceForm(request.form)
    if request.method == "POST" and form.validate():
        db.execute("""INSERT INTO articles
        (refid, author, journal, year, volume, number, pages, month, note, key)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
                   [refs_id, form.author.data, form.journal.data,
                   form.year.data, form.volume.data, form.number.data,
                   form.pages.data, form.month.data, form.note.data,
                    form.key.data])
        db.commit()
        return redirect("/refs")
    return render_template("add_reference.html", form=form)
