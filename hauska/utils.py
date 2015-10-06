import functools
from hauska import app

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
