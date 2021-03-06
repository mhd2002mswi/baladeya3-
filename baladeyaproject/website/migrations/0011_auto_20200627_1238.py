# Generated by Django 3.0.7 on 2020-06-27 09:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_auto_20200627_1224'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companysection',
            name='madetby',
        ),
        migrations.AlterField(
            model_name='company',
            name='company_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 27, 12, 38, 18, 328546), null=True),
        ),
        migrations.AlterField(
            model_name='companysection',
            name='company_section_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 27, 12, 38, 18, 327549), null=True),
        ),
        migrations.AlterField(
            model_name='companytype',
            name='company_type_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 27, 12, 38, 18, 327549), null=True),
        ),
        migrations.AlterField(
            model_name='email',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 27, 12, 38, 18, 325554), null=True),
        ),
        migrations.AlterField(
            model_name='maalem',
            name='maalem_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 27, 12, 38, 18, 326551), null=True),
        ),
        migrations.AlterField(
            model_name='newsactivity',
            name='news_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 27, 12, 38, 18, 322563), null=True),
        ),
        migrations.AlterField(
            model_name='newsdecisions',
            name='news_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 27, 12, 38, 18, 321565), null=True),
        ),
        migrations.AlterField(
            model_name='newsprojects',
            name='news_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 27, 12, 38, 18, 323559), null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='Question_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 27, 12, 38, 18, 324556), null=True),
        ),
        migrations.AlterField(
            model_name='response',
            name='response_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 27, 12, 38, 18, 324556), null=True),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='transaction_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 27, 12, 38, 18, 325554), null=True),
        ),
    ]
