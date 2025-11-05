from django.contrib import admin
from .models import UserProfile, EmploymentContract,RentalAgreement,FreelanceContract,PartnershipAgreement, TranslatedContract
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(EmploymentContract)
admin.site.register(RentalAgreement)
admin.site.register(FreelanceContract)
admin.site.register(PartnershipAgreement)
admin.site.register(TranslatedContract)