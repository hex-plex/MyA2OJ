"""User table

Revision ID: da6b20ac2b57
Revises: 
Create Date: 2020-06-01 13:33:15.520860

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'da6b20ac2b57'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('handle', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_handle'), 'user', ['handle'], unique=True)
    op.create_table('submission',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('verdict', sa.String(length=64), nullable=True),
    sa.Column('index', sa.String(length=5), nullable=True),
    sa.Column('contestId', sa.Integer(), nullable=True),
    sa.Column('pname', sa.String(length=64), nullable=True),
    sa.Column('timeCons', sa.Integer(), nullable=True),
    sa.Column('memoryCons', sa.Integer(), nullable=True),
    sa.Column('passedTestCount', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('pname')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('submission')
    op.drop_index(op.f('ix_user_handle'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###