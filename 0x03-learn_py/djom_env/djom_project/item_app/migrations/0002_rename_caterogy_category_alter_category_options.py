# Generated by Django 4.2.2 on 2023-06-13 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Caterogy',
            new_name='Category',
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
    ]
