# Generated by Django 4.2 on 2024-05-02 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('username', models.CharField(default='', max_length=20, primary_key=True, serialize=False)),
                ('password', models.CharField(default='', max_length=20)),
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=11)),
                ('isflamengo', models.BooleanField()),
                ('onePiece', models.BooleanField()),
                ('endereco', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('username', models.CharField(default='', max_length=20, primary_key=True, serialize=False)),
                ('password', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('username', models.CharField(default='', max_length=20, primary_key=True, serialize=False)),
                ('password', models.CharField(default='', max_length=20)),
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=11)),
            ],
        ),
        migrations.AddField(
            model_name='livro',
            name='categoria',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='livro',
            name='origem',
            field=models.CharField(default='Mari', max_length=100),
        ),
        migrations.AddField(
            model_name='livro',
            name='valor',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valorTotal', models.PositiveIntegerField()),
                ('valorDesconto', models.PositiveIntegerField()),
                ('formaPagamento', models.CharField(max_length=7)),
                ('Pagconcluido', models.BooleanField()),
                ('cliente', models.ManyToManyField(to='estoque.cliente')),
                ('vendedor', models.ManyToManyField(to='estoque.vendedor')),
            ],
        ),
    ]
