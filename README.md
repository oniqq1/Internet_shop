
# Zara remake
Hello there!!
<br>

It is a project for end of second semestr in course GoIteens
This project will get more updates with time
<br>
This shop-site can used for choosing clothing and education by 
analysis code
<br>



See soon for new info

Project worked [here](http://116.203.195.165:32322/) <- clickable

---

##  Photos

<img width="1000" alt="Знімок екрана 2025-12-31 001036" src="https://github.com/user-attachments/assets/3bd82c44-0826-40a3-91bd-06b3dfea80d0" />
<img width="1000" alt="Знімок екрана 2025-12-31 001027" src="https://github.com/user-attachments/assets/29dbc603-15da-4589-bf5f-1874f3eda9ba" />
<img width="1000" alt="Знімок екрана 2025-12-31 000959" src="https://github.com/user-attachments/assets/a21330dd-6da2-4936-b8c5-9ad218f5b75e" />


---
## Technologies
[bcrypt](https://pypi.org/project/bcrypt/) , [Flask](https://flask.palletsprojects.com/en/stable/) , [Materialize](https://materializecss.com/)


<br><br><br>


## Deployment

At the start you need to clone repository

```bash
  https://github.com/oniqq1/Internet_shop.git
```
After clonning you can continue instruction..
<br>
To deploy this project run first you need to install librarys

```bash
  pip install -r requirements.txt
```

#### flask has used for creating site and comunicate with customers

#### bcrypt has used for hash passwords in database
<br>
After that start app

```bash
  python3 main.py
```

or

```bash
  python main.py
```

All done , go to link and it works

For support contact us...

<br><br><br>




## Usage / Examples

There will be lot of code-examples

You can understand how it works :

```bash
import sqlite3
import logging
from flask import Flask ,session
from secret import key
from connection import create_table
```

There are imports to crate app , db etc. 
<br><br>
*secret* it is created by you file to like this :

```bash
key = "YOUR_KEY"
```

*create_table* it is func. to create table if not exist looks like :

```bash
def create_table():
    connection = sqlite3.connect("database.db")
    with open("schema.sql") as f:
        connection.executescript(f.read())
```

We are connecting to db and opening db by *schema*

I think something you understood

So it is end
<br><br><br>
## Authors / Support

To take feedback or get support you can connect with one of this persons



- [@oniqq1](https://github.com/oniqq1)  - backend  - [telegram](https://t.me/oinqqq)

- [@chrczq](https://github.com/chrczq)  - frontend - [telegram](https://t.me/chrczq)

You can take feedback for us , only you need to contact with us !!!

Special thanks to [Kostya](https://github.com/KostyaTeacher)
<br><br>
