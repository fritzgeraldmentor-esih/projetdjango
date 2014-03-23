# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Cour(models.Model):
    NomCours = models.CharField(max_length=100,verbose_name='Nom du Cours')
    CreditsECTS = models.CharField(max_length=3,verbose_name='Quantité Credits')
    Langues = models.CharField(choices=[('fr','Francais'),('an','Anglais'),('es','Espagnol'),('cr','Creole')],max_length=20)
    LieuEnseignement = models.CharField(max_length=100,verbose_name="Lieu d'enseignement")
    Grade = models.CharField(choices=[('Propedeutique','Propedeutique'),('L1','Premiere Annee Licence'),('L2','Deuxieme Annee Licence'),('L3','Troisieme Annee Licence')],max_length=50)
    Semestre = models.CharField(choices=[('S1','Premier Semestre'),('S2','Deuxieme Semestre')],max_length=30)
    PublicCible = models.CharField(max_length=50,verbose_name='Public Cible')
    Objectif = models.CharField(max_length=250,verbose_name='Objecctif du Cours')
    DescriptifCours = models.CharField(max_length=100,verbose_name='Description du Cours')

    def __unicode__(self):
        #return u'%s (%s credits)'%(self.NomCours, self.CreditsECTS)
        return u'%s|*:*|%s|*:*|%s|*:*|%s|*:*|%s|*:*|%s|*:*|%s|*:*|%s|*:*|%s'%( self.Semestre,self.Grade,self.NomCours, self.CreditsECTS, self.Langues, self.LieuEnseignement,  self.PublicCible, self.Objectif, self.DescriptifCours)


class Programme(models.Model):
    NomProgramme = models.CharField(max_length=100,verbose_name='Nom du Programme')
    Domaine = models.CharField(choices=[('E&G','Economie et Gestion'),('S&T','Sciences et Technologiques')],max_length=30)
    Mention = models.CharField(choices=[('E&G','Economie et Gestion'),('S&I','Sciences Informatiques')],max_length=30)
    Specialite = models.CharField(choices=[('TEL','Telecommunication'),('BDD','Base de Donnee'),('MONE','Management des Organisation de la Net Economie'),('SdE',"Sciences de l'Entreprise"),('SC','Sciences Comptables')],max_length=30,verbose_name='Specialité')

    def __unicode__(self):
        return u'%s'%(self.NomProgramme)
        #return u'%s|*:*|%s|*:*|%s|*:*|%s'%(self.NomProgramme, self.Domaine, self.Mention, self.Specialite)


class Professeur(models.Model):
    NomProfesseur = models.CharField(max_length=50,verbose_name='Nom du Professeur')
    PrenomProfesseur = models.CharField(max_length=50,verbose_name='Prenom du Professeur')
    Telephone = models.CharField(max_length=12)
    Email = models.EmailField(verbose_name='e-mail')
    CV = models.CharField(max_length=100)

    def __unicode__(self):
        return u'%s %s'%(self.NomProfesseur, self.PrenomProfesseur)
        #return u'%s|*:*|%s|*:*|%s|*:*|%s'%(self.NomProfesseur, self.PrenomProfesseur, self.Telephone, self.Email)

class Appartenir(models.Model):
   IdCours = models.ForeignKey(Cour,verbose_name='Cours')
   IdProgramme = models.ForeignKey(Programme,verbose_name='Programme')
   TypeCours = models.CharField(choices=[('OPT','Optionnel'),('OBL','Obligatoire')],max_length=20,verbose_name='Type du Cours')

   def __unicode__(self):
        return u'%s | %s | %s'%(self.IdCours, self.IdProgramme, self.TypeCours)



class Dispenser(models.Model):
    IdCours = models.ForeignKey(Cour)
    IdProfesseur = models.ForeignKey(Professeur)
    #CodeCours = ""
    #IdentiteProfesseur = ""

    def __unicode__(self):
        # ChampsCours = self.IdCours.split("|*:*|")
        # self.CodeCours = ChampsCours[0]+"-"+ChampsCours[1]+"-"+ChampsCours[2]
        # ChampsProfesseur = self.IdProfesseur.split("|*:*|")
        # self.IdentiteProfesseur = ChampsProfesseur[0]+" "+ChampsProfesseur[1]

        return u'%s | %s'%(self.IdCours, self.IdProfesseur)


