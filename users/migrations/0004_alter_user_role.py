# Generated by Django 4.2.11 on 2024-04-25 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[(1, 'Фрилансер'), (2, 'Клиент')], default=1, max_length=20),
        ),
    ]
