from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.core.urlresolvers import reverse_lazy


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^user-creation/$', views.AccountCreateView.as_view(), name='user_creation'),
    url(r'^(?P<pk>[0-9]+)/update/$', views.AccountUpdateView.as_view(), name='user_change'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout-with-template/$',
        auth_views.logout,
        {
            'template_name': 'app/logged_out.html',
        },
        name='logout_with_template'
    ),
    url(r'^logout-with-redirect/$',
        auth_views.logout,
        {
            'next_page': reverse_lazy('app:index'),
            'template_name': 'app/logged_out.html',
        },
        name='logout_with_redirect'
    ),
    url(r'^logout-then-login/$',
        auth_views.logout_then_login,
        {
        },
        name='logout_then_login'
    ),
    url(r'list/$',views.list, name='list'),
    url(r'^(?P<product_id>[0-9]+)/detail/$', views.detail, name='detail'),
]
