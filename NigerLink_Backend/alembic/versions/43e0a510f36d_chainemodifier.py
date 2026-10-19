"""chainemodifier

Revision ID: 43e0a510f36d
Revises: 8dc1aa36cef0
Create Date: 2026-10-07 17:18:37.558273

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '43e0a510f36d'
down_revision: Union[str, Sequence[str], None] = '8dc1aa36cef0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
