import sqlite3
import datetime


DB_NAME = "trading_history.db"


def connect():

    return sqlite3.connect(DB_NAME)



def create_table():

    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS signals (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        symbol TEXT,

        signal TEXT,

        confidence REAL,

        price REAL,

        result TEXT,

        time TEXT
    )
    """)

    conn.commit()
    conn.close()



def save_signal(
        symbol,
        signal,
        confidence,
        price
):

    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO signals
    (
    symbol,
    signal,
    confidence,
    price,
    time
    )

    VALUES (?,?,?,?,?)
    """,
    (
        symbol,
        signal,
        confidence,
        price,
        str(datetime.datetime.now())
    ))

    conn.commit()
    conn.close()



def get_history():

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM signals ORDER BY id DESC"
    )

    data = cur.fetchall()

    conn.close()

    return data
