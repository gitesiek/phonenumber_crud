from django.urls import path
from .views import ImagesFromFolderView, DownloadImageView, upload_food_photo


urlpatterns = [
    path('upload/', upload_food_photo, name='upload_food_photo'),
    path('images-from-folder/', ImagesFromFolderView.as_view(), name='images_from_folder'),
    path('download-image/<str:image_name>/', DownloadImageView.as_view(), name='download_image'),
]