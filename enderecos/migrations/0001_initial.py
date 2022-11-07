# Generated by Django 4.1.2 on 2022-11-04 19:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Endereco",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("cidade", models.TextField()),
                ("estado", models.TextField()),
                ("rua", models.TextField()),
                ("numero", models.TextField()),
                ("complemento", models.TextField()),
                ("ponto_de_referencia", models.TextField()),
                (
                    "conta",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="endereco",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
