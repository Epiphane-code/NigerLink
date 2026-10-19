"""crer table chaineT

Revision ID: eec940a22234
Revises: 33e93f59fde0
Create Date: 2026-10-07 21:42:39.229677

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'eec940a22234'
down_revision: Union[str, Sequence[str], None] = '33e93f59fde0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('chainestemporaires',
        sa.Column('chaineId', sa.Integer(), nullable=False),
        sa.Column('titre', sa.String(length=100), nullable=False),
        sa.Column('pays', sa.String(length=100), nullable=False),
        sa.Column('ville', sa.String(length=100), nullable=False),
        sa.Column('description', sa.String(length=250), nullable=False),
        sa.Column('followers', sa.Integer(), default=0),
        sa.Column('motCle', sa.String(length=250), nullable=False),
        sa.Column('gestionnaireId', sa.Integer(), nullable=False),
        sa.Column('createById', sa.Integer(), nullable=False),
        sa.Column('dateCreate', sa.DateTime(), nullable=False),
        sa.Column('statut', sa.String(length=100), default='encours'),
        sa.ForeignKeyConstraint(['createById'], ['users.userId'], ),
        sa.ForeignKeyConstraint(['gestionnaireId'], ['users.userId'], ),
        sa.PrimaryKeyConstraint('chaineId')
        )
    op.create_index(op.f('ix_chainestemporaires_chaineId'), 'chainestemporaires', ['chaineId'], unique=False)
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
