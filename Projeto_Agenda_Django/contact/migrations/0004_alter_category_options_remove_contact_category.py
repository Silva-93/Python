# Generated by Django 4.2.5 on 2023-09-27 23:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_category_contact_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.RemoveField(
            model_name='contact',
            name='category',
        ),
    ]
