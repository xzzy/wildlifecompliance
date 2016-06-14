from __future__ import unicode_literals

from django.apps import AppConfig

class WLApplications(AppConfig):
    name = 'wildlifelicensing.apps.applications'
    label = 'wl_applications'

class WLDashboard(AppConfig):
    name = 'wildlifelicensing.apps.dashboard'
    label = 'wl_dashboard'

class WLMain(AppConfig):
    name = 'wildlifelicensing.apps.main'
    label = 'wl_main'

class WLEmails(AppConfig):
    name = 'wildlifelicensing.apps.emails'
    label = 'wl_emails'

class WLReturns(AppConfig):
    name = 'wildlifelicensing.apps.returns'
    label = 'wl_returns'