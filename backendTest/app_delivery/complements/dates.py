from datetime import datetime,date
from django.http import request
from django.http.response import HttpResponse, HttpResponseBadRequest

'''Este metodo se encarga de dejar realizar algunas validaciones de fechas y hora, además de que
 transforma la fecha para poder almacenarla en la base de datos'''
class Transformdata:
    def __init__(self,date=None):
        self.thisDate = date
    
    #transforma un string y lo regresa en tipo datetime
    def transform_date(self):
        try:
            dateObj = datetime.strptime(self.thisDate, '%d/%m/%y')
        except:
            HttpResponseBadRequest("Ingresa una fecha valida como viene en el campo de date")
        return dateObj
    
    #se una para la validación de cuando se crea un nuevo menu, si el menu tiene fecha anterior regresa un verdadero
    def validate_date(self):
        today = datetime.combine(date.today(), datetime.min.time())
        response=False
        if self.thisDate >= today:
            response = True

        return response

    #valida la hora si la hora en la que se consulta es distinta de las 11 regresa True
    def validate_hour(self):
        response= False
        current_hour = datetime.now().time()
        just_hour = str(current_hour)[0:2]

        if int(just_hour) > 11:
            response = True
        
        return response

