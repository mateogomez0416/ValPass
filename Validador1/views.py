from django.http import HttpResponse
from django.shortcuts import render

from django.template import Template, RequestContext
from django.template.loader import get_template

import re

class Expression(object):
    def __init__(self,password):
        self.password=password 


    def Uppercase_letter(self):
        if re.match('[A-Z]',self.password[0]): 
            return "#21bd09"
        else:
            return "#bd0909"     

    def Three_number(self):
        if re.match('[(0-9)]{3}',self.password[1:4]):
            return "#21bd09"
        else:
            return "#bd0909"

    def Three_lowercase_letter(self):
        if re.match('[a-z]{3}',self.password[4:7]):
            return "#21bd09"
        else:
            return "#bd0909"

    def Special_characters(self):
        
        if self.password[7:10] == "   " :
            return "#bd0909"
        else:
            
            if re.match('[\W]{3}',self.password[7:10]):
               return "#21bd09"
            else:
               return "#bd0909"

    def Complete_expresion(self):
        if re.match('[A-Z][0-9]{3}[a-z]{3}[\W]{3}',self.password):
            return "#21bd09"
        else:
            return "#bd0909"    

        
        
        
def busqueda_productos(request):

    return render(request,"formData.html")


def resultado(request):


    correo= request.GET["pas"]
    usuario= request.GET["use"]

    ce=len(correo)

    valid = Expression(correo)

    if valid.Special_characters() == "#21bd09":
        mensaje= correo + " " + " valida"
           
        return render(request, "dataresult.html",{"valido_mayu":valid.Uppercase_letter(),"valido_num":valid.Three_number(),
        "valido_min":valid.Three_lowercase_letter(), "valido_charac":valid.Special_characters(),
        "valido":valid.Special_characters(),"sms":mensaje, "user":usuario})
    else:
         mensaje= correo + " " + " no valida!!"
         return render(request, "dataresult.html",{"valido_mayu":valid.Uppercase_letter(),"valido_num":valid.Three_number(),
         "valido_min":valid.Three_lowercase_letter(), "valido_charac":valid.Special_characters(),
         "valido":valid.Special_characters(),"sms":mensaje, "user":usuario})
         
    

    





