# Generated by Django 4.0.3 on 2022-03-08 16:38

from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(db_index=True, default=False, editable=False)),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('code', models.SlugField(max_length=100, unique=True, verbose_name='Channel Code')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('picture', models.ImageField(upload_to='media/channels', verbose_name='Picture')),
            ],
            options={
                'verbose_name': 'Channel',
                'verbose_name_plural': 'Channels',
                'ordering': ('-created_at',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(db_index=True, default=False, editable=False)),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('season', models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(Decimal('0'))], verbose_name='Season')),
                ('episode', models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(Decimal('0'))], verbose_name='Episode')),
                ('rating', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=5, validators=[django.core.validators.MinValueValidator(Decimal('0')), django.core.validators.MaxValueValidator(Decimal('10'))], verbose_name='Rating')),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.channel', verbose_name='Channel')),
                ('file', models.ManyToManyField(blank=True, to='core.document', verbose_name='Document')),
            ],
            options={
                'verbose_name': 'Content',
                'verbose_name_plural': 'Contents',
                'ordering': ('-created_at',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(db_index=True, default=False, editable=False)),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('age_rate', models.PositiveIntegerField(default=0, help_text='Please enter the minimum age rate to reach contents of this genre.', verbose_name='Age Rate')),
            ],
            options={
                'verbose_name': 'Genre',
                'verbose_name_plural': 'Genres',
                'ordering': ('-created_at',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(db_index=True, default=False, editable=False)),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('code', models.SlugField(max_length=100, unique=True, verbose_name='Group Code')),
            ],
            options={
                'verbose_name': 'Group',
                'verbose_name_plural': 'Groups',
                'ordering': ('-created_at',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ContentPersonRelation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(db_index=True, default=False, editable=False)),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('relation_type', models.CharField(choices=[('author', 'Author'), ('director', 'Director'), ('cast', 'Cast')], max_length=20, verbose_name='Content Person Relation Type')),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.content', verbose_name='Content')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.person', verbose_name='Person')),
            ],
            options={
                'verbose_name': 'Content Person Relation',
                'verbose_name_plural': 'Content Person Relations',
                'ordering': ('-created_at',),
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='content',
            name='genre',
            field=models.ManyToManyField(blank=True, to='product.genre', verbose_name='Genre'),
        ),
        migrations.AddField(
            model_name='content',
            name='person',
            field=models.ManyToManyField(blank=True, through='product.ContentPersonRelation', to='core.person', verbose_name='Person'),
        ),
        migrations.AddField(
            model_name='channel',
            name='group',
            field=models.ManyToManyField(blank=True, to='product.groups', verbose_name='Group'),
        ),
        migrations.AddField(
            model_name='channel',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.language', verbose_name='Language'),
        ),
        migrations.AddField(
            model_name='channel',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.channel', verbose_name='Parent'),
        ),
        migrations.AddConstraint(
            model_name='contentpersonrelation',
            constraint=models.UniqueConstraint(fields=('content', 'person', 'relation_type'), name='product_contentpersonrelation_unique_content_person_relation_type'),
        ),
    ]
