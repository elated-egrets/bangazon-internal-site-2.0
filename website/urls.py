from django.conf.urls import url
from website import views
from . import views

app_name = "website"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.login_user, name='login'),
    url(r'^logout$', views.user_logout, name='logout'),
    url(r'^register$', views.register, name='register'),
    url(r'^sell$', views.sell_product, name='sell'),
    url(r'^payment_type/add$', views.add_payment_type, name='add_payment'),
    url(r'^products$', views.list_products, name='list_products'),
    url(r'^profile$', views.profile_view, name='profile'),
    url(r'^categories$', views.category_view, name='categories'),
    url(r'^my_products$', views.list_my_products, name='list_my_products'),
    url(r'^products/(?P<product>[0-9]+)$', views.product_detail, name='product_detail'),
    url(r'^payment_type/delete/(?P<payment>[0-9]+)/$', views.delete_payment_type, name='delete_person'),
    url(r'^my_products/delete/(?P<product>[0-9]+)/$', views.delete_my_product, name='delete_my_product'),
	  url(r'^categories/(?P<category>[0-9]+)/$', views.category_detail_view, name='category_detail'),
    url(r'^cart$', views.order_view, name='order_view')
]