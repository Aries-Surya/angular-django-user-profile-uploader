import os
import zipfile
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
import logging

logger = logging.getLogger(__name__)

@api_view(['POST'])
def upload_profile_photos(request):
    if 'file' not in request.FILES:
        logger.error('No file provided')
        return Response({'error': 'No file provided'}, status=status.HTTP_400_BAD_REQUEST)

    uploaded_file = request.FILES['file']
    if not uploaded_file.name.endswith('.zip'):
        logger.error('File is not a zip archive')
        return Response({'error': 'File is not a zip archive'}, status=status.HTTP_400_BAD_REQUEST)

    fs = FileSystemStorage()
    zip_file_path = fs.save(uploaded_file.name, uploaded_file)
    zip_file_path_full = fs.path(zip_file_path)

    logger.info(f'Uploaded file saved at {zip_file_path_full}')

    with zipfile.ZipFile(zip_file_path_full, 'r') as zip_ref:
        zip_ref.extractall(fs.location)
        for file_name in zip_ref.namelist():
            # Ensure we only process files, not directories
            if not file_name.endswith('/'):
                mobile = os.path.splitext(os.path.basename(file_name))[0].strip()
                logger.info(f'Extracted mobile number: {mobile}')
                if not mobile:
                    logger.warning(f'File name {file_name} does not contain a valid mobile number')
                    continue
                try:
                    user = User.objects.get(mobile=mobile)
                    logger.info(f'Found user: {user.name} with mobile {mobile}')
                    user.profile_photo = file_name
                    user.save()
                    logger.info(f'Profile photo updated for user with mobile {mobile}')
                except User.DoesNotExist:
                    logger.warning(f'User with mobile {mobile} does not exist')
                    continue

    return JsonResponse({'message': 'Files uploaded successfully'})

def index(request):
    return HttpResponse("Welcome to the User Profile Photo Upload Service")