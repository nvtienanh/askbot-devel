# Generated by Django 2.2.17 on 2021-01-20 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('askbot', '0017_auto_20210116_0753'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vote',
            options={'verbose_name': 'vote', 'verbose_name_plural': 'đánh giá'},
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='languages',
            field=models.CharField(default='vi', max_length=128),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='primary_language',
            field=models.CharField(choices=[('vi', 'Vietnam')], default='vi', max_length=16),
        ),
    ]
