"""user and message

Revision ID: 5b031ce35f4f
Revises: 5669255705d2
Create Date: 2023-05-18 12:49:49.464756

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5b031ce35f4f'
down_revision = '5669255705d2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('message', schema=None) as batch_op:
        batch_op.add_column(sa.Column('userid_from', sa.String(length=30), nullable=True))
        batch_op.add_column(sa.Column('userid_to', sa.String(length=30), nullable=True))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key(None, 'user', ['userid_to'], ['username'])
        batch_op.create_foreign_key(None, 'user', ['userid_from'], ['username'])
        batch_op.drop_column('userid')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('message', schema=None) as batch_op:
        batch_op.add_column(sa.Column('userid', sa.VARCHAR(length=30), nullable=True))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key(None, 'user', ['userid'], ['username'])
        batch_op.drop_column('userid_to')
        batch_op.drop_column('userid_from')

    # ### end Alembic commands ###
