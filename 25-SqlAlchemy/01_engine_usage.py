from sqlalchemy import create_engine, text
import os

# Remove existing DB for a clean run
if os.path.exists("some.db"):
    os.remove("some.db")

# Engine represents the DB + connection pool
engine = create_engine("sqlite:///some.db")

# Create tables and insert data inside a transaction
with engine.begin() as conn:
    conn.execute(text("""
        create table employee (
            emp_id integer primary key autoincrement,
            emp_name varchar
        )
    """))

    conn.execute(text("insert into employee(emp_name) values ('ed')"))
    conn.execute(text("insert into employee(emp_name) values ('jack')"))
    conn.execute(text("insert into employee(emp_name) values ('fred')"))

    conn.execute(text("""
        create table employee_of_month (
            emp_id integer primary key,
            emp_name varchar
        )
    """))

# Queries are executed via a Connection
with engine.connect() as conn:
    result = conn.execute(
        text("select emp_id, emp_name from employee where emp_id=:emp_id"),
        {"emp_id": 3}
    )

    row = result.fetchone()
    print(row)

# Result objects are iterable
with engine.connect() as conn:
    result = conn.execute(text("select * from employee"))
    for row in result:
        print(row)

# fetchall() returns a list of rows
with engine.connect() as conn:
    result = conn.execute(text("select * from employee"))
    print(result.fetchall())

# Explicit transaction control
with engine.begin() as conn:
    conn.execute(
        text("insert into employee_of_month (emp_name) values (:emp_name)"),
        {"emp_name": "wendy"}
    )
