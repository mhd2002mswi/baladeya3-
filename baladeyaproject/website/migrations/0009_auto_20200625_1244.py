# Generated by Django 3.0.7 on 2020-06-25 09:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_auto_20200625_1146'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transactions',
            name='response_date',
        ),
        migrations.AddField(
            model_name='transactions',
            name='transaction_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 25, 12, 44, 19, 551418), null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='company_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 25, 12, 44, 19, 553414), null=True),
        ),
        migrations.AlterField(
            model_name='companysection',
            name='company_section_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 25, 12, 44, 19, 552415), null=True),
        ),
        migrations.AlterField(
            model_name='companytype',
            name='company_type_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 25, 12, 44, 19, 553414), null=True),
        ),
        migrations.AlterField(
            model_name='email',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 25, 12, 44, 19, 550417), null=True),
        ),
        migrations.AlterField(
            model_name='maalem',
            name='maalem_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 25, 12, 44, 19, 552415), null=True),
        ),
        migrations.AlterField(
            model_name='newsactivity',
            name='news_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 25, 12, 44, 19, 547431), null=True),
        ),
        migrations.AlterField(
            model_name='newsdecisions',
            name='news_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 25, 12, 44, 19, 546432), null=True),
        ),
        migrations.AlterField(
            model_name='newsprojects',
            name='news_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 25, 12, 44, 19, 548426), null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='Question_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 25, 12, 44, 19, 549425), null=True),
        ),
        migrations.AlterField(
            model_name='response',
            name='response_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 25, 12, 44, 19, 550417), null=True),
        ),
    ]
