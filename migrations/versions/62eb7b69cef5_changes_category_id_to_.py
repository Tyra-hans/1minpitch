"""changes category_id to categoryhishistoryyhistory

Revision ID: 62eb7b69cef5
Revises: 559b8f0c461e
Create Date: 2019-10-24 08:23:56.865378

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '62eb7b69cef5'
down_revision = '559b8f0c461e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitches', sa.Column('comments_id', sa.Integer(), nullable=True))
    op.add_column('pitches', sa.Column('description', sa.String(length=500), nullable=True))
    op.add_column('pitches', sa.Column('name', sa.String(length=100), nullable=True))
    op.create_index(op.f('ix_pitches_description'), 'pitches', ['description'], unique=False)
    op.create_index(op.f('ix_pitches_name'), 'pitches', ['name'], unique=False)
    op.drop_index('ix_pitches_pitch', table_name='pitches')
    op.drop_index('ix_pitches_title', table_name='pitches')
    op.create_foreign_key(None, 'pitches', 'comments', ['comments_id'], ['id'])
    op.drop_column('pitches', 'title')
    op.drop_column('pitches', 'pitch')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitches', sa.Column('pitch', sa.VARCHAR(length=300), autoincrement=False, nullable=True))
    op.add_column('pitches', sa.Column('title', sa.VARCHAR(length=100), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'pitches', type_='foreignkey')
    op.create_index('ix_pitches_title', 'pitches', ['title'], unique=False)
    op.create_index('ix_pitches_pitch', 'pitches', ['pitch'], unique=False)
    op.drop_index(op.f('ix_pitches_name'), table_name='pitches')
    op.drop_index(op.f('ix_pitches_description'), table_name='pitches')
    op.drop_column('pitches', 'name')
    op.drop_column('pitches', 'description')
    op.drop_column('pitches', 'comments_id')
    # ### end Alembic commands ###
