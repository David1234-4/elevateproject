from django.shortcuts import render, get_object_or_404
from django.http import FileResponse
from .models import DownloadFile

def download_list(request):
    category = request.GET.get('category')
    files = DownloadFile.objects.filter(category=category) if category else DownloadFile.objects.all()
    return render(request, 'downloads/downloads.html', {'files': files})

def stream_video(request, file_id):
    file = get_object_or_404(DownloadFile, id=file_id)
    file.views += 1
    file.save()
    return render(request, 'downloads/player.html', {'file': file})

def download_file(request, file_id):
    file = get_object_or_404(DownloadFile, id=file_id)
    file.downloads += 1
    file.save()
    return FileResponse(file.file.open(), as_attachment=True)
