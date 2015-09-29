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
    cur = db.execute('select refid, bibtexkey from refs ORDER BY refid asc')
    refs = [dict(refid=row[0], bibtexkey=row[1]) for row in cur.fetchall()]
    print refs
    return render_template("refs.html",refs=refs)

class ArticleForm(Form):
    bibtexkey = TextField("Anna viitteelle nimi:")

@app.route("/add", methods=["GET", "POST"])
def add_article():
    db=get_db()
    form = ArticleForm(request.form)
    if request.method == "POST" and form.validate():
        cur = db.cursor()
        cur.execute("INSERT INTO refs (bibtexkey) VALUES (?)", [form.bibtexkey.data])
        db.commit()
        return redirect("/add/%d" % cur.lastrowid)
    return render_template("add_article.html", form=form)

class ReferenceForm(Form):
    author = TextField("Kirjoittaja")
    title = TextField("Otsikko")
    journal = TextField("Journal")
    year = IntegerField("Vuosi")
    volume = IntegerField("Vuosikerta")
    number = IntegerField("Numero")
    pages = TextField("Sivut")
    month = IntegerField("Kuukausi")
    note = TextField("Huomio")

@app.route("/add/<int:refs_id>", methods=["GET", "POST"])
def add_reference(refs_id):
    db=get_db()
    form = ReferenceForm(request.form)
    if request.method == "POST" and form.validate():
        db.execute("""INSERT INTO articles
        (refid, author, title, journal, year, volume, number, pages, month, note)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
                   [refs_id, form.author.data, form.title.data, form.journal.data,
                   form.year.data, form.volume.data, form.number.data,
                   form.pages.data, form.month.data, form.note.data])
        db.commit()
        return redirect("/refs")
    return render_template("add_reference.html", form=form)
