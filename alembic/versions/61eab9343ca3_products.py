"""products

Revision ID: 61eab9343ca3
Revises: 1c550e641c3d
Create Date: 2022-05-01 21:40:08.830762

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '61eab9343ca3'
down_revision = '1c550e641c3d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('products',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('author', sa.Integer(), nullable=True),
    sa.Column('sex', sa.String(), nullable=True),
    sa.Column('type', sa.String(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('sizes', sa.JSON(), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['author'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('products')
    # ### end Alembic commands ###
