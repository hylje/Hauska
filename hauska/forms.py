from wtforms import Form, IntegerField, StringField, validators, ValidationError

from hauska.utils import bibtexkey_exists


class BaseForm(Form):
    bibtexkey = StringField(
        "Name this reference for citing",
        validators=[validators.input_required()]
    )

    def validate_bibtexkey(self, field):
        if bibtexkey_exists(field.data):
            raise ValidationError("This reference name already exists")

class ArticleForm(BaseForm):
    author = StringField("Author *", validators=[validators.input_required()])
    title = StringField("Title *", validators=[validators.input_required()])
    journal = StringField("Journal *", validators=[validators.input_required()])
    year = IntegerField("Year *", validators=[validators.input_required()])
    volume = IntegerField("Volume *", validators=[validators.input_required()])
    number = IntegerField("Number", validators=[validators.optional()])
    pages = StringField("Pages", validators=[validators.optional()])
    month = IntegerField("Month", validators=[validators.optional()])
    note = StringField("Note", validators=[validators.optional()])

#TODO book validaattorit
class BookForm(BaseForm): 
    author = StringField("Author")
    title = StringField("Title")
    editor = StringField("Editor")
    publisher = StringField("Publisher")
    year = IntegerField("Year")
    volume = IntegerField("Volume")
    number = IntegerField("Number")
    series = StringField("Series")
    address = StringField("Address")
    edition = StringField("Edition")
    month = IntegerField("Month")
    note = StringField("Note")

class BookletForm(BaseForm):
    author = StringField("Author", validators=[validators.optional()])
    title = StringField("Title *", validators=[validators.input_required()])
    howpublished = StringField("How published", validators=[validators.optional()])
    address = IntegerField("Address", validators=[validators.optional()])
    month = IntegerField("Month", validators=[validators.optional()])
    year = IntegerField("Year", validators=[validators.optional()])
    note = StringField("Note", validators=[validators.optional()])

class ConferenceForm(BaseForm):
    author = StringField("Author *", validators=[validators.input_required()])
    title = StringField("Title *", validators=[validators.input_required()])
    booktitle = StringField("Book title *", validators=[validators.input_required()])
    year = IntegerField("Year *", validators=[validators.input_required()])
    editor = StringField("Editor", validators=[validators.optional()])
    volume = IntegerField("Volume", validators=[validators.optional()])
    number = IntegerField("Number", validators=[validators.optional()])
    series = StringField("Series", validators=[validators.optional()])
    pages = StringField("Pages", validators=[validators.optional()])
    address = StringField("Address", validators=[validators.optional()])
    month = IntegerField("Month", validators=[validators.optional()])
    organization = StringField("Organization", validators=[validators.optional()])
    publisher = StringField("Publisher", validators=[validators.optional()])
    note = StringField("Note", validators=[validators.optional()])
