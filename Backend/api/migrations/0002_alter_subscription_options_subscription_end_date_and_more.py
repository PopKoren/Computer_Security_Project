# Generated by Django 5.1.3 on 2024-11-20 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subscription',
            options={'ordering': ['-start_date']},
        ),
        migrations.AddField(
            model_name='subscription',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='plan',
            field=models.CharField(choices=[('Basic', 'Basic Plan'), ('Pro', 'Pro Plan'), ('Enterprise', 'Enterprise Plan')], max_length=20),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='start_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
