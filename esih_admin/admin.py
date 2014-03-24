# -*- coding: utf-8 -*-
from django.contrib import admin
from esih_admin.models import *

# Register your models here.
class CourAdmin(admin.ModelAdmin):
    list_display=('NomCours','code_cours','CreditsECTS', 'Langues', 'LieuEnseignement', 'Grade', 'Semestre', 'PublicCible', 'Objectif', 'DescriptifCours')
    list_filter = ('CreditsECTS','LieuEnseignement','Langues','Grade', 'Semestre',)
    list_display_links = ('NomCours','DescriptifCours','code_cours',)
    ordering = ('NomCours', )
    search_fields = ('NomCours','PublicCible', 'Objectif',)

    def code_cours(self,cours):
        ch = str(cours.Grade)+str(cours.Semestre)+'-'+str(cours.NomCours)
        return ch.title().replace(' ','')

class ProgrammeAdmin(admin.ModelAdmin):
    list_display=('NomProgramme', 'Domaine', 'Mention', 'Specialite')
    list_filter = ('Domaine', 'Mention', 'Specialite',)
    list_display_links = ('NomProgramme',)
    ordering = ('NomProgramme', )
    search_fields = ('NomProgramme', 'Domaine', 'Mention', 'Specialite',)

class ProfesseurAdmin(admin.ModelAdmin):
    list_display=('NomProfesseur','PrenomProfesseur','Telephone','Email','CV')
    list_display_links = ('NomProfesseur','PrenomProfesseur','CV')
    ordering = ('NomProfesseur','PrenomProfesseur',)
    search_fields = ('NomProfesseur','PrenomProfesseur',)

class AppartenirAdmin(admin.ModelAdmin):
    list_display=('code_Attachement','nom_du_Cours', 'code_du_Cours', 'nom_du_Programme', 'TypeCours',)
    list_display_links = ('code_Attachement',)
    list_filter = ( 'IdProgramme', 'TypeCours',)
    #ordering = ('nom_du_Cours',)
    search_fields = ('code_Attachement','nom_du_Cours',)

    def code_Attachement(self,code):
        return code.IdProgramme.Domaine+'-'+code.IdProgramme.Mention+'-'+code.IdProgramme.Specialite+'-'+code.TypeCours+'-'+code.IdCours.Langues

    def nom_du_Cours(self,cours):
        return cours.IdCours.NomCours

    def code_du_Cours(self,cours):
        return cours.IdCours.Grade+cours.IdCours.Semestre+'-'+cours.IdCours.NomCours

    def nom_du_Programme(self,prog):
        return prog.IdProgramme.NomProgramme

class DispenserAdmin(admin.ModelAdmin):
    list_display=('IdCours','IdProfesseur')

admin.site.register(Cour, CourAdmin)
admin.site.register(Programme, ProgrammeAdmin)
admin.site.register(Professeur, ProfesseurAdmin)
admin.site.register(Appartenir, AppartenirAdmin)
admin.site.register(Dispenser, DispenserAdmin)


