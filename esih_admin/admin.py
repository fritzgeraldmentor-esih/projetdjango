# -*- coding: utf-8 -*-
from django.contrib import admin
from esih_admin.models import *

# Register your models here.
class CourAdmin(admin.ModelAdmin):
    list_display=('NomCours', 'CreditsECTS', 'Langues', 'LieuEnseignement', 'Grade', 'Semestre', 'PublicCible', 'Objectif', 'DescriptifCours')
    list_filter = ('NomCours','CreditsECTS','LieuEnseignement','Langues','Grade', 'Semestre',)
    #date_hierarchy = 'date'
    ordering = ('NomCours', )
    search_fields = ('CreditsECTS', 'LieuEnseignement')

class ProgrammeAdmin(admin.ModelAdmin):
    list_display=('NomProgramme', 'Domaine', 'Mention', 'Specialite')

class ProfesseurAdmin(admin.ModelAdmin):
    list_display=('NomProfesseur','PrenomProfesseur','Telephone','Email')

class AppartenirAdmin(admin.ModelAdmin):
    list_display=('IdCours', 'IdProgramme', 'TypeCours','apercu_contenu')

    def apercu_contenu(self, appartenir):
        """
        Retourne les 40 premiers caractères du contenu de l'article. S'il
        y a plus de 40 caractères, il faut ajouter des points de
        suspension.
        """
        #pass
        b = str(appartenir.IdCours)
        a = b.split('|*:*|')
        return a[0]+' '+a[2]
        #text = article.IdCours[0:4]
        #if len(article.IdCours) > 4:
        #    return '%s...' % text
        #else:
        #    return text
        # En-tête de notre colonne
        #apercu_contenu.short_description = u'Aperçu du contenu'

class DispenserAdmin(admin.ModelAdmin):
    list_display=('IdCours','IdProfesseur')

admin.site.register(Cour, CourAdmin)
admin.site.register(Programme, ProgrammeAdmin)
admin.site.register(Professeur, ProfesseurAdmin)
admin.site.register(Appartenir, AppartenirAdmin)
admin.site.register(Dispenser, DispenserAdmin)


