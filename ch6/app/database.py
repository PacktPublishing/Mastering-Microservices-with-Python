from sqlalchemy import Table, Column, Integer, String, ForeignKey, CHAR, Interval
from sqlalchemy.dialects.postgresql import TIMESTAMP, JSONB
import sqlalchemy as sa

METADATA = sa.MetaData()

"""
CREATE TABLE videos (
   id      int PRIMARY KEY,
   title       string(40) NOT NULL,
   owner_id         string(5) NOT NULL,
   date_created   date,
   tags        string(30),
   len        interval hour to minute
);"""

videos = Table(
    'videos', METADATA,
    Column('id', Integer, primary_key=True),
    Column('title', String(40)),
    Column('owner_id', String(5)),
    Column('date_created', TIMESTAMP),
    Column('len', Interval),
)

