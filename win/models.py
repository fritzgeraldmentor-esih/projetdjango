from django.db import models

# Create your models here.

class Programme(models.Model):
    Domaine = models.CharField(max_length=50)
    Mention = models.CharField(max_length=50)
    Specialite = models.CharField(max_length=50)
    TypeCours = models.CharField(max_length=50)
    Langue = models.CharField(max_length=50)


class Cours(models.Model):
    Etablissement = models.CharField(max_length=50)
    Grade = models.CharField(max_length=50)
    Semestre = models.CharField(max_length=2)
    NomCours = models.CharField(max_length=50)


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

