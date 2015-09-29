# -*- encoding: utf-8 -*-

from hauska import app,get_db
from flask import render_template, request, redirect
from wtforms import Form, IntegerField, TextField

@app.route("/")
def hello():
    return render_template("index.html")
    
@app.route("/article/<id>")
def view_article(id):
    db=get_db()
    cur = db.execute('select * from articles where id = ?',
                    [id])
    ref = [dict(id=row[0],
                    bibtexkey=row[1],
                    author=row[2],
                    title=row[3],
                    journal=row[4],
                    year=row[5],
                    volume=row[6],
                    number=row[7],
                    pages=row[8],
                    month=row[9],
                    note=row[10]) for row in cur.fetchall()]
    return render_template("view_article.html", ref=ref[0])

@app.route("/refs")
def list_refs():
    db=get_db()
    cur = db.execute('select id, bibtexkey from articles ORDER BY id asc')
    articles = [dict(id=row[0], bibtexkey=row[1]) for row in cur.fetchall()]
    
    cur = db.execute('select id, bibtexkey from books ORDER BY id asc')
    books = [dict(id=row[0], bibtexkey=row[1]) for row in cur.fetchall()]
    
    cur = db.execute('select id, bibtexkey from booklets ORDER BY id asc')
    booklets = [dict(id=row[0], bibtexkey=row[1]) for row in cur.fetchall()]
    
    cur = db.execute('select id, bibtexkey from conferences ORDER BY id asc')
    conferences = [dict(id=row[0], bibtexkey=row[1]) for row in cur.fetchall()]
    
    cur = db.execute('select id, bibtexkey from inbooks ORDER BY id asc')
    inbooks = [dict(id=row[0], bibtexkey=row[1]) for row in cur.fetchall()]
    
    cur = db.execute('select id, bibtexkey from incollections ORDER BY id asc')
    incollections = [dict(id=row[0], bibtexkey=row[1]) for row in cur.fetchall()]
    
    cur = db.execute('select id, bibtexkey from inproceedings ORDER BY id asc')
    inproceedings = [dict(id=row[0], bibtexkey=row[1]) for row in cur.fetchall()]
    
    cur = db.execute('select id, bibtexkey from manuals ORDER BY id asc')
    manuals = [dict(id=row[0], bibtexkey=row[1]) for row in cur.fetchall()]
    
    cur = db.execute('select id, bibtexkey from masterstheses ORDER BY id asc')
    masterstheses = [dict(id=row[0], bibtexkey=row[1]) for row in cur.fetchall()]
    
    cur = db.execute('select id, bibtexkey from miscs ORDER BY id asc')
    miscs = [dict(id=row[0], bibtexkey=row[1]) for row in cur.fetchall()]
    
    cur = db.execute('select id, bibtexkey from phdtheses ORDER BY id asc')
    phdtheses = [dict(id=row[0], bibtexkey=row[1]) for row in cur.fetchall()]
    
    cur = db.execute('select id, bibtexkey from proceedings ORDER BY id asc')
    proceedings = [dict(id=row[0], bibtexkey=row[1]) for row in cur.fetchall()]
    
    cur = db.execute('select id, bibtexkey from techreports ORDER BY id asc')
    techreports = [dict(id=row[0], bibtexkey=row[1]) for row in cur.fetchall()]
    
    cur = db.execute('select id, bibtexkey from unpublished ORDER BY id asc')
    unpublished = [dict(id=row[0], bibtexkey=row[1]) for row in cur.fetchall()]
    #print refs
    return render_template("refs.html",articles=articles,books=books,booklets=booklets,conferences=conferences,inbooks=inbooks,incollections=incollections,inproceedings=inproceedings,manuals=manuals,masterstheses=masterstheses,miscs=miscs,phdtheses=phdtheses,proceedings=proceedings,techreports=techreports,unpublished=unpublished)

class ArticleForm(Form):
    bibtexkey = TextField("Anna viitteelle nimi:")

@app.route("/add")
def add_reference():
    #db=get_db()
    #form = ArticleForm(request.form)
    #if request.method == "POST" and form.validate():
    #    cur = db.cursor()
    #    cur.execute("INSERT INTO refs (bibtexkey) VALUES (?)", [form.bibtexkey.data])
    #    db.commit()
    #    return redirect("/add/%d" % cur.lastrowid)
    #return render_template("add_reference.html", form=form)
    return render_template("add_reference.html")

class ReferenceForm(Form):
    bibtexkey = TextField("Name this reference for citing")
    author = TextField("Author")
    title = TextField("Title")
    journal = TextField("Journal")
    year = IntegerField("Year")
    volume = IntegerField("Volume")
    number = IntegerField("Number")
    pages = TextField("Pages")
    month = IntegerField("Month")
    note = TextField("Note")

@app.route("/add/article", methods=["GET", "POST"])
def add_article():
    db=get_db()
    form = ReferenceForm(request.form)
    if request.method == "POST" and form.validate():
        db.execute("""INSERT INTO articles
        (bibtexkey, author, title, journal, year, volume, number, pages, month, note)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
                   [form.bibtexkey.data,
                   form.author.data,
                   form.title.data,
                   form.journal.data,
                   form.year.data,
                   form.volume.data,
                   form.number.data,
                   form.pages.data,
                   form.month.data,
                   form.note.data])
        db.commit()
        return redirect("/refs")
    return render_template("add_article.html", form=form)
