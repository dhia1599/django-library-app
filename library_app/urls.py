from rest_framework.routers import DefaultRouter
from .views import AuteurViewSet, CategorieViewSet, CommentaireViewSet, EditeurViewSet, EmpruntViewSet, EvaluationViewSet, ExemplaireViewSet, LivreViewSet

router = DefaultRouter()

router.register(r'auteurs', AuteurViewSet)
router.register(r'livres', LivreViewSet)
router.register(r'categories', CategorieViewSet)
router.register(r'exemplaires', ExemplaireViewSet)
router.register(r'emprunts', EmpruntViewSet)  # Notez l'ajustement du pluriel ici
router.register(r'commentaires', CommentaireViewSet)
router.register(r'editeurs', EditeurViewSet)
router.register(r'evaluations', EvaluationViewSet)

# Ajoutez les routes générées par le routeur à urlpatterns
urlpatterns = router.urls

