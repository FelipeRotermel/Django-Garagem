# Generated by Django 4.1.7 on 2023-03-31 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('garagem', '0010_alter_cor_options_alter_veiculo_categoria_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cor',
            options={'verbose_name': 'Cor', 'verbose_name_plural': 'Cores'},
        ),
    ]
