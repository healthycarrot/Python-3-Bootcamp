from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///some.db")

# Begin the transaction to create table and insert data
# commits automatically at the end of the block
# with engine.begin() as conn:
#     conn.execute(text("""
#         CREATE TABLE department (
#             id INTEGER PRIMARY KEY,
#             name TEXT
#         )
#     """))

# with engine.begin() as conn:
#     conn.execute(text("INSERT INTO department (name) VALUES ('IT')"))
#     conn.execute(text("INSERT INTO department (name) VALUES ('HR')"))



# Demonstrate explicit transaction control
# It will not commit the insert
with engine.connect() as conn:
    # trans = conn.begin()
    conn.execute(text("INSERT INTO department (name) VALUES ('Training')"))
    # trans.commit()
    # trans.rollback()

with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM department"))
    print(result.fetchall())