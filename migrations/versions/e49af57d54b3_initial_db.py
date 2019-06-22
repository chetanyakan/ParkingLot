"""Initial DB

Revision ID: e49af57d54b3
Revises: 
Create Date: 2019-06-22 18:15:42.998865

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e49af57d54b3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('slot',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('active', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('parking',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('slot_id', sa.Integer(), nullable=False),
    sa.Column('registration_number', sa.String(length=20), nullable=False),
    sa.Column('colour', sa.String(length=15), nullable=False),
    sa.Column('active', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['slot_id'], ['slot.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_parking_colour'), 'parking', ['colour'], unique=False)
    op.create_index(op.f('ix_parking_registration_number'), 'parking', ['registration_number'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_parking_registration_number'), table_name='parking')
    op.drop_index(op.f('ix_parking_colour'), table_name='parking')
    op.drop_table('parking')
    op.drop_table('slot')
    # ### end Alembic commands ###
