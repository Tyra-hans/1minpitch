"""creates a comment table and a pitches table

Revision ID: 64cecfeb3c92
Revises: 1ff1d8b3ca17
Create Date: 2019-10-23 13:41:45.661446

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '64cecfeb3c92'
down_revision = '1ff1d8b3ca17'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_category_name'), 'category', ['name'], unique=False)
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('comment_post', sa.String(length=255), nullable=True),
    sa.Column('time', sa.DateTime(), nullable=True),
    sa.Column('pitch_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['pitch_id'], ['pitches.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_comments_comment_post'), 'comments', ['comment_post'], unique=False)
    op.add_column('pitches', sa.Column('category_id', sa.Integer(), nullable=True))
    op.add_column('pitches', sa.Column('pitch', sa.String(length=300), nullable=True))
    op.add_column('pitches', sa.Column('time', sa.DateTime(), nullable=True))
    op.add_column('pitches', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_pitches_pitch'), 'pitches', ['pitch'], unique=False)
    op.create_index(op.f('ix_pitches_title'), 'pitches', ['title'], unique=False)
    op.create_foreign_key(None, 'pitches', 'users', ['user_id'], ['id'])
    op.create_foreign_key(None, 'pitches', 'category', ['category_id'], ['id'])
    op.drop_column('pitches', 'category')
    op.drop_column('pitches', 'date_posted')
    op.drop_column('pitches', 'content')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitches', sa.Column('content', sa.TEXT(), autoincrement=False, nullable=True))
    op.add_column('pitches', sa.Column('date_posted', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.add_column('pitches', sa.Column('category', sa.TEXT(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'pitches', type_='foreignkey')
    op.drop_constraint(None, 'pitches', type_='foreignkey')
    op.drop_index(op.f('ix_pitches_title'), table_name='pitches')
    op.drop_index(op.f('ix_pitches_pitch'), table_name='pitches')
    op.drop_column('pitches', 'user_id')
    op.drop_column('pitches', 'time')
    op.drop_column('pitches', 'pitch')
    op.drop_column('pitches', 'category_id')
    op.drop_index(op.f('ix_comments_comment_post'), table_name='comments')
    op.drop_table('comments')
    op.drop_index(op.f('ix_category_name'), table_name='category')
    op.drop_table('category')
    # ### end Alembic commands ###
