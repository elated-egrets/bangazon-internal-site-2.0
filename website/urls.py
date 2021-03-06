from django.conf.urls import url
from website import views
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "website"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url('login', views.login_user, name='login'),
    url(r'^logout$', views.user_logout, name='logout'),
    url(r'^register$', views.register, name='register'),
    url(r'^sell$', views.sell_product, name='sell'),
    url(r'^payment_type/add$', views.add_payment_type, name='add_payment'),
    url(r'^products$', views.list_products, name='list_products'),
    url(r'^profile$', views.profile_view, name='profile'),
    url(r'^profile/edit/(?P<pk>\d+)/$', views.edit_profile, name='edit_profile'),
    url(r'^categories$', views.category_view, name='categories'),
    url(r'^my_products$', views.list_my_products, name='list_my_products'),
    url(r'^products/(?P<product>[0-9]+)$', views.product_detail, name='product_detail'),
    url(r'^payment_type/delete/(?P<payment>[0-9]+)/$', views.delete_payment_type, name='delete_payment'),
    url(r'^my_products/delete/(?P<product>[0-9]+)/$', views.delete_my_product, name='delete_my_product'),
    url(r'^categories/(?P<category>[0-9]+)/$', views.category_detail_view, name='category_detail'),
    url(r'^cart$', views.order_view, name='order_view'),
    url(r'^categories/(?P<category>[0-9]+)/$', views.category_detail_view, name='category_detail'),
    url(r'^cart$', views.order_view, name='order_view'),
    url(r'^checkout$', views.complete_order_view, name='complete_order_view'),
    url(r'^categories/add$', views.category_add, name='category_add'),
    url(r'^checkout$', views.complete_order_view, name='complete_order_view'),
    url(r'^my_orders$', views.order_history_view, name='order_history'),
    url(r'^order/(?P<order>[0-9]+)$', views.order_history_detail_view, name='order_history_detail'),
]

if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

