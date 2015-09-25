CREATE TABLE IF NOT EXISTS refs (
    refid integer primary key autoincrement,
    title text not null
);
CREATE TABLE IF NOT EXISTS articles (
    articleid integer primary key autoincrement,
    refid integer references refs(refid),
    author text not null,
    journal text not null,
    year int not null,
    volume int not null,
    number int,
    pages text,
    month int,
    note text,
    key text
);
