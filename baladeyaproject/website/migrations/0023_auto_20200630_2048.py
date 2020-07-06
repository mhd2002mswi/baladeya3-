# Generated by Django 3.0.7 on 2020-06-30 17:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0022_auto_20200630_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='company_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 30, 20, 48, 52, 3316), null=True),
        ),
        migrations.AlterField(
            model_name='companysection',
            name='company_section_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 30, 20, 48, 52, 2352), null=True),
        ),
        migrations.AlterField(
            model_name='companytype',
            name='company_type_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 30, 20, 48, 52, 2352), null=True),
        ),
        migrations.AlterField(
            model_name='email',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 30, 20, 48, 52, 356), null=True),
        ),
        migrations.AlterField(
            model_name='maalem',
            name='maalem_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 30, 20, 48, 52, 1353), null=True),
        ),
        migrations.AlterField(
            model_name='newsactivity',
            name='news_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 30, 20, 48, 51, 997367), null=True),
        ),
        migrations.AlterField(
            model_name='newsactivity',
            name='news_principale_image',
            field=models.ImageField(upload_to='News/Activity/Principal/Image/'),
        ),
        migrations.AlterField(
            model_name='newsdecisions',
            name='news_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 30, 20, 48, 51, 996336), null=True),
        ),
        migrations.AlterField(
            model_name='newsprojects',
            name='news_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 30, 20, 48, 51, 998361), null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='Question_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 30, 20, 48, 51, 999360), null=True),
        ),
        migrations.AlterField(
            model_name='response',
            name='response_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 30, 20, 48, 51, 999360), null=True),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='transaction_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 30, 20, 48, 52, 356), null=True),
        ),
    ]
