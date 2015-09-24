CREATE TABLE IF NOT EXISTS reference (
       author text not null,
       title text not null,
       booktitle text,
       journal text,
       volume int,
       number int,
       year int not null,
       pages text,
       publisher text not null
);
