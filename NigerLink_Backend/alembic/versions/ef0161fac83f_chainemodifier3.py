"""chainemodifier3

Revision ID: ef0161fac83f
Revises: 9ddaa4cb3a4d
Create Date: 2026-10-07 17:41:21.903619

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ef0161fac83f'
down_revision: Union[str, Sequence[str], None] = '9ddaa4cb3a4d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
