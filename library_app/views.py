from django.shortcuts import render

from rest_framework import viewsets
from library_app.models import Auteur, Categorie, Commentaire, Editeur, Emprunt, Evaluation, Exemplaire, Livre
from library_app.serializers import AuteurSerializer, CategorieSerializer, CommentaireSerializer, EditeurSerializer, EmpruntSerializer, EvaluationSerializer, ExemplaireSerializer, LivreSerializer

# Create your views here.

class AuteurViewSet(viewsets.ModelViewSet):
    queryset = Auteur.objects.all()
    serializer_class = AuteurSerializer

class LivreViewSet(viewsets.ModelViewSet):
    queryset = Livre.objects.all()
    serializer_class = LivreSerializer

class CategorieViewSet(viewsets.ModelViewSet):
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer


class ExemplaireViewSet(viewsets.ModelViewSet):
    queryset = Exemplaire.objects.all()
    serializer_class = ExemplaireSerializer

class EmpruntViewSet(viewsets.ModelViewSet):
    queryset = Emprunt.objects.all()
    serializer_class = EmpruntSerializer


class CommentaireViewSet(viewsets.ModelViewSet):
    queryset = Commentaire.objects.all()
    serializer_class = CommentaireSerializer

class EditeurViewSet(viewsets.ModelViewSet):
    queryset = Editeur.objects.all()
    serializer_class = EditeurSerializer


class EvaluationViewSet(viewsets.ModelViewSet):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer