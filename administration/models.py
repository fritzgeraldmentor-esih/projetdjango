from django.db import models

# Create your models here.

class Cours(models.Model):
    NomCours = models.CharField(max_length=100)
    CreditsECTS = models.CharField(max_length=3)
    Langues = models.CharField(max_length=20)
    LieuEnseignement = models.CharField(max_length=100)
    Grade = models.CharField(max_length=2)
    Semestre = models.CharField(max_length=2)
    PublicCible = models.CharField(max_length=50)
    Objectif = models.CharField(max_length=250)
    DescriptifCours = models.CharField(max_length=100)


class Programmes(models.Model):
    NomProgramme = models.CharField(max_length=100)
    Domaine = models.CharField(max_length=30)
    Mention = models.CharField(max_length=30)
    Specialite = models.CharField(max_length=30)


class Professeurs(models.Model):
    NomProfesseur = models.CharField(max_length=50)
    PrenomProfesseur = models.CharField(max_length=50)
    Telephone = models.CharField(max_length=12)
    Email = models.CharField(max_length=100)
    CV = models.CharField(max_length=100)

class Appartenir(models.Model):
   IdCours = models.ForeignKey(Cours)
   IdProgramme = models.ForeignKey(Programmes)
   TypeCours = models.CharField(max_length=3)


class Dispenser(models.Model):
    IdCours = models.ForeignKey(Cours)
    IdProfesseur = models.ForeignKey(Professeurs)

