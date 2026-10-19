"""device

Revision ID: 8dc1aa36cef0
Revises: 5cbd8ab9cd9f
Create Date: 2026-10-07 17:05:33.016218

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8dc1aa36cef0'
down_revision: Union[str, Sequence[str], None] = '5cbd8ab9cd9f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
