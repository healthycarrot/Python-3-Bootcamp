# Core Joins / Foreign Keys / Subqueries (SQLAlchemy 2.x)

from sqlalchemy import (
    MetaData, Table, Column, String, Integer,
    ForeignKey, select, create_engine, func
)

metadata = MetaData()

# User table
user_table = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String(50)),
    Column("fullname", String(50)),
)

# Address table
address_table = Table(
    "address",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer, ForeignKey("user.id"), nullable=False),
    Column("email_address", String(100), nullable=False),
)

# Create DB
engine = create_engine("sqlite://")
metadata.create_all(engine)

# Insert data (transaction required)
with engine.begin() as conn:
    conn.execute(
        user_table.insert(),
        [
            {"username": "ed", "fullname": "Ed Jones"},
            {"username": "jack", "fullname": "Jack Burger"},
            {"username": "wendy", "fullname": "Wendy Weathersmith"},
        ],
    )

    conn.execute(
        address_table.insert(),
        [
            {"user_id": 1, "email_address": "ed@ed.com"},
            {"user_id": 1, "email_address": "ed@gmail.com"},
            {"user_id": 2, "email_address": "jack@yahoo.com"},
            {"user_id": 3, "email_address": "wendy@gmail.com"},
        ],
    )

# Explicit join
join_obj = user_table.join(
    address_table, user_table.c.id == address_table.c.user_id
)
print(join_obj)

# FK-based join
print(user_table.join(address_table))

# SELECT from JOIN
stmt = (
    select(user_table, address_table)
    .select_from(user_table.join(address_table))
)

with engine.connect() as conn:
    print(conn.execute(stmt).fetchall())

# Subquery example
subq = (
    select(
        address_table.c.user_id,
        func.count(address_table.c.id).label("count"),
    )
    .group_by(address_table.c.user_id)
    .subquery()
)

stmt = (
    select(user_table.c.username, subq.c.count)
    .join(subq, user_table.c.id == subq.c.user_id)
    .order_by(user_table.c.username)
)

with engine.connect() as conn:
    print(conn.execute(stmt).fetchall())

# Scalar subquery
scalar_stmt = (
    select(func.count(address_table.c.id))
    .where(user_table.c.id == address_table.c.user_id)
    .scalar_subquery()
)

stmt = select(user_table.c.username, scalar_stmt)

with engine.connect() as conn:
    print(conn.execute(stmt).fetchall())
