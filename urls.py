from django.conf.urls.defaults import *

urlpatterns = patterns(
    '',
    (r'^', include('ripplesite.ripple.urls')),
    (r'^market/', include('ripplesite.market.urls')),
    
    # Uncomment this for admin:
    (r'^admin/', include('django.contrib.admin.urls')),
    
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/ryan/projects/ripplesite/ripple/media'}),
)
