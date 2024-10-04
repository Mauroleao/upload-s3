from django.http import HttpResponse
from django.shortcuts import render
from PIL import Image
import os
from django.conf import settings
from .models import Myfile
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

def home(request):
    if request.method == "GET":
        return render(request, "home.html")
    elif request.method == "POST":
        file = request.FILES['my_file']

        if file.size > 100000000:  # limit o tamanho maximo do arquivo upado // limitado ate 100mb
            return HttpResponse('Arquivo muito grande')

        # Salvar no S3
        mf = Myfile(title='minha_imagem', arquivo=file)
        mf.save()  # Salva tanto na pasta quanto o caminho no banco de dados

        # Salvar localmente
        local_path = os.path.join(settings.MEDIA_ROOT, file.name)
        with open(local_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        print(file)
        return render(request, "status.html", {"file": file})
        