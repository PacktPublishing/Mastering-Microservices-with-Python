from datetime import datetime

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
    Column('title', String(40), nullable=False),
    Column('owner_id', String(5), nullable=False),
    Column('date_created', TIMESTAMP),
    Column('len', Interval),
)


def get_video(id, *, session):
    query = videos.select().where(videos.c.id == id)
    results = session.execute(query).fetchone()

    return {
        'id': results.id,
        'title': results.title,
        'owner': results.owner_id,
        'date_created': results.date_created,
        'length': results.len
    }


def modify_video(id, title, owner_id, *, session):
    query = videos.update().where(videos.c.id == id)
    if title:
        query = query.values(title=title)
    if owner_id:
        query = query.values(owner_id=owner_id)

    session.execute(query)
    session.commit()


def add_video(title, owner_id, length, *, session):
    query = videos.insert().values(
        title=title,
        owner_id=owner_id,
        len=length,
        date_created=datetime.now()
    )
    r = session.execute(query)
    i = r.inserted_primary_key[0]
    session.commit()
    print(i)
    return i

""" uncomment below for v 22 """
"""
videos = Table(
    'videos', METADATA,
    Column('id', Integer, primary_key=True),
    Column('title', String(40), nullable=False),
    Column('title_v2', String(60)),
    Column('owner_id', String(5), nullable=False),
    Column('date_created', TIMESTAMP),
    Column('len', Interval),
)

def get_video(id, *, session):
    query = videos.select().where(videos.c.id == id)
    results = session.execute(query).fetchone()

    return {
        'id': results.id,
        'title': results.title_v2 or results.title,
        'owner': results.owner_id,
        'date_created': results.date_created,
        'length': results.len
    }
    
def modify_video(id, title, owner_id, *, session):
    query = videos.update().where(videos.c.id == id)
    if title:
        query = query.values(title_v2=title)
    if owner_id:
        query = query.values(owner_id=owner_id)

    session.execute(query)
    session.commit()
    

def add_video(title, owner_id, length, *, session):
    query = videos.insert().values(
        title_v2=title,
        owner_id=owner_id,
        len=length,
        date_created=datetime.now()
    )
    r = session.execute(query)
    i = r.inserted_primary_key[0]
    session.commit()
    return i
"""

