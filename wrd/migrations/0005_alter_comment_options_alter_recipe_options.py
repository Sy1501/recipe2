# Generated by Django 5.0.6 on 2024-07-08 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wrd', '0004_alter_recipe_ingredients_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created_on']},
        ),
        migrations.AlterModelOptions(
            name='recipe',
            options={'ordering': ['-created_at']},
        ),
    ]