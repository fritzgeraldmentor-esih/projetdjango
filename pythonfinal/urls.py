from django.conf.urls import patterns, include, url

from django.contrib import admin
#from administration.views import insertionCours
#from administration.views import index
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pythonfinal.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^$','administration.views.home'),

    # *** Les pages d'acceuils ***
    url(r'^administration/$', 'administration.views.Acceuil'),
    url(r'^cours/$', 'administration.views.Cours'),
    url(r'^professeur/$', 'administration.views.Professeur'),
    url(r'^programme/$', 'administration.views.Programme'),


    # *** Les formulaires d'inscription ***
    url(r'^cours/inserer/$', 'administration.views.FormulaireCours'),
    url(r'^professeur/inserer/$', 'administration.views.FormulaireProfesseur'),
    url(r'^programme/inserer/$', 'administration.views.FormulaireProgramme'),


    # *** Les insertions ***
    url(r'^cours/savecours/$','administration.views.InsertionCours'),
    url(r'^professeur/saveprofesseur/$','administration.views.InsertionProfesseur'),
    url(r'^programme/saveprogramme/$','administration.views.InsertionProgramme'),


    # *** Les Listings ***
    url(r'^cours/listercours/$','administration.views.ListerCours'),
    url(r'^professeur/listerprofesseur/$','administration.views.ListerProfesseur'),


    # *** Les Suppressions ***
    url(r'^cours/supprimercour/(\d+)/$','administration.views.SupprimerCours'),
    url(r'^professeur/supprimerprofesseur/(\d+)/$','administration.views.SupprimerProfesseur'),
    url(r'^professeur/supprimerprogramme/(\d+)/$','administration.views.SupprimerProgramme'),
	
)
