"""empty message

Revision ID: b0cafa8c8601
Revises:
Create Date: 2022-04-04 17:10:05.115372

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "b0cafa8c8601"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "initiates",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("name", sa.String(length=50), nullable=True),
        sa.Column("phone_number", sa.String(length=10), nullable=True),
        sa.Column("initiate_problem", sa.String(length=1024), nullable=True),
        sa.Column(
            "timestamp",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_initiates_timestamp"), "initiates", ["timestamp"], unique=False
    )
    op.create_table(
        "register_surgeons",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("name", sa.String(length=50), nullable=True),
        sa.Column("area", sa.String(length=255), nullable=True),
        sa.Column("phone_number", sa.String(length=10), nullable=True),
        sa.Column(
            "timestamp",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_register_surgeons_timestamp"),
        "register_surgeons",
        ["timestamp"],
        unique=False,
    )
    op.create_table(
        "reportsurgeons",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("opt_name", sa.String(length=50), nullable=True),
        sa.Column("phone_number", sa.String(length=10), nullable=True),
        sa.Column("surgeons_name", sa.String(length=50), nullable=True),
        sa.Column("area", sa.String(length=255), nullable=True),
        sa.Column("report_problem", sa.String(length=1024), nullable=True),
        sa.Column(
            "timestamp",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_reportsurgeons_timestamp"),
        "reportsurgeons",
        ["timestamp"],
        unique=False,
    )
    op.create_table(
        "roles",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=80), nullable=True),
        sa.Column("description", sa.String(length=255), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )
    op.create_table(
        "surgeons",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("name", sa.String(length=50), nullable=True),
        sa.Column("id_number", sa.String(length=50), nullable=True),
        sa.Column("area", sa.String(length=255), nullable=True),
        sa.Column("phone_number", sa.String(length=10), nullable=True),
        sa.Column("standard", sa.String(length=10), nullable=True),
        sa.Column("category", sa.String(length=10), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(length=50), nullable=False),
        sa.Column("password", sa.String(length=100), nullable=True),
        sa.Column("disabled", sa.Boolean(), nullable=True),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=True,
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_users_created_at"), "users", ["created_at"], unique=False)
    op.create_index(op.f("ix_users_email"), "users", ["email"], unique=True)
    op.create_table(
        "roles_users",
        sa.Column("user_id", sa.Integer(), nullable=True),
        sa.Column("role_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(["role_id"], ["roles.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], ondelete="CASCADE"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("roles_users")
    op.drop_index(op.f("ix_users_email"), table_name="users")
    op.drop_index(op.f("ix_users_created_at"), table_name="users")
    op.drop_table("users")
    op.drop_table("surgeons")
    op.drop_table("roles")
    op.drop_index(op.f("ix_reportsurgeons_timestamp"), table_name="reportsurgeons")
    op.drop_table("reportsurgeons")
    op.drop_index(
        op.f("ix_register_surgeons_timestamp"), table_name="register_surgeons"
    )
    op.drop_table("register_surgeons")
    op.drop_index(op.f("ix_initiates_timestamp"), table_name="initiates")
    op.drop_table("initiates")
    # ### end Alembic commands ###
