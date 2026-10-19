"""ajout colonne

Revision ID: b47e6c7ed6c6
Revises: 2bf08fef37f6
Create Date: 2026-10-07 20:39:10.735156

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b47e6c7ed6c6'
down_revision: Union[str, Sequence[str], None] = '2bf08fef37f6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('chaines', sa.Column('approvedById', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'chaines', 'users', ['approvedById'], ['userId'])
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint(None, 'chaines', type_='foreignkey')
    op.drop_column('chaines', 'approvedById')
    pass
