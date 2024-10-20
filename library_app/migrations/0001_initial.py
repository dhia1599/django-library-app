# Generated by Django 5.1.2 on 2024-10-19 11:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Auteur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('biographie', models.TextField()),
                ('date_de_naissance', models.DateField()),
                ('date_de_deces', models.DateField(blank=True, null=True)),
                ('nationalite', models.CharField(max_length=100)),
                ('photo', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Editeur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('adresse', models.CharField(max_length=255)),
                ('site_web', models.URLField()),
                ('email_contact', models.EmailField(max_length=254)),
                ('description', models.TextField()),
                ('logo', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Exemplaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('etat', models.CharField(choices=[('Neuf', 'Neuf'), ('Bon', 'Bon'), ('Acceptable', 'Acceptable')], max_length=50)),
                ('date_acquisition', models.DateField()),
                ('localisation', models.CharField(max_length=100)),
                ('disponibilite', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Emprunt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_emprunt', models.DateTimeField(auto_now_add=True)),
                ('date_retour_prevue', models.DateTimeField()),
                ('date_retour_effective', models.DateTimeField(blank=True, null=True)),
                ('statut', models.CharField(choices=[('En cours', 'En cours'), ('Terminé', 'Terminé'), ('En retard', 'En retard')], max_length=50)),
                ('remarques', models.TextField(blank=True, null=True)),
                ('utilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('exemplaire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library_app.exemplaire')),
            ],
        ),
        migrations.CreateModel(
            name='Livre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=255)),
                ('resume', models.TextField()),
                ('date_de_publication', models.DateField()),
                ('isbn', models.CharField(max_length=13, unique=True)),
                ('nombre_de_pages', models.IntegerField()),
                ('langue', models.CharField(max_length=50)),
                ('image_de_couverture', models.URLField(blank=True, null=True)),
                ('auteurs', models.ManyToManyField(to='library_app.auteur')),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library_app.categorie')),
            ],
        ),
        migrations.AddField(
            model_name='exemplaire',
            name='livre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library_app.livre'),
        ),
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('commentaire', models.TextField(blank=True, null=True)),
                ('recommande', models.BooleanField(default=False)),
                ('date_evaluation', models.DateTimeField(auto_now_add=True)),
                ('utilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('livre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library_app.livre')),
            ],
        ),
        migrations.CreateModel(
            name='Commentaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenu', models.TextField()),
                ('date_publication', models.DateTimeField(auto_now_add=True)),
                ('note', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('visible', models.BooleanField(default=True)),
                ('modere', models.BooleanField(default=False)),
                ('utilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('livre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library_app.livre')),
            ],
        ),
    ]
