"""add user table

Revision ID: 6852e89f1cbd
Revises: 325e594ba166
Create Date: 2022-11-09 19:42:27.971409

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6852e89f1cbd'
down_revision = '325e594ba166'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
