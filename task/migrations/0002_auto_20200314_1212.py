# Generated by Django 3.0.4 on 2020-03-14 04:12

from django.db import migrations, models
import django.db.models.deletion
import task.validators


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='任务名'),
        ),
        migrations.AlterField(
            model_name='tool',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='工具名'),
        ),
        migrations.CreateModel(
            name='BatchTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='批量任务名')),
                ('dispatch', models.CharField(max_length=100, validators=[task.validators.cron_validator], verbose_name='调度')),
                ('active', models.BooleanField(default=True, verbose_name='是否生效')),
                ('task1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='task1', to='task.Task', verbose_name='任务1')),
                ('task10', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='task10', to='task.Task', verbose_name='任务10')),
                ('task2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='task2', to='task.Task', verbose_name='任务2')),
                ('task3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='task3', to='task.Task', verbose_name='任务3')),
                ('task4', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='task4', to='task.Task', verbose_name='任务4')),
                ('task5', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='task5', to='task.Task', verbose_name='任务5')),
                ('task6', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='task6', to='task.Task', verbose_name='任务6')),
                ('task7', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='task7', to='task.Task', verbose_name='任务7')),
                ('task8', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='task8', to='task.Task', verbose_name='任务8')),
                ('task9', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='task9', to='task.Task', verbose_name='任务9')),
            ],
            options={
                'verbose_name': '批量任务表',
                'verbose_name_plural': '批量任务表',
            },
        ),
    ]
