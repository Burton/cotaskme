from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'cotaskme.views.home', name='home'),
    url(r'^new-task-list$', 'cotaskme.views.newlist', name='newlist'),

    url(r'^t/([^/]+)$', 'cotaskme.views.tasklist', name='tasklist'),
    url(r'^t/([^/]+)/_action$', 'cotaskme.views.tasklist_action', name='tasklist_action'),
    url(r'^t/([^/]+)/_post$', 'cotaskme.views.tasklist_post', name='tasklist_post'),

    url('', include('social.apps.django_app.urls', namespace='social')),
    url('logout$', 'cotaskme.views.logout_view'),

    url(r'^admin/', include(admin.site.urls)),
)
