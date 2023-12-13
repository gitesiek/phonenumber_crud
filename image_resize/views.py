from django.shortcuts import render, redirect
from .forms import FoodPhotoForm
from django.views import View
from PIL import Image
import os
from django.urls import reverse
from django.http import HttpResponse
from .models import UploadedImage
from django.views.generic.edit import FormView
from .forms import FileFieldForm

def upload_food_photo(request):
    if request.method == 'POST':
        form = FoodPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_food_photo')
    else:
        form = FoodPhotoForm()
    return render(request, 'upload_food_photo.html', {'form': form})


class ImagesFromFolderView(View):
    def get(self, request):
        folder_path = 'uploads/'
        files = os.listdir(folder_path)
        images = [f for f in files if os.path.isfile(os.path.join(folder_path, f)) and f.lower().endswith(('.png', '.jpg', '.jpeg'))]

        download_links = []
        for image in images:
            download_url = reverse('download_image', kwargs={'image_name': image})
            download_links.append({'name': image, 'url': download_url})

        context = {'download_links': download_links}
        return render(request, 'images_from_folder.html', context)


class DownloadImageView(View):
    def get(self, request, image_name):
        folder_path = 'uploads/'
        file_path = os.path.join(folder_path, image_name)

        if os.path.exists(file_path):
            with open(file_path, 'rb') as file:
                response = HttpResponse(file.read(), content_type='image/jpeg')
                response['Content-Disposition'] = f'attachment; filename="{image_name}"'
                return response
        else:
            return HttpResponse("File not found")


class FileFieldFormView(FormView):
    form_class = FileFieldForm
    template_name = "mass_upload.html"  # Replace with your template.
    success_url = '/mass_upload/'

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        files = form.cleaned_data["file_field"]
        for f in files:
            img = Image.open(f)
            img.thumbnail((1008, 756))
            
            new_filepath = os.path.join('uploads', f.name)  # Define your destination folder path
            img.save(new_filepath)
            img.close()

        return super().form_valid(form)