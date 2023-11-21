# Generated by Django 4.2.7 on 2023-11-21 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='asset',
            new_name='target_asset',
        ),
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.TextField(blank=True, help_text="예: '서울특별시 마포구 연남동 사파리월드 12-3'"),
        ),
        migrations.AddField(
            model_name='user',
            name='favorite_company',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='saving_type',
            field=models.CharField(blank=True, choices=[('thrifty', '알뜰형'), ('challenging', '도전형'), ('diligent', '성실형')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='financial_products',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
