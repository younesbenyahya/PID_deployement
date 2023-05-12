# Generated by Django 4.2 on 2023-05-12 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=60)),
                ('lastname', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='ArtisteType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reservation.artist')),
            ],
        ),
        migrations.CreateModel(
            name='Locality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postal_code', models.CharField(max_length=6)),
                ('locality', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=60)),
                ('designation', models.CharField(max_length=60)),
                ('address', models.CharField(max_length=255)),
                ('website', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=30)),
                ('locality_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reservation.locality')),
            ],
        ),
        migrations.CreateModel(
            name='Representation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('when', models.DateTimeField()),
                ('location_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='reservation.location')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=255)),
                ('firstname', models.CharField(max_length=60)),
                ('lastname', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=100)),
                ('langue', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=60)),
                ('title', models.CharField(max_length=255, verbose_name='Show Title')),
                ('description', models.TextField(verbose_name='Show Description')),
                ('poster_url', models.CharField(max_length=255, verbose_name='Show Image')),
                ('bookable', models.BooleanField()),
                ('price', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('location_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='reservation.location')),
            ],
        ),
        migrations.CreateModel(
            name='RoleUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reservation.role')),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reservation.user')),
            ],
        ),
        migrations.CreateModel(
            name='RepresentationUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('places', models.IntegerField()),
                ('representation_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='reservation.representation')),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='reservation.user')),
            ],
        ),
        migrations.AddField(
            model_name='representation',
            name='show_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reservation.show'),
        ),
        migrations.CreateModel(
            name='ArtistTypeShow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artiste_type_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reservation.artistetype')),
                ('show_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reservation.show')),
            ],
        ),
        migrations.AddField(
            model_name='artistetype',
            name='type_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reservation.type'),
        ),
    ]
