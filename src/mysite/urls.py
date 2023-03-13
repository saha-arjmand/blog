from django.contrib import admin
from django.urls import path

# Home view
from question.views import (
    question_view,
)

from account.views import (
    account_view,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('question/', question_view),
    path('account/', account_view),
]
