"""add last few columns to post table

Revision ID: 7332431f1c00
Revises: b8c55f0efad9
Create Date: 2022-11-09 19:54:30.885514

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7332431f1c00'
down_revision = 'b8c55f0efad9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('published', sa.Boolean(),
                                     nullable=False, server_default='TRUE'))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                                     nullable=False, server_default=sa.text('NOW()')))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
