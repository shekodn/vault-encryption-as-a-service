# Generated by Django 3.1 on 2020-09-02 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("credit_cards", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="creditcard", name="pan", field=models.CharField(max_length=20),
        ),
    ]