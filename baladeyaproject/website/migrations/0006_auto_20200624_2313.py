# Generated by Django 3.0.7 on 2020-06-24 20:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20200624_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='company_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 24, 23, 13, 9, 724106), null=True),
        ),
        migrations.AlterField(
            model_name='companysection',
            name='company_section_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 24, 23, 13, 9, 723108), null=True),
        ),
        migrations.AlterField(
            model_name='companytype',
            name='company_type_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 24, 23, 13, 9, 723108), null=True),
        ),
        migrations.AlterField(
            model_name='email',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 24, 23, 13, 9, 721114), null=True),
        ),
        migrations.AlterField(
            model_name='maalem',
            name='maalem_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 24, 23, 13, 9, 722112), null=True),
        ),
        migrations.AlterField(
            model_name='newsactivity',
            name='news_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 24, 23, 13, 9, 718122), null=True),
        ),
        migrations.AlterField(
            model_name='newsdecisions',
            name='news_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 24, 23, 13, 9, 717125), null=True),
        ),
        migrations.AlterField(
            model_name='newsprojects',
            name='news_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 24, 23, 13, 9, 719119), null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='Question_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 24, 23, 13, 9, 720117), null=True),
        ),
        migrations.AlterField(
            model_name='response',
            name='response_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 24, 23, 13, 9, 720117), null=True),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='response_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 24, 23, 13, 9, 721114), null=True),
        ),
    ]