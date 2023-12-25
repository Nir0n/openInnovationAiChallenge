"""Add index to depth column

Revision ID: c00a36afb9e7
Revises: 8ac3e7eb7afa
Create Date: 2023-12-24 20:43:58.841987

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c00a36afb9e7'
down_revision: Union[str, None] = '8ac3e7eb7afa'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_index('index_depth', 'images', ['depth'], unique=False)

def downgrade() -> None:
    op.drop_index('index_depth', table_name='images')
