from django.db import models

# Create your models here.
#ei models ta dbsqlite e migrate korar jonno cmd te F:\Phitron reset\Django-with-Karim\myproject>python manage.py makemigration eta likhte hobe
# tarpor abar eta likhbo F:\Phitron reset\Django-with-Karim\myproject>python manage.py migrate
#erpor amra jokhon website er admin e kaaj korte jabo tokhon jei username and pass khujbe oitar jonno amra abar cmd te F:\Phitron reset\Django-with-Karim\myproject>python manage.py createsuperuser eta likhbo
class Feature(models.Model): #models.Model ei basic class k model e convert kortese
    #id: int eta amra comment kore dicchi karon models.model jokhon add korbo tokhon each object er id automatically create hoye jai
    name= models.CharField(max_length=100)
    details= models.CharField(max_length=500)
#ei model take ekhon amra admin.py file e register korbo