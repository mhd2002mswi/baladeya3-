# Generated by Django 3.0.7 on 2020-06-24 14:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20200624_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='company_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 24, 17, 19, 43, 173253)),
        ),
        migrations.AlterField(
            model_name='companysection',
            name='company_section_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 24, 17, 19, 43, 173253)),
        ),
        migrations.AlterField(
            model_name='companytype',
            name='company_type_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 24, 17, 19, 43, 173253)),
        ),
        migrations.AlterField(
            model_name='email',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 24, 17, 19, 43, 170286)),
        ),
        migrations.AlterField(
            model_name='maalem',
            name='maalem_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 24, 17, 19, 43, 172674)),
        ),
        migrations.AlterField(
            model_name='newsactivity',
            name='news_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 24, 17, 19, 43, 168267)),
        ),
        migrations.AlterField(
            model_name='newsdecisions',
            name='news_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 24, 17, 19, 43, 167269)),
        ),
        migrations.AlterField(
            model_name='newsprojects',
            name='news_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 24, 17, 19, 43, 168267)),
        ),
        migrations.AlterField(
            model_name='question',
            name='Question_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 24, 17, 19, 43, 169263), null=True),
        ),
        migrations.AlterField(
            model_name='response',
            name='response_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 24, 17, 19, 43, 170286)),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='response_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 24, 17, 19, 43, 170286)),
        ),
    ]
