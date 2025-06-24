"""Add rating and interactive history

Revision ID: 1ef2f25b59d2
Revises: 
Create Date: 2025-06-23 23:01:40.121758

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1ef2f25b59d2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Создаем таблицу пользователей
    op.create_table('user',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('user_id', sa.String(), nullable=False),
        sa.Column('username', sa.String(), nullable=True),
        sa.Column('first_name', sa.String(), nullable=True),
        sa.Column('rating', sa.Integer(), nullable=False, server_default='0'),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('user_id')
    )
    
    # Создаем таблицу истории интерактивов
    op.create_table('interactive_history',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('interactive_name', sa.String(length=100), nullable=False),
        sa.Column('points_earned', sa.Integer(), nullable=False, server_default='1'),
        sa.Column('completed_at', sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    # Удаляем таблицы в обратном порядке
    op.drop_table('interactive_history')
    op.drop_table('user') 