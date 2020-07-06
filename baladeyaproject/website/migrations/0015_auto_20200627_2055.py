# Generated by Django 3.0.7 on 2020-06-27 17:55

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0014_auto_20200627_1747'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsfiledecisions',
            name='madetby',
        ),
        migrations.AlterField(
            model_name='company',
            name='company_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 27, 20, 55, 56, 28544), null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='madetby',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='company',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='company', to='website.CompanyType'),
        ),
        migrations.AlterField(
            model_name='companysection',
            name='company_section_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 27, 20, 55, 56, 27554), null=True),
        ),
        migrations.AlterField(
            model_name='companytype',
            name='company_type_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 27, 20, 55, 56, 27554), null=True),
        ),
        migrations.AlterField(
            model_name='companytype',
            name='madetby',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='companytype',
            name='section',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='type', to='website.CompanySection'),
        ),
        migrations.AlterField(
            model_name='email',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 27, 20, 55, 56, 25552), null=True),
        ),
        migrations.AlterField(
            model_name='maalem',
            name='maalem_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 27, 20, 55, 56, 26549), null=True),
        ),
        migrations.AlterField(
            model_name='maalem',
            name='madetby',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='maalemimage',
            name='maalem_image_maalem',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='image', to='website.Maalem'),
        ),
        migrations.AlterField(
            model_name='maalemimage',
            name='madetby',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='newsactivity',
            name='madetby',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='newsactivity',
            name='news_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 27, 20, 55, 56, 22562), null=True),
        ),
        migrations.AlterField(
            model_name='newsdecisions',
            name='madetby',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='newsdecisions',
            name='news_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 27, 20, 55, 56, 21530), null=True),
        ),
        migrations.AlterField(
            model_name='newsfileactivity',
            name='madetby',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='newsfileactivity',
            name='relation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='activityfile', to='website.NewsActivity'),
        ),
        migrations.AlterField(
            model_name='newsfiledecisions',
            name='relation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='decisionfile', to='website.NewsDecisions'),
        ),
        migrations.AlterField(
            model_name='newsfileprojects',
            name='madetby',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='newsfileprojects',
            name='relation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='projectfile', to='website.NewsProjects'),
        ),
        migrations.AlterField(
            model_name='newsprojects',
            name='madetby',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='newsprojects',
            name='news_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 27, 20, 55, 56, 23557), null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='Question_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 27, 20, 55, 56, 24562), null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='Question_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='question', to='website.QuestionType'),
        ),
        migrations.AlterField(
            model_name='question',
            name='madetby',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='rentalvaluebill',
            name='rental_value_bill_rental_value',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bill', to='website.RentalValue'),
        ),
        migrations.AlterField(
            model_name='response',
            name='madetby',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='response',
            name='response_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 27, 20, 55, 56, 24562), null=True),
        ),
        migrations.AlterField(
            model_name='response',
            name='response_question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='response', to='website.Question'),
        ),
        migrations.AlterField(
            model_name='responsefile',
            name='madetby',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='responsefile',
            name='response_response',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='file', to='website.Question'),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='madetby',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='transaction_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 27, 20, 55, 56, 25552), null=True),
        ),
    ]
