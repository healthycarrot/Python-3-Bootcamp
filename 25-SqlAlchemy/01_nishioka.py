from sqlalchemy import create_engine, text
import os

if os.path.exists("some.db"):
    os.remove("some.db")

engine = create_engine("sqlite:///some.db")
with engine.begin() as conn:
    
    conn.execute(text("""
                      create table employee (
                        emp_id integer primary key autoincrement,
                        emp_name varchar
                        )"""))                      
    conn.execute(text("insert into employee(emp_name) values ('ed')"))
    conn.execute(text("insert into employee(emp_name) values ('jack')"))
    conn.execute(text("insert into employee(emp_name) values ('fred')"))
    conn.rollback()
    result = conn.execute(
        text("select * from employee where emp_id = :emp_id"),
        {"emp_id": 3},
    )
    print(result.fetchall())
    # row = result.first()
    # print(row)
    # print(row.emp_id)
    # print(row.emp_name)
    # print(row._mapping["emp_id"])