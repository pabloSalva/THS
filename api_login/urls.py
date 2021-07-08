from django.urls import path, include

#from allauth.account.views import ConfirmEmailView
#from . import views
from .views import SocialLoginView

urlpatterns = [
    path('oauth/login/', SocialLoginView.as_view()),
    #  # Override urls
    # path('registration/account-email-verification-sent/', views.null_view, name='account_email_verification_sent'),
    # path('registration/account-confirm-email/(?P<key>[-:\w]+)/$', ConfirmEmailView.as_view(), name='account_confirm_email'),
    # path('registration/complete/$', views.complete_view, name='account_confirm_complete'),
    # path('password-reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.null_view, name='password_reset_confirm'),
    # # Default urls
    # path('', include('rest_auth.urls')),
    # path('registration/', include('rest_auth.registration.urls')),
]
