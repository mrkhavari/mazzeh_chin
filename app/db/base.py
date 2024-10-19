from neomodel import install_all_labels

from app.admin.models.admin import Admin  # isort:skip


async def install_labels():
    install_all_labels()
