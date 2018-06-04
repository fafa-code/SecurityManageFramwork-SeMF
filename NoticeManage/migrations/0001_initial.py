# Generated by Django 2.0.4 on 2018-06-04 10:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notice_title', models.CharField(max_length=30, verbose_name='通知标题')),
                ('notice_body', models.TextField(verbose_name='通知内容')),
                ('notice_status', models.BooleanField(default=False, verbose_name='阅读状态')),
                ('notice_url', models.CharField(max_length=50, null=True, verbose_name='父链接')),
                ('notice_type', models.CharField(choices=[('notice', '安全通告'), ('inform', '任务通知')], max_length=30, verbose_name='通知类型')),
                ('notice_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='通知时间')),
                ('notice_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notice_for_user', to=settings.AUTH_USER_MODEL, verbose_name='所属用户')),
            ],
        ),
    ]
