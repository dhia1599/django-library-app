from rest_framework import serializers

from .models import Auteur, Livre, Categorie, Exemplaire, Emprunt, Commentaire, Editeur, Evaluation

class AuteurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auteur
        fields = '__all__'


class LivreSerializer(serializers.ModelSerializer):
    auteurs = serializers.PrimaryKeyRelatedField(many=True, queryset=Auteur.objects.all())

    class Meta:
        model = Livre
        fields = '__all__'


class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = '__all__'


class ExemplaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exemplaire
        fields = '__all__'


class EmpruntSerializer(serializers.ModelSerializer):
    utilisateur = serializers.StringRelatedField()
    exemplaire = ExemplaireSerializer()

    class Meta:
        model = Emprunt
        fields = '__all__'


class CommentaireSerializer(serializers.ModelSerializer):
    utilisateur = serializers.StringRelatedField()
    livre = serializers.StringRelatedField()

    class Meta:
        model = Commentaire
        fields = '__all__'


class EditeurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editeur
        fields = '__all__'


class EvaluationSerializer(serializers.ModelSerializer):
    utilisateur = serializers.StringRelatedField()
    livre = serializers.StringRelatedField()

    class Meta:
        model = Evaluation
        fields = '__all__'

