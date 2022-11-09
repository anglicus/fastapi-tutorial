"""add content column to posts table

Revision ID: 325e594ba166
Revises: 64a170313e58
Create Date: 2022-11-09 19:36:02.668385

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '325e594ba166'
down_revision = '64a170313e58'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
