# Generated by Django 4.2.1 on 2024-03-18 09:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_employeetravelallowance_km_covered_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employeetravelallowance',
            old_name='location_from',
            new_name='ending_location',
        ),
        migrations.RenameField(
            model_name='employeetravelallowance',
            old_name='location_to',
            new_name='starting_location',
        ),
        migrations.RemoveField(
            model_name='employeetravelallowance',
            name='km_covered',
        ),
        migrations.AddField(
            model_name='employeetravelallowance',
            name='ending_kilometer',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employeetravelallowance',
            name='starting_kilometer',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='employeetravelallowance',
            name='created_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='employeetravelallowance',
            name='employee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='travel_allowances', to='api.employee'),
        ),
    ]
