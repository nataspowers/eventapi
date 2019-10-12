from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='max_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='min_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='date_created',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='date_modified',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='date_published',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
