"""empty message

Revision ID: 56c1746dab61
Revises: 
Create Date: 2021-04-22 00:48:52.231897

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '56c1746dab61'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('comments', schema=None) as batch_op:
        batch_op.alter_column('comment',
               existing_type=sa.TEXT(),
               nullable='False')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('comments', schema=None) as batch_op:
        batch_op.alter_column('comment',
               existing_type=sa.TEXT(),
               nullable=True)

    # ### end Alembic commands ###