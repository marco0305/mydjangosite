# Generated by Django 3.0.6 on 2020-06-08 07:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pNames', models.CharField(max_length=50, unique=True)),
                ('pTypes', models.CharField(choices=[('Plastic Lens', '塑膠鏡片'), ('機構', '機構'), ('Others', '其它')], max_length=50)),
                ('pCaves', models.CharField(max_length=50)),
                ('pModels', models.CharField(max_length=50, unique=True)),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='Create_Time:')),
            ],
        ),
        migrations.CreateModel(
            name='ProductAttribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attCaves', models.CharField(max_length=5)),
                ('pNotes', models.CharField(max_length=200)),
                ('attID', models.CharField(max_length=20, null=True, unique=True)),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='Create_Time:')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='production.Product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductStocks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='Create_Time:')),
                ('psNumbers', models.IntegerField()),
                ('psNotes', models.CharField(max_length=200)),
                ('psChecked', models.BooleanField(blank=True, default=False, help_text='是否檢驗')),
                ('psCheckedDate', models.DateTimeField(blank=True, verbose_name='Check_Time:')),
                ('stockitem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='production.ProductAttribute')),
            ],
        ),
    ]
