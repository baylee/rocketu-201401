from django.conf.urls import patterns, url

urlpatterns = patterns('storefront.views',
    url(r'^$', 'home', name='home'),
    url(r'^about/$', 'about', name='about'),
    url(r'^support/$', 'support', name='support'),

    url(r'^shop/$', 'shop', name='shop'),
    url(r'^shop/category/(?P<category>.*)/$', 'category', name='category'),
    url(r'^shop/product/(?P<product_name>.*)/$', 'product_detail', name='product_detail'),
)