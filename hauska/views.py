# -*- encoding: utf-8 -*-


from flask import render_template, request, redirect


from hauska import app, get_db
from hauska.utils import plaintext_response
from hauska import forms


@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/article/<id>")
def view_article(id):
    db = get_db()
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


@app.route("/book/<id>")
def view_book(id):
    db = get_db()
    cur = db.execute('select * from books where id = ?',
                     [id])
    ref = [dict(id=row[0],
                bibtexkey=row[1],
                title=row[2],
                author=row[3],
                editor=row[4],
                publisher=row[5],
                year=row[6],
                volume=row[7],
                number=row[8],
                series=row[9],
                address=row[10],
                edition=row[11],
                month=row[12],
                note=row[13]) for row in cur.fetchall()]
    return render_template("view_book.html", ref=ref[0])


@app.route("/booklet/<id>")
def view_booklet(id):
    db = get_db()
    cur = db.execute('select * from booklets where id = ?',
                     [id])
    ref = [dict(id=row[0],
                bibtexkey=row[1],
                title=row[2],
                author=row[3],
                howpublished=row[4],
                address=row[5],
                month=row[6],
                year=row[7],
                note=row[8]) for row in cur.fetchall()]
    return render_template("view_booklet.html", ref=ref[0])


@app.route("/conference/<id>")
def view_conference(id):
    db = get_db()
    cur = db.execute('select * from conferences where id = ?',
                     [id])
    ref = [dict(id=row[0],
                bibtexkey=row[1],
                author=row[2],
                title=row[3],
                booktitle=row[4],
                year=row[5],
                editor=row[6],
                volume=row[7],
                number=row[8],
                series=row[9],
                pages=row[10],
                address=row[11],
                month=row[12],
                organization=row[13],
                publisher=row[14],
                note=row[15]) for row in cur.fetchall()]
    return render_template("view_conference.html", ref=ref[0])


@app.route("/inproceedings/<id>")
def view_inproceedings(id):
    db = get_db()
    cur = db.execute('select * from inproceedings where id = ?',
                     [id])
    ref = [dict(id=row[0],
                bibtexkey=row[1],
                author=row[2],
                title=row[3],
                booktitle=row[4],
                year=row[5],
                editor=row[6],
                volume=row[7],
                number=row[8],
                series=row[9],
                pages=row[10],
                address=row[11],
                month=row[12],
                organization=row[13],
                publisher=row[14],
                note=row[15]) for row in cur.fetchall()]
    return render_template("view_inproceedings.html", ref=ref[0])


@app.route("/refs")
def list_refs():
    db = get_db()
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
    # print refs

    no_entries = not any([
        articles, books, booklets, conferences, inbooks,
        incollections, inproceedings, manuals, masterstheses,
        miscs, phdtheses, proceedings, techreports, unpublished
    ])

    return render_template("refs.html",
                           articles=articles,
                           books=books,
                           booklets=booklets,
                           conferences=conferences,
                           inbooks=inbooks,
                           incollections=incollections,
                           inproceedings=inproceedings,
                           manuals=manuals,
                           masterstheses=masterstheses,
                           miscs=miscs, phdtheses=phdtheses,
                           proceedings=proceedings,
                           techreports=techreports,
                           unpublished=unpublished,
                           no_entries=no_entries)


# class ArticleForm(Form):
#    bibtexkey = TextField("Anna viitteelle nimi:")

@app.route("/add")
def add_reference():
    # db=get_db()
    # form = ArticleForm(request.form)
    # if request.method == "POST" and form.validate():
    #    cur = db.cursor()
    #    cur.execute("INSERT INTO refs (bibtexkey) VALUES (?)", [form.bibtexkey.data])
    #    db.commit()
    #    return redirect("/add/%d" % cur.lastrowid)
    # return render_template("add_reference.html", form=form)
    return render_template("add_reference.html")


@app.route("/add/article", methods=["GET", "POST"])
def add_article():
    db = get_db()
    form = forms.ArticleForm(request.form)
    if request.method == "POST" and form.validate():
        # Lisätään null jos valinnainen kenttä tyhjä
        number = 'NULL'
        if form.number.data is not None:
            number = form.number.data
        pages = 'NULL'
        if form.pages.data is not None:
            pages = form.pages.data
        month = 'NULL'
        if form.month.data is not None:
            month = form.month.data
        note = 'NULL'
        if form.note.data is not None:
            note = form.note.data
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
                    number,
                    pages,
                    month,
                    note])
        db.commit()
        return redirect("/refs")
    return render_template("add_article.html", form=form)

@app.route("/add/book", methods=["GET", "POST"])
def add_book():
    db = get_db()
    form = forms.BookForm(request.form)
    if request.method == "POST" and form.validate():
        db.execute("""INSERT INTO books
        (bibtexkey, author, title, editor, publisher, year, volume, number, series, address, edition, month, note)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
                   [form.bibtexkey.data,
                    form.author.data,
                    form.title.data,
                    form.editor.data,
                    form.publisher.data,
                    form.year.data,
                    form.volume.data,
                    form.number.data,
                    form.series.data,
                    form.address.data,
                    form.edition.data,
                    form.month.data,
                    form.note.data])
        db.commit()
        return redirect("/refs")
    return render_template("add_book.html", form=form)



@app.route("/add/booklet", methods=["GET", "POST"])
def add_booklet():
    db = get_db()
    form = forms.BookletForm(request.form)
    if request.method == "POST" and form.validate():
        db.execute("""INSERT INTO booklets
        (bibtexkey, author, title, howpublished, address, month, year, note)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
                   [form.bibtexkey.data,
                    form.author.data,
                    form.title.data,
                    form.howpublished.data,
                    form.address.data,
                    form.month.data,
                    form.year.data,
                    form.note.data])
        db.commit()
        return redirect("/refs")
    return render_template("add_booklet.html", form=form)

@app.route("/add/conference", methods=["GET", "POST"])
def add_conference():
    db = get_db()
    form = forms.ConferenceForm(request.form)
    if request.method == "POST" and form.validate():
        db.execute("""INSERT INTO conferences
        (bibtexkey, author, title, booktitle, year, editor, volume, number, series, pages, address, month, organization, publisher, note)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
                   [form.bibtexkey.data,
                    form.author.data,
                    form.title.data,
                    form.booktitle.data,
                    form.year.data,
                    form.editor.data,
                    form.volume.data,
                    form.number.data,
                    form.series.data,
                    form.pages.data,
                    form.address.data,
                    form.month.data,
                    form.organization.data,
                    form.publisher.data,
                    form.note.data])
        db.commit()
        return redirect("/refs")
    return render_template("add_conference.html", form=form)

@app.route("/add/inproceedings", methods=["GET", "POST"])
def add_inproceedings():
    db = get_db()
    form = ConferenceForm(request.form)
    if request.method == "POST" and form.validate():
        db.execute("""INSERT INTO inproceedings
        (bibtexkey, author, title, booktitle, year, editor, volume, number, series, pages, address, month, organization, publisher, note)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
                   [form.bibtexkey.data,
                    form.author.data,
                    form.title.data,
                    form.booktitle.data,
                    form.year.data,
                    form.editor.data,
                    form.volume.data,
                    form.number.data,
                    form.series.data,
                    form.pages.data,
                    form.address.data,
                    form.month.data,
                    form.organization.data,
                    form.publisher.data,
                    form.note.data])
        db.commit()
        return redirect("/refs")
    return render_template("add_inproceedings.html", form=form)


def article_to_bib(ref):
    bibstring = "@article{" + ref['bibtexkey'] + ",\n"
    bibstring += "\t" + "author = \"" + ref['author'] + "\",\n"
    bibstring += "\t" + "title = \"" + ref['title'] + "\",\n"
    bibstring += "\t" + "journal = \"" + ref['journal'] + "\",\n"
    bibstring += "\t" + "year = \"" + str(ref['year']) + "\",\n"
    if ref['volume']:
        bibstring += "\t" + "volume = \"" + str(ref['volume']) + "\",\n"
    if ref['number']:
        bibstring += "\t" + "number = \"" + str(ref['number']) + "\",\n"
    if ref['pages']:
        bibstring += "\t" + "pages = \"" + ref['pages'] + "\",\n"
    if ref['month']:
        bibstring += "\t" + "month = \"" + str(ref['month']) + "\",\n"
    if ref['note']:
        bibstring += "\t" + "note = \"" + ref['note'] + "\",\n"
    bibstring += "}\n"
    return bibstring


@app.route("/article/<id>/bib")
@plaintext_response
def view_article_bib(id):
    db = get_db()
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
    return article_to_bib(ref[0])


def book_to_bib(ref):
    bibstring = "@book{" + ref['bibtexkey'] + ",\n"
    bibstring += "\t" + "title = \"" + ref['title'] + "\",\n"
    if ref['author']:
        bibstring += "\t" + "author = \"" + ref['author'] + "\",\n"
    if ref['editor']:
        bibstring += "\t" + "editor = \"" + ref['editor'] + "\",\n"
    if not ref['author']:
        if not ref['editor']:
            bibstring += "\t" + "author = \"missing author or editor\",\n"
    bibstring += "\t" + "publisher = \"" + ref['publisher'] + "\",\n"
    bibstring += "\t" + "year = \"" + str(ref['year']) + "\",\n"
    if ref['volume']:
        bibstring += "\t" + "volume = \"" + str(ref['volume']) + "\",\n"
    if ref['number']:
        bibstring += "\t" + "number = \"" + str(ref['number']) + "\",\n"
    if ref['series']:
        bibstring += "\t" + "series = \"" + ref['series'] + "\",\n"
    if ref['address']:
        bibstring += "\t" + "address = \"" + ref['address'] + "\",\n"
    if ref['edition']:
        bibstring += "\t" + "edition = \"" + ref['edition'] + "\",\n"
    if ref['month']:
        bibstring += "\t" + "month = \"" + str(ref['month']) + "\",\n"
    if ref['note']:
        bibstring += "\t" + "note = \"" + ref['note'] + "\",\n"
    bibstring += "}\n"
    return bibstring


@app.route("/book/<id>/bib")
@plaintext_response
def view_book_bib(id):
    db = get_db()
    cur = db.execute('select * from books where id = ?',
                     [id])
    ref = [dict(id=row[0],
                bibtexkey=row[1],
                title=row[2],
                author=row[3],
                editor=row[4],
                publisher=row[5],
                year=row[6],
                volume=row[7],
                number=row[8],
                series=row[9],
                address=row[10],
                edition=row[11],
                month=row[12],
                note=row[13]) for row in cur.fetchall()]
    return book_to_bib(ref[0])


def booklet_to_bib(ref):
    bibstring = "@booklet{" + ref['bibtexkey'] + ",\n"
    bibstring += "\t" + "title = \"" + ref['title'] + "\",\n"
    if ref['author']:
        bibstring += "\t" + "author = \"" + ref['author'] + "\",\n"
    if ref['howpublished']:
        bibstring += "\t" + "howpublished = \"" + ref['howpublished'] + "\",\n"
    if ref['address']:
        bibstring += "\t" + "address = \"" + ref['address'] + "\",\n"
    if ref['month']:
        bibstring += "\t" + "month = \"" + str(ref['month']) + "\",\n"
    if ref['year']:
        bibstring += "\t" + "year = \"" + str(ref['year']) + "\",\n"
    if ref['note']:
        bibstring += "\t" + "note = \"" + ref['note'] + "\",\n"
    bibstring += "}\n"
    return bibstring


@app.route("/booklet/<id>/bib")
@plaintext_response
def view_booklet_bib(id):
    db = get_db()
    cur = db.execute('select * from booklets where id = ?',
                     [id])
    ref = [dict(id=row[0],
                bibtexkey=row[1],
                title=row[2],
                author=row[3],
                howpublished=row[4],
                address=row[5],
                month=row[6],
                year=row[7],
                note=row[8]) for row in cur.fetchall()]
    return booklet_to_bib(ref[0])


def conference_to_bib(ref):
    bibstring = "@conference{" + ref['bibtexkey'] + ",\n"
    bibstring += "\t" + "author = \"" + ref['author'] + "\",\n"
    bibstring += "\t" + "title = \"" + ref['title'] + "\",\n"
    bibstring += "\t" + "booktitle = \"" + ref['booktitle'] + "\",\n"
    bibstring += "\t" + "year = \"" + str(ref['year']) + "\",\n"
    if ref['editor']:
        bibstring += "\t" + "editor = \"" + ref['editor'] + "\",\n"
    if ref['volume']:
        bibstring += "\t" + "volume = \"" + str(ref['volume']) + "\",\n"
    if ref['number']:
        bibstring += "\t" + "number = \"" + str(ref['number']) + "\",\n"
    if ref['series']:
        bibstring += "\t" + "series = \"" + ref['series'] + "\",\n"
    if ref['pages']:
        bibstring += "\t" + "pages = \"" + ref['pages'] + "\",\n"
    if ref['address']:
        bibstring += "\t" + "address = \"" + ref['address'] + "\",\n"
    if ref['month']:
        bibstring += "\t" + "month = \"" + str(ref['month']) + "\",\n"
    if ref['organization']:
        bibstring += "\t" + "organization = \"" + ref['organization'] + "\",\n"
    if ref['publisher']:
        bibstring += "\t" + "publisher = \"" + ref['publisher'] + "\",\n"
    if ref['note']:
        bibstring += "\t" + "note = \"" + ref['note'] + "\",\n"
    bibstring += "}\n"
    return bibstring


@app.route("/conference/<id>/bib")
@plaintext_response
def view_conference_bib(id):
    db = get_db()
    cur = db.execute('select * from conferences where id = ?',
                     [id])
    ref = [dict(id=row[0],
                bibtexkey=row[1],
                author=row[2],
                title=row[3],
                booktitle=row[4],
                year=row[5],
                editor=row[6],
                volume=row[7],
                number=row[8],
                series=row[9],
                pages=row[10],
                address=row[11],
                month=row[12],
                organization=row[13],
                publisher=row[14],
                note=row[15]) for row in cur.fetchall()]
    return conference_to_bib(ref[0])


def inproceedings_to_bib(ref):
    bibstring = "@inproceedings{" + ref['bibtexkey'] + ",\n"
    bibstring += "\t" + "author = \"" + ref['author'] + "\",\n"
    bibstring += "\t" + "title = \"" + ref['title'] + "\",\n"
    bibstring += "\t" + "booktitle = \"" + ref['booktitle'] + "\",\n"
    bibstring += "\t" + "year = \"" + str(ref['year']) + "\",\n"
    if ref['editor']:
        bibstring += "\t" + "editor = \"" + ref['editor'] + "\",\n"
    if ref['volume']:
        bibstring += "\t" + "volume = \"" + str(ref['volume']) + "\",\n"
    if ref['number']:
        bibstring += "\t" + "number = \"" + str(ref['number']) + "\",\n"
    if ref['series']:
        bibstring += "\t" + "series = \"" + ref['series'] + "\",\n"
    if ref['pages']:
        bibstring += "\t" + "pages = \"" + ref['pages'] + "\",\n"
    if ref['address']:
        bibstring += "\t" + "address = \"" + ref['address'] + "\",\n"
    if ref['month']:
        bibstring += "\t" + "month = \"" + str(ref['month']) + "\",\n"
    if ref['organization']:
        bibstring += "\t" + "organization = \"" + ref['organization'] + "\",\n"
    if ref['publisher']:
        bibstring += "\t" + "publisher = \"" + ref['publisher'] + "\",\n"
    if ref['note']:
        bibstring += "\t" + "note = \"" + ref['note'] + "\",\n"
    bibstring += "}\n"
    return bibstring


@app.route("/inproceedings/<id>/bib")
@plaintext_response
def view_inproceedings_bib(id):
    db = get_db()
    cur = db.execute('select * from inproceedings where id = ?',
                     [id])
    ref = [dict(id=row[0],
                bibtexkey=row[1],
                author=row[2],
                title=row[3],
                booktitle=row[4],
                year=row[5],
                editor=row[6],
                volume=row[7],
                number=row[8],
                series=row[9],
                pages=row[10],
                address=row[11],
                month=row[12],
                organization=row[13],
                publisher=row[14],
                note=row[15]) for row in cur.fetchall()]
    return inproceedings_to_bib(ref[0])


@app.route("/refs/bib")
@plaintext_response
def list_refs_bib():
    bibtex_compilation = []
    db = get_db()
    cur = db.execute('select * from articles ORDER BY id asc')
    articles = [dict(id=row[0],
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

    bibtex_compilation.extend(article_to_bib(ref) for ref in articles)

    cur = db.execute('select * from books ORDER BY id asc')
    books = [dict(id=row[0],
                  bibtexkey=row[1],
                  title=row[2],
                  author=row[3],
                  editor=row[4],
                  publisher=row[5],
                  year=row[6],
                  volume=row[7],
                  number=row[8],
                  series=row[9],
                  address=row[10],
                  edition=row[11],
                  month=row[12],
                  note=row[13]) for row in cur.fetchall()]
    bibtex_compilation.extend(book_to_bib(ref) for ref in books)

    cur = db.execute('select * from booklets ORDER BY id asc')
    booklets = [dict(id=row[0],
                     bibtexkey=row[1],
                     title=row[2],
                     author=row[3],
                     howpublished=row[4],
                     address=row[5],
                     month=row[6],
                     year=row[7],
                     note=row[8]) for row in cur.fetchall()]

    bibtex_compilation.extend(booklet_to_bib(ref) for ref in booklets)

    cur = db.execute('select * from conferences ORDER BY id asc')
    conferences = [dict(id=row[0],
                        bibtexkey=row[1],
                        author=row[2],
                        title=row[3],
                        booktitle=row[4],
                        year=row[5],
                        editor=row[6],
                        volume=row[7],
                        number=row[8],
                        series=row[9],
                        pages=row[10],
                        address=row[11],
                        month=row[12],
                        organization=row[13],
                        publisher=row[14],
                        note=row[15]) for row in cur.fetchall()]

    bibtex_compilation.extend(conference_to_bib(ref) for ref in conferences)

    cur = db.execute('select * from inbooks ORDER BY id asc')
    inbooks = [dict(id=row[0], bibtexkey=row[1]) for row in cur.fetchall()]

    # bibtex_compilation.extend(inbook_to_bib(ref) for ref in inbooks)

    cur = db.execute('select * from incollections ORDER BY id asc')
    incollections = [dict(id=row[0], bibtexkey=row[1]) for row in cur.fetchall()]
    # bibtex_compilation.extend(incollection_to_bib(ref) for ref in incollections)

    cur = db.execute('select * from inproceedings ORDER BY id asc')
    inproceedings = [dict(id=row[0],
                          bibtexkey=row[1],
                          author=row[2],
                          title=row[3],
                          booktitle=row[4],
                          year=row[5],
                          editor=row[6],
                          volume=row[7],
                          number=row[8],
                          series=row[9],
                          pages=row[10],
                          address=row[11],
                          month=row[12],
                          organization=row[13],
                          publisher=row[14],
                          note=row[15]) for row in cur.fetchall()]

    bibtex_compilation.extend(inproceedings_to_bib(ref) for ref in inproceedings)

    cur = db.execute('select * from manuals ORDER BY id asc')
    manuals = [dict(id=row[0], bibtexkey=row[1]) for row in cur.fetchall()]
    # bibtex_compilation.extend(manual_to_bib(ref) for ref in manuals)

    cur = db.execute('select * from masterstheses ORDER BY id asc')
    masterstheses = [dict(id=row[0], bibtexkey=row[1]) for row in cur.fetchall()]
    # bibtex_compilation.extend(masterthesis_to_bib(ref) for ref in mastertheses)

    cur = db.execute('select * from miscs ORDER BY id asc')
    miscs = [dict(id=row[0], bibtexkey=row[1]) for row in cur.fetchall()]
    # bibtex_compilation.extend(misc_to_bib(ref) for ref in miscs)

    cur = db.execute('select * from phdtheses ORDER BY id asc')
    phdtheses = [dict(id=row[0], bibtexkey=row[1]) for row in cur.fetchall()]
    # bibtex_compilation.extend(phdthesis_to_bib(ref) for ref in phdtheses)

    cur = db.execute('select * from proceedings ORDER BY id asc')
    proceedings = [dict(id=row[0], bibtexkey=row[1]) for row in cur.fetchall()]
    # bibtex_compilation.extend(proceeding_to_bib(ref) for ref in proceedings)

    cur = db.execute('select * from techreports ORDER BY id asc')
    techreports = [dict(id=row[0], bibtexkey=row[1]) for row in cur.fetchall()]
    # bibtex_compilation.extend(techreport_to_bib(ref) for ref in techreports)

    cur = db.execute('select * from unpublished ORDER BY id asc')
    unpublished = [dict(id=row[0], bibtexkey=row[1]) for row in cur.fetchall()]
    # bibtex_compilation.extend(unpublished_to_bib(ref) for ref in unpublished)

    return "\n".join(bibtex_compilation)


def handle_special_characters_in_bibtex_value(value):
    conversion = {'ä': '{\\\"a}',
                  'Ä': '{\\\"A}',
                  'ö': '{\\\"o}',
                  'Ö': '{\\\"O}',
                  'å': '{\\aa}',
                  'Å': '{\\AA}'}
    for c in conversion:
        value = value.replace(c, conversion[c])
    return value
