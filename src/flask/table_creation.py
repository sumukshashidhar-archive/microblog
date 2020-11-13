import sqlite3

MAKE_USERS_TABLE = """

CREATE TABLE users
(
    userid INT PRIMARY KEY,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);


"""


MAKE_POSTS_TABLE = """

CREATE TABLE posts
(
    postid INT PRIMARY KEY NOT NULL,
    userid INT NOT NULL, 
    title TEXT NOT NULL,
    time TEXT NOT NULL,
    content TEXT NOT NULL, 
    FOREIGN KEY(userid) REFERENCES users(userid)
    
);  
"""


conn = sqlite3.connect('./../../db/dbase.db')

conn.execute(MAKE_USERS_TABLE)
conn.execute(MAKE_POSTS_TABLE)
print("Connected")