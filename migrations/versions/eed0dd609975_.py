"""empty message

Revision ID: eed0dd609975
Revises: 0b84dd6e4a6a
Create Date: 2023-11-16 19:30:38.634602

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eed0dd609975'
down_revision = '0b84dd6e4a6a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('instructors',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('specialty', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('gym_classes',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('gym_name', sa.String(), nullable=True),
    sa.Column('type_class', sa.String(), nullable=True),
    sa.Column('instructor_id', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['instructor_id'], ['instructors.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('bookings',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('gym_class_id', sa.Integer(), nullable=True),
    sa.Column('booking_date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['gym_class_id'], ['gym_classes.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('bookings')
    op.drop_table('gym_classes')
    op.drop_table('instructors')
    # ### end Alembic commands ###