"""fill title_v2 in

Revision ID: 14515d4ce091
Revises: 482a52fcba58
Create Date: 2019-03-25 22:08:07.526402

"""
import itertools

from alembic import op, context
import sqlalchemy as sa

from app import database


# revision identifiers, used by Alembic.
revision = '14515d4ce091'
down_revision = '482a52fcba58'
branch_labels = None
depends_on = None


def upgrade():
    # url = context.config.get_main_option("sqlalchemy.url")
    # engine = sa.create_engine(url)
    # DBSession.configure(bind=engine)
    connection = op.get_bind()
    for i in itertools.count():
        # with op.get_context().begin_transaction():
        q = database.videos.select().limit(1).offset(1 * i)
        print(q)
        results = connection.execute('select * from videos;')
        results = results.fetchall()
        print(results)
        if not results:
            break



def downgrade():
    pass
