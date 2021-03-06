from django.urls import path

from . import views

urlpatterns = [
    path('managePatients', views.manage_patients, name='managePatients'),
    path('viewPatient/<int:patient_id>', views.view_patient, name='viewPatient'),
    path('registerPatient', views.register_patient, name='registerPatient'),
    path('printSticker/<int:patient_id>', views.print_sticker, name='printSticker'),

    # APIs
    path('managePatients/findPatientById', views.find_patient_by_id, name='findPatientById')
]
