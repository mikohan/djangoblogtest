# Generated by Django 2.2.3 on 2019-07-01 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('elastic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=120, unique=True)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(db_index=True, max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categorypost', to='elastic.CategoryPost'),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, default='', max_length=255, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=255, null=True, unique=True)),
                ('description', models.TextField(db_index=True)),
                ('brand', models.CharField(db_index=True, max_length=255)),
                ('image', models.ImageField(default='product_images/no-img.jpg', upload_to='product_images/')),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='elastic.Category')),
            ],
        ),
    ]