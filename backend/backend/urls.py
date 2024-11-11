from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from lessons import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

router = routers.DefaultRouter()
router.register(r'aulas', views.AulaViewSet)
router.register(r'participantes', views.ParticipanteViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'instrutor_dashboard', views.InstrutorDashboardViewSet, basename='instrutor_dashboard')

schema_view = get_schema_view(
    openapi.Info(
        title="API de Aulas Online",
        default_version='v1',
        description="API para gerenciamento de aulas online",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="luketes.borges@gmail.com"),
        license=openapi.License(name="Lucas Borges License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), # Para obter o token JWT
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), # Para atualizar o token

    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
