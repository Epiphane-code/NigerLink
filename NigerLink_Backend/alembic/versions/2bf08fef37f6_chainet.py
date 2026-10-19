"""chaineT

Revision ID: 2bf08fef37f6
Revises: ef0161fac83f
Create Date: 2026-10-07 17:49:35.067060

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2bf08fef37f6'
down_revision: Union[str, Sequence[str], None] = 'ef0161fac83f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
