from django.conf.urls import include, patterns

# Add additional url patterns for additional apps
# here and they will be included in the main urls.py
extrapatterns = patterns('',
     #(r'^explorer/', include('explorer.urls')),
     #(r'^helpdesk/', include('helpdesk.urls')),
    ('^', include('committees.urls')),
    ('^', include('case_studies.urls')),
    ('^', include('donations.urls')),
    ('^', include('speakers.urls')),
    ('^', include('staff.urls')),
    ('^', include('studygroups.urls')),
    ('^', include('videos.urls')),
)
