from django.contrib import admin
from django.urls import path

# Home view
from question.views import (
    question_view,
)

from account.views import (
    registration_view,
    logout_view,
    login_view,
    account_view,
)

from home.views import (
    home_view,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name="home"),
    path('question/', question_view),
    path('register/', registration_view, name="register"),
    path('logout/', logout_view, name="logout"),
    path('login/', login_view, name="login"),
    path('account/', account_view, name="account"),
]

