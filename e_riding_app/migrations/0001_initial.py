# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-01 17:02
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('begin', models.DateTimeField()),
                ('close', models.DateTimeField()),
                ('place', models.CharField(max_length=100)),
                ('judges', models.ManyToManyField(related_name='competition_judges', to=settings.AUTH_USER_MODEL)),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='competition_manager', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DescriptionStep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('length', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Horse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=8)),
                ('color', models.CharField(max_length=8)),
                ('breed', models.CharField(max_length=8)),
                ('stable', models.CharField(max_length=8)),
                ('birthday', models.DateField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='horse_owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pair',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pair_horse', to='e_riding_app.Horse')),
            ],
        ),
        migrations.CreateModel(
            name='PairOnStart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight_rider', models.FloatField()),
                ('cheerleader', models.ManyToManyField(related_name='team_cheerleader', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('finish_time', models.DateTimeField()),
                ('vet_entrance_time', models.DateTimeField()),
                ('norm_execution', models.CharField(max_length=100)),
                ('description_step', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='step_description_step', to='e_riding_app.DescriptionStep')),
                ('pair', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='step_pair', to='e_riding_app.Pair')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pairs', models.ManyToManyField(related_name='team_pair', to='e_riding_app.Pair')),
            ],
        ),
        migrations.CreateModel(
            name='VetCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pulse', models.CharField(max_length=3)),
                ('mucouns_membrane', models.CharField(max_length=50)),
                ('capilary_refill', models.CharField(max_length=50)),
                ('dehydratation', models.CharField(max_length=50)),
                ('gut_sounds', models.CharField(max_length=50)),
                ('muscle_tone', models.CharField(max_length=50)),
                ('gait', models.CharField(max_length=2)),
                ('overall', models.CharField(max_length=50)),
                ('notes', models.TextField()),
                ('review_time', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vetcard_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='step',
            name='vet_card',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='step_vet_card', to='e_riding_app.VetCard'),
        ),
        migrations.AddField(
            model_name='paironstart',
            name='vet_card_on_start',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pair_on_start_vet_card', to='e_riding_app.VetCard'),
        ),
        migrations.AddField(
            model_name='pair',
            name='pair_on_start',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pair_on_start', to='e_riding_app.PairOnStart'),
        ),
        migrations.AddField(
            model_name='pair',
            name='rider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pair_rider', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='competition',
            name='teams',
            field=models.ManyToManyField(related_name='competition_teams', to='e_riding_app.Team'),
        ),
    ]
