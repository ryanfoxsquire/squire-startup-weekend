"""empty message

Revision ID: 3fca2e1e966
Revises: 2cc9986e1ef
Create Date: 2015-07-08 21:54:00.667386

"""

# revision identifiers, used by Alembic.
revision = '3fca2e1e966'
down_revision = '2cc9986e1ef'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('candidates',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=255), nullable=True),
    sa.Column('last_name', sa.String(length=255), nullable=True),
    sa.Column('party', sa.String(length=255), nullable=True),
    sa.Column('picture_url', sa.String(length=255), nullable=True),
    sa.Column('twitter_url', sa.String(length=255), nullable=True),
    sa.Column('facebook_url', sa.String(length=255), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('candidates')
    ### end Alembic commands ###
