"""database creation

Revision ID: 8288009b447c
Revises: 
Create Date: 2024-06-30 23:15:34.681935

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "8288009b447c"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "accessories",
        sa.Column("brand", sa.String(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column(
            "size", sa.Enum("One_size", name="sizeaccessories"), nullable=False
        ),
        sa.Column("price", sa.Integer(), nullable=False),
        sa.Column("description", sa.String(), nullable=False),
        sa.Column("id", sa.UUID(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_accessories")),
    )
    op.create_table(
        "clothing",
        sa.Column("brand", sa.String(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column(
            "size",
            sa.Enum(
                "XS",
                "S",
                "M",
                "L",
                "XL",
                "XXl",
                "XXXl",
                "One_size",
                name="sizeinternational",
            ),
            nullable=False,
        ),
        sa.Column("price", sa.Integer(), nullable=False),
        sa.Column("description", sa.String(), nullable=False),
        sa.Column("id", sa.UUID(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_clothing")),
    )
    op.create_table(
        "footwear",
        sa.Column("brand", sa.String(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column(
            "size",
            sa.Enum(
                "thirty_five",
                "thirty_six",
                "thirty_seven",
                "thirty_eight",
                "thirty_nine",
                "forty",
                "forty_one",
                "forty_two",
                "forty_three",
                "forty_four",
                "forty_five",
                "forty_six",
                "forty_seven",
                "forty_eight",
                name="sizeeu",
            ),
            nullable=False,
        ),
        sa.Column("price", sa.Integer(), nullable=False),
        sa.Column("description", sa.String(), nullable=False),
        sa.Column("id", sa.UUID(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_footwear")),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("footwear")
    op.drop_table("clothing")
    op.drop_table("accessories")
    # ### end Alembic commands ###