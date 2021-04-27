from datetime import datetime,date
from django.http import request
from django.http.response import HttpResponse, HttpResponseBadRequest

class Transformdata:
    def __init__(self,date):
        self.thisDate = date
    

    def transform_date(self):
        try:
            dateObj = datetime.strptime(self.thisDate, '%d/%m/%y')
        except:
            HttpResponseBadRequest("Ingresa una fecha valida como viene en el campo de date")
        return dateObj

    def validate_date(self):
        today = datetime.combine(date.today(), datetime.min.time())
        response=False
        if self.thisDate >= today:
            response = True

        return response