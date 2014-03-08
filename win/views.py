from django.http import request
from django.shortcuts import render, redirect

# Create your views here.
from win.models import Cours, Professeur


def home(request):
    return render(request,'win/Acceuil.html',locals())

#fonction pour creer

def ccours(request):
    try:
        cours = Cours.objects.create(Etablissement=request.POST['Etablissement'],Grade=request.POST['Grade'],
                  Semestre=request.POST['Semestre'],NomCours=request.POST['NomCours'])

        return redirect("/icours/")
    except:
        return render(request,'win/Formulaire-Insertion-Cours.html',locals())
def cprof(request):
    try:
      prof=Professeur.objects.create(Nom=request.POST['NomProfesseur'],Prenom=request.POST['PrenomProfesseur'],
        Niveau=request.POST['NiveauProf'],Email=request.POST['Email'], Tel=request.POST['Telephone'],Cv=request.POST['UploadCV'],PassWord=request.POST[''])
      return redirect("/iprofesseur/")
    except:
        render(request,'win/Formulaire-Insertion-Professeur.html',locals())

def cDescriptionCours(request):
    try:
        DescriptionCours=DescriptionCours.objects.create(CodeCours=redirect.POST[''])

    except:
        pass






#fonction pour lister

def lcours(request):
    try:
        toutcours = Cours.objects.all()
        lcours = toutcours.reverse()
        return render(request,'win/ListeCours.html',locals())
    except:
        return render(request,'win/ListeCours.html',locals())

#fonction permettant de modifier

def mcours(reques,id):
    try:
        cours = Cours.objects.get(id=id)
        cours.Etablissement=request.Post['Etablissement']
        cours.Grade=request.Post['Grade']
        cours.NomCours=request.Post['NomCours']
        cours.Semestre=request.Post['Semestre']
        cours.save()
        return redirect("/listcours/")
    except:
        return render(request,'win/mcours.html',locals())


#fonctions pour suprimer

def scours(request,id):
    try:
        Cours.objects.filter(id=id).delete()
        return redirect("/listcours/")
    except:
        return render(request,'win/listecours.html',locals())
