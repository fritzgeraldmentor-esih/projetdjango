from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from administration.models import *
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return HttpResponse('Bonjour mon ami')




# ******************************
#      *** Les Acceuils ***
# ******************************
def homex(request):
    t = get_template('home.html')
    html = t.render(Context({}))
    return HttpResponse(html)
def home(request):
    return render(request,'home.html')
def Acceuil(request):
    t = get_template('Acceuil.html')
    html = t.render(Context({}))
    return HttpResponse(html)

def Cours(request):
    t = get_template('Cours\Cours.html')
    html = t.render(Context({}))
    return HttpResponse(html)

def Professeur(request):
    t = get_template('Professeur\Professeur.html')
    html = t.render(Context({}))
    return HttpResponse(html)

def Programme(request):
    t = get_template('Programme\Programme.html')
    html = t.render(Context({}))
    return HttpResponse(html)


# *********************************
#      *** Les Formulaires ***
# *********************************
def FormulaireCours(request):
    t = get_template('Cours\Formulaire-Insertion-Cours.html')
    html = t.render(Context({}))
    return HttpResponse(html)

def FormulaireProfesseur(request):
    t = get_template('Professeur\Formulaire-Insertion-Professeur.html')
    html = t.render(Context({}))
    return HttpResponse(html)

def FormulaireProgramme(request):
    t = get_template('Programme\Formulaire-Insertion-Programme.html')
    html = t.render(Context({}))
    return HttpResponse(html)

# ********************************
#      *** Les Insertions ***
# ********************************
def InsertionCours(request):
    try:
        NouveauCours = Cours(
            NomCours=request.POST['NomCours'] ,
            CreditsECTS=request.POST['CreditsECTS'] ,
            Langues=request.POST['Langues'] ,
            LieuEnseignement=request.POST['LieuEnseignement'] ,
            Grade=request.POST['Grade'] ,
            Semestre=request.POST['Semestre'] ,
            PublicCible=request.POST['PublicCible'],
            Objectif=request.POST['Objectif'] ,
            DescriptifCours=request.POST['DescriptifCours']
        )

        NouveauCours.save()
        list = Cours.objects.all()

        return render(request, 'Cours\ListeCours.html',locals())


    except KeyError:
        pass

def InsertionProfesseur(request):
    try:
        NouveauProfesseur = Professeurs(
            NomProfesseur=request.POST['NomProfesseur'] ,
            PrenomProfesseur=request.POST['PrenomProfesseur'] ,
            Telephone=request.POST['Telephone'] ,
            Email=request.POST['Email'] ,
            CV=request.POST['CV'] ,
        )

        NouveauProfesseur.save()
        listProfesseur = Professeurs.objects.all()

        ##return render(request, '{% url "administration.views.ListerProfesseur" %}',locals())
        return render(request, 'Professeur/ListeProfesseur.html',locals())


    except KeyError:
        pass


def InsertionProgramme(request):
    try:
        NouveauProgramme = Programmes(
            NomProgramme=request.POST['NomProgramme'] ,
            Domaine=request.POST['Domaine'] ,
            Mention=request.POST['Mention'] ,
            Specialite=request.POST['Specialite'] ,
        )

        NouveauProgramme.save()
        listProgramme = Programmes.objects.all()

        return render(request, 'Programme/ListeProgramme.html',locals())


    except KeyError:
        pass

# ******************************
#      *** Les Listings ***
# ******************************
def ListerCours(request):
    try:
        list = Cours.objects.all()
        return render(request, 'Cours\ListeCours.html',locals())
    except KeyError:
        pass

def ListerProfesseur(request):
    try:
        listProfesseur = Professeurs.objects.all()
        return render(request, 'Professeur\ListeProfesseur.html',locals())
    except KeyError:
        pass

def ListerProgramme(request):
    try:
        listProgramme = Programmes.objects.all()
        return render(request, 'Programme\ListeProgramme.html',locals())
    except KeyError:
        pass

# **********************************
#      *** Les Suppressions ***
# **********************************
def SupprimerCours(request, id):
    try:
        Cours.objects.filter(id=id).delete()
        return redirect(ListerCours)
    except KeyError:
        pass

def SupprimerProfesseur(request, id):
    try:
        Professeurs.objects.filter(id=id).delete()
        return redirect(ListerProfesseur)
    except KeyError:
        pass


def SupprimerProgramme(request, id):
    try:
        Programmes.objects.filter(id=id).delete()
        return redirect(ListerProgramme)
    except KeyError:
        pass
