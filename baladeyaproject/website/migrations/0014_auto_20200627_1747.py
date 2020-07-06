# Generated by Django 3.0.7 on 2020-06-27 14:47

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0013_auto_20200627_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='company_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 27, 17, 47, 18, 244226), null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='company', to='website.CompanyType'),
        ),
        migrations.AlterField(
            model_name='companysection',
            name='company_section_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 27, 17, 47, 18, 244226), null=True),
        ),
        migrations.AlterField(
            model_name='companytype',
            name='company_type_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 27, 17, 47, 18, 244226), null=True),
        ),
        migrations.AlterField(
            model_name='companytype',
            name='section',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='type', to='website.CompanySection'),
        ),
        migrations.AlterField(
            model_name='email',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 27, 17, 47, 18, 242238), null=True),
        ),
        migrations.AlterField(
            model_name='maalem',
            name='maalem_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 27, 17, 47, 18, 243231), null=True),
        ),
        migrations.AlterField(
            model_name='maalem',
            name='maalem_principal_image',
            field=models.ImageField(upload_to='Maalem/Principal/'),
        ),
        migrations.AlterField(
            model_name='maalemimage',
            name='maalem_image_image',
            field=models.ImageField(upload_to='Maalem/Second/'),
        ),
        migrations.AlterField(
            model_name='maalemimage',
            name='maalem_image_maalem',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='image', to='website.Maalem'),
        ),
        migrations.AlterField(
            model_name='newsactivity',
            name='news_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 27, 17, 47, 18, 238245), null=True),
        ),
        migrations.AlterField(
            model_name='newsactivity',
            name='news_principale_image',
            field=models.ImageField(upload_to='News/Activity/Principal/Image/'),
        ),
        migrations.AlterField(
            model_name='newsdecisions',
            name='news_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 27, 17, 47, 18, 237217), null=True),
        ),
        migrations.AlterField(
            model_name='newsdecisions',
            name='news_principale_image',
            field=models.ImageField(upload_to='News/Decision/Principal/Image/'),
        ),
        migrations.AlterField(
            model_name='newsfileactivity',
            name='news_file',
            field=models.FileField(blank=True, null=True, upload_to='News/Activity/Second/File/'),
        ),
        migrations.AlterField(
            model_name='newsfileactivity',
            name='news_image',
            field=models.ImageField(blank=True, null=True, upload_to='News/Activity/Second/Image/'),
        ),
        migrations.AlterField(
            model_name='newsfileactivity',
            name='relation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='activityfile', to='website.NewsActivity'),
        ),
        migrations.AlterField(
            model_name='newsfiledecisions',
            name='news_file',
            field=models.FileField(blank=True, null=True, upload_to='News/Decision/Second/File/'),
        ),
        migrations.AlterField(
            model_name='newsfiledecisions',
            name='news_image',
            field=models.ImageField(blank=True, null=True, upload_to='News/Decision/Second/Image/'),
        ),
        migrations.AlterField(
            model_name='newsfiledecisions',
            name='relation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='decisionfile', to='website.NewsDecisions'),
        ),
        migrations.AlterField(
            model_name='newsfileprojects',
            name='news_file',
            field=models.FileField(blank=True, null=True, upload_to='News/Projects/Second/File/'),
        ),
        migrations.AlterField(
            model_name='newsfileprojects',
            name='news_image',
            field=models.ImageField(blank=True, null=True, upload_to='News/Projects/Second/File/'),
        ),
        migrations.AlterField(
            model_name='newsfileprojects',
            name='relation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='projectfile', to='website.NewsProjects'),
        ),
        migrations.AlterField(
            model_name='newsprojects',
            name='news_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 27, 17, 47, 18, 239241), null=True),
        ),
        migrations.AlterField(
            model_name='newsprojects',
            name='news_principale_image',
            field=models.ImageField(upload_to='News/Projects/Principal/Image/'),
        ),
        migrations.AlterField(
            model_name='question',
            name='Question_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 27, 17, 47, 18, 240239), null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='Question_principal_image',
            field=models.ImageField(blank=True, null=True, upload_to='Contactus/Question/Principal/Image/'),
        ),
        migrations.AlterField(
            model_name='question',
            name='Question_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='question', to='website.QuestionType'),
        ),
        migrations.AlterField(
            model_name='rentalvaluebill',
            name='rental_value_bill_rental_value',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bill', to='website.RentalValue'),
        ),
        migrations.AlterField(
            model_name='response',
            name='response_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 27, 17, 47, 18, 241236), null=True),
        ),
        migrations.AlterField(
            model_name='response',
            name='response_principal_image',
            field=models.ImageField(blank=True, null=True, upload_to='Contactus/Response/Principal/Image'),
        ),
        migrations.AlterField(
            model_name='response',
            name='response_question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='response', to='website.Question'),
        ),
        migrations.AlterField(
            model_name='responsefile',
            name='response_file',
            field=models.FileField(blank=True, null=True, upload_to='Contactus/Response/Second/File/'),
        ),
        migrations.AlterField(
            model_name='responsefile',
            name='response_image',
            field=models.ImageField(blank=True, null=True, upload_to='Contactus/Response/Second/Image/'),
        ),
        migrations.AlterField(
            model_name='responsefile',
            name='response_response',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='file', to='website.Question'),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='transaction_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 27, 17, 47, 18, 242238), null=True),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='transactions_file',
            field=models.FileField(upload_to='Transactions/Principal/'),
        ),
    ]