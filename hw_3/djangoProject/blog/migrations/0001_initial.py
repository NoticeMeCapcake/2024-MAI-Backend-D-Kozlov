from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(verbose_name='ID курса')),
                ('login', models.CharField(max_length=100, verbose_name='Логин пользователя')),
                ('login', models.CharField(max_length=256, verbose_name='Пароль пользователя')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
        migrations.CreateModel(
            name='UserPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(verbose_name='ID курса')),
                ('author_id', models.UUIDField(verbose_name="ID автора")),
                ('name', models.CharField(max_length=100, verbose_name='Название поста')),
                ('content', models.TextField(verbose_name='Содержимое поста')),
                ('likes', models.IntegerField(verbose_name="Количество лайков"))
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(verbose_name='ID комментария')),

            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
    ]