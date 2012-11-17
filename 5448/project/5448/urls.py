from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', '{{ project_name }}.views.home', name='home'),
    # url(r'^{{ project_name }}/', include('{{ project_name }}.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'auth.views.index', name='index'),
    url(r'^new/$', 'auth.views.new_user', name='auth-new-user'),
    url(r'^created/$', 'auth.views.user_created', name='auth-user-created'),
    url(r'^validate/(?P<token>.*)/$', 'auth.views.validate', name='auth-user-validate'),
    url(r'^login/$', 'auth.views.login', name='auth-login'),
    url(r'^logout/$', 'auth.views.logout', name='auth-logout'),

    url(r'^dashboard/$', 'dashboard.views.index', name='dashboard'),
    url(r'^create_type/$', 'dashboard.views.create_activity_type', name='create-type'),
)
