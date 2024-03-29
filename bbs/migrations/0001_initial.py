# Generated by Django 2.2 on 2021-07-27 00:54

import bbs.storage
import ckeditor_uploader.fields
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nickname', models.CharField(blank=True, max_length=50, null=True)),
                ('avatar', models.FileField(default='/avatars/avatar.jpg', storage=bbs.storage.ImageStorage(), upload_to='avatar/%Y%m')),
                ('last_login_ip', models.CharField(max_length=64)),
                ('update_time', models.IntegerField(blank=True, null=True)),
                ('sex', models.PositiveIntegerField(default=0)),
                ('email', models.CharField(max_length=64)),
                ('mobile', models.CharField(blank=True, max_length=11, null=True)),
                ('birthday', models.DateTimeField(blank=True, null=True)),
                ('introduction', models.TextField(blank=True, null=True)),
                ('github', models.CharField(blank=True, max_length=255, null=True)),
                ('qq', models.CharField(blank=True, max_length=12, null=True)),
                ('sign', models.CharField(blank=True, max_length=128, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '用户表',
                'db_table': 'users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='分类名称')),
                ('description', models.TextField(blank=True, null=True, verbose_name='分类描述')),
                ('post_count', models.PositiveIntegerField(default=0, verbose_name='帖子个数')),
                ('create_time', models.IntegerField(verbose_name='创建时间')),
                ('update_time', models.IntegerField(blank=True, null=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '帖子分类表',
                'verbose_name_plural': '帖子分类表',
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Topics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('body', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('reply_count', models.PositiveIntegerField(default=0)),
                ('view_count', models.PositiveIntegerField(default=0)),
                ('sort', models.PositiveIntegerField(default=0)),
                ('create_time', models.PositiveIntegerField()),
                ('update_time', models.PositiveIntegerField(blank=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bbs.Categories')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '帖子表',
                'verbose_name_plural': '帖子表',
                'db_table': 'topics',
            },
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bbs.Topics')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '标签表',
                'verbose_name_plural': '标签表',
                'db_table': 'tags',
            },
        ),
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=191)),
                ('content', models.TextField(blank=True, null=True)),
                ('is_read', models.PositiveIntegerField(default=0)),
                ('create_time', models.IntegerField()),
                ('update_time', models.IntegerField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '通知表',
                'verbose_name_plural': '通知表',
                'db_table': 'notifications',
            },
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(default='info', max_length=32, verbose_name='异常级别')),
                ('request_path', models.CharField(max_length=191, verbose_name='请求地址')),
                ('ip', models.CharField(max_length=64)),
                ('params', models.TextField(verbose_name='请求参数')),
                ('content', models.TextField(blank=True, null=True, verbose_name='异常内容')),
                ('create_time', models.PositiveIntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '日志记录表',
                'verbose_name_plural': '日志记录表',
                'db_table': 'logs',
            },
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_like', models.PositiveIntegerField(default=0)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bbs.Topics')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '点赞表',
                'verbose_name_plural': '点赞表',
                'db_table': 'likes',
            },
        ),
        migrations.CreateModel(
            name='Collects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_name', models.CharField(max_length=50, verbose_name='收藏的帖子标题')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bbs.Topics')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '收藏表',
                'verbose_name_plural': '收藏表',
                'db_table': 'collects',
                'unique_together': {('user', 'topic')},
            },
        ),
    ]
