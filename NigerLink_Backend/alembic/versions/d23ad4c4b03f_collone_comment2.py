"""collone comment2

Revision ID: d23ad4c4b03f
Revises: b031af6d31bf
Create Date: 2026-10-09 08:46:17.796631

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd23ad4c4b03f'
down_revision: Union[str, Sequence[str], None] = 'b031af6d31bf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
