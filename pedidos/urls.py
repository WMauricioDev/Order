from rest_framework.routers import DefaultRouter
from .views import RestauranteViewSet, ProductoViewSet, OrdenViewSet

router = DefaultRouter()
router.register(r'restaurantes', RestauranteViewSet)
router.register(r'productos', ProductoViewSet)
router.register(r'pedidos', OrdenViewSet)
urlpatterns = router.urls
