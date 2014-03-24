from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def dispCV(request):
    f = """
            <html>
            <head>
            <title>Test objet</title>
            </head>
            <body>
            <iframe src="CV_Professeurs\Sogecarte_e-statement_3.pdf" width="800" height="600" align="middle"></iframe>
            </body>
            </html>
        """
    #f="""<iframe frameborder = "0" width = "100%" height = "650" src = "C:\Users\acer\pythonfinal\pythonfinal\static\Mes_Fichiers\CV_Professeurs\Sogecarte_e-statement_3.pdf"></iframe>"""
    #f="""<iframe frameborder="0" width="100%" height="650%" src="C:\Users\acer\Desktop\Kids_lyrics.pdf"></iframe>"""
    return HttpResponse(f)