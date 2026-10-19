"""ajout 2 colonnes

Revision ID: 33e93f59fde0
Revises: b47e6c7ed6c6
Create Date: 2026-10-07 20:57:30.292125

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '33e93f59fde0'
down_revision: Union[str, Sequence[str], None] = 'b47e6c7ed6c6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('chaines', sa.Column('approvedByNom', sa.String(length=100), nullable=True))
    op.add_column('chaines', sa.Column('dateApproved', sa.DateTime(), nullable=True))
    
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('chaines', 'approvedByNom')
    op.drop_column('chaines', 'dateApproved')
    pass
