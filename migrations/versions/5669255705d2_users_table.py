"""users table

Revision ID: 5669255705d2
Revises: 
Create Date: 2023-05-17 13:00:16.151376

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5669255705d2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('username', sa.String(length=30), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('hashed_password', sa.String(length=128), nullable=False),
    sa.Column('is_pro', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('username')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_user_name'), ['name'], unique=False)

    op.create_table('message',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('text', sa.String(length=288), nullable=True),
    sa.Column('time', sa.DateTime(), nullable=True),
    sa.Column('userid', sa.String(length=30), nullable=True),
    sa.ForeignKeyConstraint(['userid'], ['user.username'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('message', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_message_time'), ['time'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('message', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_message_time'))

    op.drop_table('message')
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_user_name'))

    op.drop_table('user')
    # ### end Alembic commands ###