"""empty message

Revision ID: 65471c7fad80
Revises: 
Create Date: 2020-01-07 19:26:14.076168

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '65471c7fad80'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dz_area',
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=32), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('dz_facilities',
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=32), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('dz_user',
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=32), nullable=False),
    sa.Column('password_hash', sa.String(length=128), nullable=False),
    sa.Column('mobile', sa.String(length=11), nullable=False),
    sa.Column('real_name', sa.String(length=32), nullable=True),
    sa.Column('id_card', sa.String(length=20), nullable=True),
    sa.Column('avatar_url', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('mobile'),
    sa.UniqueConstraint('name')
    )
    op.create_table('dz_house',
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('area_id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=64), nullable=False),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('address', sa.String(length=512), nullable=True),
    sa.Column('room_count', sa.Integer(), nullable=True),
    sa.Column('house_area', sa.Integer(), nullable=True),
    sa.Column('house_pattren', sa.String(length=32), nullable=True),
    sa.Column('capacity', sa.Integer(), nullable=True),
    sa.Column('beds', sa.String(length=64), nullable=True),
    sa.Column('deposit', sa.Integer(), nullable=True),
    sa.Column('min_days', sa.Integer(), nullable=True),
    sa.Column('max_days', sa.Integer(), nullable=True),
    sa.Column('order_count', sa.Integer(), nullable=True),
    sa.Column('index_image_url', sa.String(length=256), nullable=True),
    sa.ForeignKeyConstraint(['area_id'], ['dz_area.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['dz_user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('dz_facility',
    sa.Column('house_id', sa.Integer(), nullable=False),
    sa.Column('facility_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['facility_id'], ['dz_facilities.id'], ),
    sa.ForeignKeyConstraint(['house_id'], ['dz_house.id'], ),
    sa.PrimaryKeyConstraint('house_id', 'facility_id')
    )
    op.create_table('dz_house_image',
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('house_id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(length=256), nullable=False),
    sa.ForeignKeyConstraint(['house_id'], ['dz_house.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('dz_order',
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('house_id', sa.Integer(), nullable=False),
    sa.Column('begin_time', sa.DateTime(), nullable=False),
    sa.Column('end_time', sa.DateTime(), nullable=False),
    sa.Column('days', sa.Integer(), nullable=False),
    sa.Column('house_price', sa.Integer(), nullable=False),
    sa.Column('amount', sa.Integer(), nullable=False),
    sa.Column('status', sa.Enum('WAIT_ACCEPT', 'ACCEPT', 'REJECT', 'WAIT_PAID', 'PAID', 'CANCEL', 'WAIT_COMMENT', 'COMPLETE'), nullable=True),
    sa.Column('comment', sa.Text(), nullable=True),
    sa.Column('trade_no', sa.String(length=80), nullable=True),
    sa.ForeignKeyConstraint(['house_id'], ['dz_house.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['dz_user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_dz_order_status'), 'dz_order', ['status'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_dz_order_status'), table_name='dz_order')
    op.drop_table('dz_order')
    op.drop_table('dz_house_image')
    op.drop_table('dz_facility')
    op.drop_table('dz_house')
    op.drop_table('dz_user')
    op.drop_table('dz_facilities')
    op.drop_table('dz_area')
    # ### end Alembic commands ###
