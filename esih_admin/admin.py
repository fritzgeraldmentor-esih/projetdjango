from django.contrib import admin
from esih_admin.models import *

# Register your models here.
class CourAdmin(admin.ModelAdmin):
    list_display=('NomCours', 'CreditsECTS', 'Langues', 'LieuEnseignement', 'Grade', 'Semestre', 'PublicCible', 'Objectif', 'DescriptifCours')

class ProgrammeAdmin(admin.ModelAdmin):
    list_display=('NomProgramme', 'Domaine', 'Mention', 'Specialite')

class ProfesseurAdmin(admin.ModelAdmin):
    list_display=('NomProfesseur','PrenomProfesseur','Telephone','Email')

class AppartenirAdmin(admin.ModelAdmin):
    list_display=('IdCours', 'IdProgramme', 'TypeCours')

class DispenserAdmin(admin.ModelAdmin):
    list_display=('IdCours','IdProfesseur')

admin.site.register(Cour, CourAdmin)
admin.site.register(Programme, ProgrammeAdmin)
admin.site.register(Professeur, ProfesseurAdmin)
admin.site.register(Appartenir, AppartenirAdmin)
admin.site.register(Dispenser, DispenserAdmin)


