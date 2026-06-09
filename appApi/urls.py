from django.urls import path, include
from . import views


urlpatterns = [
    path("keyboardApp/auth/login", views.auth_user),
    path("keyboardApp/auth/validation", views.auth_validate_user),
    path("keyboardApp/auth/logout", views.auth_logout),
    path("keyboardApp/auth/signup", views.auth_signUp),
    path("keyboardApp/retrieve-item-data", views.retrieve_item_info),
    path("keyboardApp/retrieve_item_with_brand", views.retrieve_item_with_brand),
    path("keyboardApp/perform-transaction", views.user_transaction),
    path("keyboardApp/retrieve-transaction", views.retrieve_user_transaction),
    path("keyboardApp/retrieve-discount-code", views.retrieve_discount),
    path("keyboardApp/submit_review", views.submit_review),
    path("keyboardApp/retrieve-user-balance", views.retrieve_user_balance)
]

