"""Add completed field to tasks

Revision ID: 6fea4c3271eb
Revises: 0fdfed6a96d2
Create Date: 2025-03-01 22:01:30.273120

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6fea4c3271eb'
down_revision: Union[str, None] = '0fdfed6a96d2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tasks', sa.Column('completed', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tasks', 'completed')
    # ### end Alembic commands ###
