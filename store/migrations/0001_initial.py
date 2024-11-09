# Generated by Django 4.2.13 on 2024-11-08 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enterprise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Укажите название', max_length=255, verbose_name='Название')),
                ('email', models.EmailField(help_text='Укажите email', max_length=100, verbose_name='Почта')),
                ('country', models.CharField(help_text='Укажите страну', max_length=100, verbose_name='Страна')),
                ('city', models.CharField(help_text='Укажите город', max_length=100, verbose_name='Город')),
                ('street', models.CharField(help_text='Укажите улицу', max_length=100, verbose_name='Улица')),
                ('house_number', models.CharField(help_text='Укажите номер дома', max_length=10, verbose_name='Номер дома')),
                ('level', models.PositiveIntegerField(choices=[(0, 'Завод'), (1, 'Розничная сеть'), (2, 'Индивидуальный предприниматель')], default=0, verbose_name='Уровень сети')),
                ('debt', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Задолженность')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время и дата создания')),
                ('supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.enterprise', verbose_name='Поставщик')),
            ],
            options={
                'verbose_name': 'Звено сети',
                'verbose_name_plural': 'Звенья сети',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Укажите название продукта', max_length=255, verbose_name='Название продукта')),
                ('product_model', models.CharField(help_text='Укажите модель продукта', max_length=255, verbose_name='Модель продукта')),
                ('release_date', models.DateField(help_text='Укажите дату выхода продукта на рынок', verbose_name='Дата выхода продукта на рынок')),
                ('supplier', models.ManyToManyField(to='store.enterprise', verbose_name='Поставщик')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
    ]
