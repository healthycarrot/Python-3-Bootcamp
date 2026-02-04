# Schema and MetaData
# -------------------
# MetaData is a registry that holds information about tables,
# columns, constraints, and relationships.

from sqlalchemy import (
    MetaData, Table, Column,
    Integer, String, Numeric, DateTime, Enum,
    ForeignKey, ForeignKeyConstraint, Unicode, UnicodeText,
    create_engine, inspect
)

# Create a MetaData container
metadata = MetaData()

# Define a table using Table + Column objects
user_table = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("fullname", String),
)

# Table.name gives the table name
user_table.name

# Table.c is a column collection (dict-like)
user_table.c.name

# Print all columns
print(user_table.c)

# Column metadata
user_table.c.name.name
user_table.c.name.type

# Primary key information
user_table.primary_key

# Generate a SQL SELECT statement
print(user_table.select())

# Create an in-memory SQLite database
engine = create_engine("sqlite:///some.db")

# Emit CREATE TABLE statements
metadata.create_all(engine)

# Demonstrating column types
fancy_table = Table(
    "fancy",
    metadata,
    Column("key", String(50), primary_key=True),
    Column("timestamp", DateTime),
    Column("amount", Numeric(10, 2)),
    Column("type", Enum("a", "b", "c", name="fancy_type_enum")),
)

# Create only this table
fancy_table.create(engine)

# Foreign key example
addresses_table = Table(
    "address",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email_address", String(100), nullable=False),
    Column("user_id", Integer, ForeignKey("user.id")),
)

addresses_table.create(engine)

# Composite foreign key example
story_table = Table(
    "story",
    metadata,
    Column("story_id", Integer, primary_key=True),
    Column("version_id", Integer, primary_key=True),
    Column("headline", Unicode(100), nullable=False),
    Column("body", UnicodeText),
)

published_table = Table(
    "published",
    metadata,
    Column("pub_id", Integer, primary_key=True),
    Column("pub_timestamp", DateTime, nullable=False),
    Column("story_id", Integer),
    Column("version_id", Integer),
    ForeignKeyConstraint(
        ["story_id", "version_id"],
        ["story.story_id", "story.version_id"],
    ),
)

# create_all() skips tables that already exist
metadata.create_all(engine)

# -------------------
# Reflection
# -------------------
# Reflection loads table definitions from an existing database

metadata2 = MetaData()

# SQLAlchemy 2.x reflection (autoload removed)
user_reflected = Table("user", metadata2, autoload_with=engine)

print(user_reflected.c)

# -------------------
# Inspector
# -------------------
# Inspector gives database-level metadata

inspector = inspect(engine)

# List all tables
inspector.get_table_names()

# Column information
inspector.get_columns("address")

# Foreign key information
inspector.get_foreign_keys("address")
