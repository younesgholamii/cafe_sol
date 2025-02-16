# Generated by Django 5.0.7 on 2025-02-16 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafes_menu', '0003_cafe_cafe_describtion_cafe_fee'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cafe',
            options={'ordering': ['name']},
        ),
        migrations.RenameField(
            model_name='cafe',
            old_name='cafe_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='cafe',
            name='cafe_describtion',
        ),
        migrations.AddField(
            model_name='cafe',
            name='describtion',
            field=models.TextField(blank=True, null=True),
        ),
    ]
