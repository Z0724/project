"""newadd4

Revision ID: 6b718ab90519
Revises: a0dae3da21c6
Create Date: 2023-01-26 21:27:25.899658

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6b718ab90519'
down_revision = 'a0dae3da21c6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('BlogMains', schema=None) as batch_op:
        batch_op.create_foreign_key(None, 'users', ['author'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('BlogMains', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')

    # ### end Alembic commands ###
