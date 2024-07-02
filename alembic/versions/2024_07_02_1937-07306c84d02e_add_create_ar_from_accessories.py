"""add create_ar from accessories

Revision ID: 07306c84d02e
Revises: 64ddb6cdb70f
Create Date: 2024-07-02 19:37:30.950578

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "07306c84d02e"
down_revision: Union[str, None] = "64ddb6cdb70f"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "accessories",
        sa.Column(
            "create_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("accessories", "create_at")
    # ### end Alembic commands ###
