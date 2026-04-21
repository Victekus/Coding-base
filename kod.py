import sqlite3
conn= sqlite3.connect("races.db")
cursor=conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    str-bonus INTEGER,
    agi-bonus INTEGER,
    char-bonus INTERGER
)
""")



stre=int(input("input strength:")) ; agi=int(input("input agility:")) ; char=int(input("input charisma:")); wis=int(input("input wisdom:")) ;  print("your statistics are:",stre,"str",agi,"agi",char,"char",wis,"wis")
tl=int(input("input tl:"))
health=(stre*agi*tl)//20 ; print(health,"hp")
mana=(char*wis*tl)//20 ;print(mana,"mp")
shield=health//3 ; print(shield,"sh")
barrier=mana//3 ; print(barrier,"br")
