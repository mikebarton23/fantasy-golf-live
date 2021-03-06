"""empty message

Revision ID: 71e2c1f3d64e
Revises: e91f8e3a6cfa
Create Date: 2020-07-30 11:37:41.061144

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '71e2c1f3d64e'
down_revision = 'e91f8e3a6cfa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('DraftedPlayer', sa.Column('tee_time', sa.String(length=40), nullable=True))
    op.add_column('available_player', sa.Column('tee_time', sa.String(length=40), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('available_player', 'tee_time')
    op.drop_column('DraftedPlayer', 'tee_time')
    # ### end Alembic commands ###
