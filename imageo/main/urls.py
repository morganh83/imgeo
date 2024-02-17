from django.urls import path, include
from . import views
from django.urls import path
from django.contrib.auth.models import User
from viewflow.contrib.auth import AuthViewset
from viewflow.urls import Application, Site, ModelViewset


site = Site(title="ACME Corp", viewsets=[
    Application(
        title='Sample App',
        icon='people',
        app_name='sample',
        viewsets=[
            ModelViewset(model=User),
        ]
    ),
])

urlpatterns = [
    path('accounts/', AuthViewset(with_profile_view=False).urls),
    path('', views.search_view, name='search'),
    path('results/', views.results_view, name='results'),
    path('settings/', views.settings_view, name='settings'),
]
