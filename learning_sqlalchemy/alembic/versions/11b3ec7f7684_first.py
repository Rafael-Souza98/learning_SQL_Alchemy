"""first

Revision ID: 11b3ec7f7684
Revises: 
Create Date: 2022-09-12 11:37:46.873609

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '11b3ec7f7684'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
     op.create_table(
        'account',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('description', sa.Unicode(200)),
        )

def downgrade() -> None:
    op.drop_table('account')
