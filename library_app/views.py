from django.shortcuts import render

from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from library_app.models import Auteur, Categorie, Commentaire, Editeur, Emprunt, Evaluation, Exemplaire, Livre
from library_app.permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from library_app.serializers import AuteurSerializer, CategorieSerializer, CommentaireSerializer, EditeurSerializer, EmpruntSerializer, EvaluationSerializer, ExemplaireSerializer, LivreSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from library_app.models import BlacklistedToken
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.

class CustomPagination(PageNumberPagination):
    page_size = 5

class AuteurViewSet(viewsets.ModelViewSet):
    queryset = Auteur.objects.all()
    serializer_class = AuteurSerializer
    permission_classes = [IsAdminOrReadOnly]

class LivreViewSet(viewsets.ModelViewSet):
    queryset = Livre.objects.all()
    serializer_class = LivreSerializer
    permission_classes = [IsAdminOrReadOnly]
    
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]

    filterset_fields = ['categorie', 'langue']

    ordering_fields = ['date_de_publication']
    ordering = ['date_de_publication']

class CategorieViewSet(viewsets.ModelViewSet):
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer
    permission_classes = [IsAdminOrReadOnly]


class ExemplaireViewSet(viewsets.ModelViewSet):
    queryset = Exemplaire.objects.all()
    serializer_class = ExemplaireSerializer
    permission_classes = [IsAdminOrReadOnly]

    filter_backends = [DjangoFilterBackend]

    filterset_fields = ['etat', 'disponibilite']

class EmpruntViewSet(viewsets.ModelViewSet):
    queryset = Emprunt.objects.all()
    serializer_class = EmpruntSerializer
    permission_classes = [IsAdminOrReadOnly]


class CommentaireViewSet(viewsets.ModelViewSet):
    queryset = Commentaire.objects.all()
    serializer_class = CommentaireSerializer
    permission_classes = [IsAdminOrReadOnly]

class EditeurViewSet(viewsets.ModelViewSet):
    queryset = Editeur.objects.all()
    serializer_class = EditeurSerializer
    permission_classes = [IsAdminOrReadOnly]


class EvaluationViewSet(viewsets.ModelViewSet):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer
    pagination_class = CustomPagination
    permission_classes = [IsOwnerOrReadOnly]

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]

    filterset_fields = ['utilisateur', 'note']

    ordering_fields = ['date_evaluation', 'note']
    ordering = ['date_evaluation']

class LogoutAndBlacklistView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get("refresh_token")
            token = RefreshToken(refresh_token)

            token.blacklist()
            
            BlacklistedToken.objects.create(
                user=request.user,
                token=refresh_token
            )
            
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)