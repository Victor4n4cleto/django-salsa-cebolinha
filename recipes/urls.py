from django.urls import path
from recipes.views import home

# todas as URLs do app de receitas
urlpatterns = [
    path('', home),

]
