"""empty message

Revision ID: 41e43654661
Revises: 3fca2e1e966
Create Date: 2015-07-08 22:52:17.554169

"""

# revision identifiers, used by Alembic.
revision = '41e43654661'
down_revision = '3fca2e1e966'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('candidates', sa.Column('smi', sa.Integer(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('candidates', 'smi')
    ### end Alembic commands ###
