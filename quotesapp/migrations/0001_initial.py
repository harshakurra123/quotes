# Generated by Django 3.2.11 on 2022-02-08 19:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QuoteCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'quote_category',
            },
        ),
        migrations.CreateModel(
            name='Quotes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote_description', models.CharField(max_length=500)),
                ('quote_title', models.CharField(max_length=100)),
                ('quote_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quotesapp.quotecategory')),
            ],
            options={
                'db_table': 'quotes',
            },
        ),
    ]