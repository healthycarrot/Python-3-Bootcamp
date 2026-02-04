# SQL Expression Language (SQLAlchemy 2.x)

from sqlalchemy import (
    MetaData, Table, Column, String, Integer,
    create_engine, select, and_, or_
)

metadata = MetaData()

user_table = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String(50)),
    Column("fullname", String(50)),
)

engine = create_engine("sqlite://")
metadata.create_all(engine)

# Expressions
print(user_table.c.username == "ed")
print((user_table.c.username == "ed") | (user_table.c.username == "jack"))

print(
    and_(
        user_table.c.fullname == "ed jones",
        or_(
            user_table.c.username == "ed",
            user_table.c.username == "jack",
        ),
    )
)

print(user_table.c.id > 5)
print(user_table.c.fullname.is_(None))
print(user_table.c.fullname + " some name")
print(user_table.c.username.in_(["wendy", "mary", "ed"]))

# Insert data
with engine.begin() as conn:
    conn.execute(
        user_table.insert(),
        [
            {"username": "ed", "fullname": "Ed Jones"},
            {"username": "jack", "fullname": "Jack Burger"},
            {"username": "wendy", "fullname": "Wendy Weathersmith"},
        ],
    )

# Select
stmt = select(user_table.c.username, user_table.c.fullname).where(
    user_table.c.username == "ed"
)

with engine.connect() as conn:
    for row in conn.execute(stmt):
        print(row)

# Select all
with engine.connect() as conn:
    print(conn.execute(select(user_table)).fetchall())

# WHERE with OR
stmt = select(user_table).where(
    or_(
        user_table.c.username == "ed",
        user_table.c.username == "wendy",
    )
)

with engine.connect() as conn:
    print(conn.execute(stmt).fetchall())

# UPDATE
with engine.begin() as conn:
    conn.execute(
        user_table.update()
        .where(user_table.c.username == "jack")
        .values(fullname="Jack Brown")
    )

# UPDATE using expressions
with engine.begin() as conn:
    conn.execute(
        user_table.update().values(
            fullname=user_table.c.username + " " + user_table.c.fullname
        )
    )

with engine.connect() as conn:
    print(conn.execute(select(user_table)).fetchall())

# DELETE
with engine.begin() as conn:
    conn.execute(
        user_table.delete().where(user_table.c.username == "jack")
    )
