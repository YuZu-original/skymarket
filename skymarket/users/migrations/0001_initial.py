

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(help_text='Введите имя, макс 64 символа', max_length=64, verbose_name='Имя')),
                ('last_name', models.CharField(help_text='Введите фамилию, макс 64 символа', max_length=64, verbose_name='Фамилия')),
                ('email', models.EmailField(help_text='Укажите электронную почту', max_length=254, unique=True, verbose_name='email address')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(help_text='Укажите телефон для связи', max_length=128, region=None, verbose_name='Телефон для связи')),
                ('role', models.CharField(choices=[('user', 'user'), ('admin', 'admin')], default='user', help_text='Выберите роль пользователя', max_length=20, verbose_name='Роль пользователя')),
                ('is_active', models.BooleanField(help_text='Укажите, активен ли аккаунт', verbose_name='Аккаунт активен')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
                'ordering': ['id'],
            },
        ),
    ]
