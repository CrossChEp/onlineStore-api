"""orders

Revision ID: 4a521598c91b
Revises: 5e1298b968de
Create Date: 2022-05-02 19:00:54.974537

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4a521598c91b'
down_revision = '5e1298b968de'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('orders',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('author', sa.Integer(), nullable=True),
    sa.Column('content', sa.JSON(), nullable=True),
    sa.Column('date', sa.DATE(), nullable=True),
    sa.Column('status', sa.String(), nullable=True),
    sa.Column('address', sa.String(), nullable=True),
    sa.Column('index', sa.Integer(), nullable=True),
    sa.Column('price_sum', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['author'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('orders')
    # ### end Alembic commands ###
