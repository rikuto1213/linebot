# your_app/views.py
import base64
from django.shortcuts import render, redirect
from .models import ImageData
from .forms import UploadImageForm

def upload_image(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            image_file = request.FILES['image']
            image_name = image_file.name
            encoded_image = base64.b64encode(image_file.read()).decode('utf-8')
            ImageData.objects.create(name=image_name, image_base64=encoded_image)
            return redirect('image_list')
    else:
        form = UploadImageForm()
    return render(request, 'bot_app/upload.html', {'form': form})

def image_list(request):
    images = ImageData.objects.all()
    return render(request, 'bot_app/image_list.html', {'images': images})
