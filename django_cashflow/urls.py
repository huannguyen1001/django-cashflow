from django.conf.urls.defaults import *

urlpatterns = patterns('django_cashflow.views',
    url(r'^$', 'list_accounts', name="list-accounts"),
    url(r'^account/view/(?P<number>.*)/$', 'account_details', name="account-details"),
    url(r'^account/add/$', 'add_account', name="add-account"),
)
