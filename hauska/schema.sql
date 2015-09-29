CREATE TABLE IF NOT EXISTS refs (
    refid integer primary key autoincrement,
    bibtexkey text not null
);
CREATE TABLE IF NOT EXISTS articles (
    articleid integer primary key autoincrement,
    refid integer references refs(refid),
    author text not null,
    title text not null,
    journal text not null,
    year int not null,
    volume int,
    number int,
    pages text,
    month int,
    note text
);
CREATE TABLE IF NOT EXISTS books (
    bookid integer primary key autoincrement,
    refid integer references refs(refid),
    title text not null,
    author text, -- joko author tai editor pitää olla
    editor text, -- tarkistus softan puolella?
    publisher text not null,
    year int not null,
    volume int,
    number int,
    series text,
    address text,
    edition text,
    month int,
    note text
);
CREATE TABLE IF NOT EXISTS booklets (
    bookletid integer primary key autoincrement,
    refid integer references refs(refid),
    title text not null,
    author text,
    howpublished text,
    address text,
    month int,
    year int,
    note text
);
CREATE TABLE IF NOT EXISTS conferences (
    conferenceid integer primary key autoincrement,
    refid integer references refs(refid),
    author text not null,
    title text not null,
    booktitle text not null,
    year int not null,
    editor text,
    volume int,
    number int,
    series text,
    pages text,
    address text,
    month int,
    organization text,
    publisher text,
    note text
);
CREATE TABLE IF NOT EXISTS inbooks (
    inbookid integer primary key autoincrement,
    refid integer references refs(refid),
    author text, -- joko author tai editor pitää olla
    editor text, -- 
    title text not null,
    chapter text, -- chapters ja/tai pages pitää olla
    pages text, -- 
    publisher text not null,
    year int not null,
    volume int,
    number int,
    series text,
    type text,
    address text,
    edition text,
    month int,
    note text
);
CREATE TABLE IF NOT EXISTS incollections (
    incollectionid integer primary key autoincrement,
    refid integer references refs(refid),
    author text not null,
    title text not null,
    booktitle text not null,
    publisher text not null,
    year int not null,
    editor text,
    volume int,
    number int,
    series text,
    type text,
    chapter text,
    pages text,
    address text,
    edition text,
    month int
);
CREATE TABLE IF NOT EXISTS inproceedings (
    inproceedingid integer primary key autoincrement,
    refid integer references refs(refid),
    author text not null,
    title text not null,
    booktitle text not null,
    year int not null,
    editor text,
    volume int,
    number int,
    series text,
    pages text,
    address text,
    month int,
    organization text,
    publisher text,
    note text
);
CREATE TABLE IF NOT EXISTS manuals (
    manualid integer primary key autoincrement,
    refid integer references refs(refid),
    title text not null,
    author text,
    organization text,
    address text,
    edition text,
    month int,
    year int,
    note text
);
CREATE TABLE IF NOT EXISTS masterstheses ( --theses oikea monikko
    mastersthesisid integer primary key autoincrement,
    refid integer references refs(refid),
    author text not null,
    title text not null,
    school text not null,
    year int not null,
    type text,
    address text,
    month int,
    note text
);
CREATE TABLE IF NOT EXISTS miscs (
    miscid integer primary key autoincrement,
    refid integer references refs(refid),
    author text,
    title text,
    howpublished text,
    month int,
    year int,
    note text
);
CREATE TABLE IF NOT EXISTS phdtheses (
    mastersthesisid integer primary key autoincrement,
    refid integer references refs(refid),
    author text not null,
    title text not null,
    school text not null,
    year int not null,
    type text,
    address text,
    month int,
    note text
);
CREATE TABLE IF NOT EXISTS proceedings (
    proceedingid integer primary key autoincrement,
    refid integer references refs(refid),
    title text not null,
    year int not null,
    editor text,
    volume int,
    number int,
    series text,
    address text,
    month int,
    organization text,
    publisher text,
    note text
);
CREATE TABLE IF NOT EXISTS techreports (
    techreportid integer primary key autoincrement,
    refid integer references refs(refid),
    author text not null,
    title text not null,
    institution text not null,
    year int not null,
    type text,
    number int,
    address text,
    month int,
    note text
);
CREATE TABLE IF NOT EXISTS unpublished (
    unpublishedid integer primary key autoincrement,
    refid integer references refs(refid),
    author text not null,
    title text not null,
    note text not null,
    month int,
    year int
);


































