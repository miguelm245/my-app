from django.contrib import admin
from .models import Post

#Resgitra POST en el administrador de Django para poder
#consultar o actualizar informacion del o de los post
admin.site.register(Post)
