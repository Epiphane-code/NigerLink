"""collone comment

Revision ID: b031af6d31bf
Revises: eec940a22234
Create Date: 2026-10-09 08:45:19.449244

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b031af6d31bf'
down_revision: Union[str, Sequence[str], None] = 'eec940a22234'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
