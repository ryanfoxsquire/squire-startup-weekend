"""empty message

Revision ID: 90df00843d
Revises: 1fe85136437
Create Date: 2015-07-08 23:07:21.659119

"""

# revision identifiers, used by Alembic.
revision = '90df00843d'
down_revision = '1fe85136437'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('candidates', 'smi')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('candidates', sa.Column('smi', sa.INTEGER(), autoincrement=False, nullable=True))
    ### end Alembic commands ###
