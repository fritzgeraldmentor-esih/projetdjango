from django.db import models

# Create your models here.

class Programme(models.Model):
    Domaine = models.CharField(choices=[('E&G','Economie et Gestion'),('S&T','Sciences et Technologies')](max_length=50))
    Mention = models.CharField(choices=[('E&G','Economie et Gestion'),('SI','Sciences Informatiques')](max_length=50))
    Specialite = models.CharField(choices=[('TEL','Telecommunications'),('BDD','Base de Donnees'),('MONE','Management des Organisations de la Net Economie'),('SdE','Sciences de Entreprise'),('SC','Sciences Comptables')](max_length=20))
    TypeCours = models.CharField(choices=[('OBL','Obligatoire'),('OPT','Optionnel')](max_length=10))
    Langue = models.CharField(choices=[('A','Anglais'),('F','Francais'),('C','Creole')](max_length=10))

    def __unicode__(self):
        return self.Domaine

class Cours(models.Model):
    Etablissement = models.CharField(max_length=50)
    Grade = models.CharField(max_length=50)
    Semestre = models.CharField(max_length=2)
    NomCours = models.CharField(max_length=50)

    def __unicode__(self):
        return

class Professeur(models.Model):
    Nom = models.CharField(max_length=50)
    Prenom = models.CharField(max_length=50)
    Niveau = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    Tel = models.CharField(max_length=50)
    Cv = models.TextField(max_length=50)
    PassWord=models.TextField(max_length=50)

class DescriptionCours(models.Model):
    CodeCours = models.CharField(max_length=50)
    TitreCours = models.CharField(max_length=50)
    CreditEcts = models.CharField(max_length=2)
    LieuEnseignement = models.CharField(max_length=20)
    PublicCible = models.CharField(max_length=20)
    PreRequis = models.CharField(max_length=400)
    Objectif = models.CharField(max_length=400)
    Description = models.CharField(max_length=400)
    PlanCours = models.CharField(max_length=400)
    Format = models.CharField(max_length=400)
    Ressource = models.CharField(max_length=400)
    Evaluation = models.CharField(max_length=400)

class inst(models.Model):
    inst = models.CharField(max_length=40)
    def __unicode__(self):
        return u'%s' % (self.inst)

