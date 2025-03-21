                                        CREATE TABLE users
                                        ( id INTEGER PRIMARY KEY AUTOINCREMENT,
                                         name TEXT UNIQUE NOT NULL ,
                                         email TEXT NOT NULL UNIQUE,
                                         password TEXT NOT NULL,
                                         rule TEXT NOT NULL,
                                         photo TEXT NOT NULL);
