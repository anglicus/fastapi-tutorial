"""add foreign key to posts table

Revision ID: b8c55f0efad9
Revises: 6852e89f1cbd
Create Date: 2022-11-09 19:50:02.345382

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b8c55f0efad9'
down_revision = '6852e89f1cbd'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('user_id', sa.Integer(), nullable=False))
    op.create_foreign_key('posts_users_fk', source_table='posts', referent_table='users', 
                          local_cols=['user_id'], remote_cols=['id'], ondelete='CASCADE')
    pass


def downgrade() -> None:
    op.drop_constraint('post_users_fx', table_name='posts')
    op.drop_column('posts', 'user_id')
    pass
