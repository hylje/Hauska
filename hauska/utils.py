import functools
from hauska import app, get_db

def plaintext_response(f):
    """Annotates view f with a plain-text header"""
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        return app.make_response((
            f(*args, **kwargs),
            200,
            [("Content-Type", "text/plain")]
        ))
    return wrapper

def bibtexkey_exists(bibtexkey):
    db = get_db()
    for table in ['articles', 'books', 'booklets', 'conferences',
                  'inbooks', 'incollections', 'inproceedings',
                  'manuals', 'masterstheses', 'miscs', 'phdtheses',
                  'proceedings', 'techreports', 'unpublished',]:
        cur = db.execute("SELECT count(id) FROM %s WHERE bibtexkey=?" % table,
                         [bibtexkey])
        count, = cur.fetchone()
        if count > 0:
            return True
    return False
