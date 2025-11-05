from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Links to Django's User model
    mobileno = models.CharField(max_length=15, unique=True)
    aadharno = models.CharField(max_length=100, blank=True, null=True)
    qualification = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.user.username

class Contract(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


from datetime import timedelta, date


def default_start_date():
    return date.today()

def default_end_date():
    return date.today() + timedelta(days=365) 


def default_deadline():
    return date.today() + timedelta(days=30)

def default_partnership_start_date():
    return date.today

def default_partnership_end_date():
    return date.today



       # 1 year from today

class EmploymentContract(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default='pending')
    contract_type=models.CharField(max_length=255,null=True)
    company_name = models.CharField(max_length=255)
    company_address = models.CharField(max_length=255)
    employee_name = models.CharField(max_length=255)
    department = models.CharField(max_length=255, blank=True, null=True)
    position = models.CharField(max_length=255)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    contract_duration = models.IntegerField(help_text="Duration in months")
    start_date = models.DateField(default=default_start_date) 
    end_date = models.DateField(default=default_end_date)
    probation_period = models.IntegerField(help_text="Probation period in months", blank=True, null=True)
    terms_conditions = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    # Malayalam Translations
    contract_type_ml = models.CharField(max_length=255, null=True, blank=True)
    company_name_ml = models.CharField(max_length=255, null=True, blank=True)
    company_address_ml = models.CharField(max_length=255, null=True, blank=True)
    employee_name_ml = models.CharField(max_length=255, null=True, blank=True)
    department_ml = models.CharField(max_length=255, blank=True, null=True)
    position_ml = models.CharField(max_length=100, null=True, blank=True)
    terms_conditions_ml = models.TextField(blank=True, null=True)

class RentalAgreement(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default='pending')
    contract_type=models.CharField(max_length=255,null=True)
    owner_name = models.CharField(max_length=255)
    property_address = models.TextField()
    tenant_name = models.CharField(max_length=255)
    monthly_rent = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    lease_term = models.IntegerField(help_text="Lease term in months")
    security_deposit = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    maintenance_charges = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    start_date = models.DateField(default=default_start_date) 
    end_date = models.DateField(default=default_end_date)
    terms_conditions = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    # Malayalam Translations
    contract_type_ml = models.CharField(max_length=255, null=True, blank=True)
    owner_name_ml = models.CharField(max_length=255, null=True, blank=True)
    property_address_ml = models.CharField(max_length=255, null=True, blank=True)
    tenant_name_ml = models.CharField(max_length=255, null=True, blank=True)
    terms_conditions_ml = models.TextField(blank=True, null=True)

class FreelanceContract(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default='pending')
    contract_type=models.CharField(max_length=255,null=True)
    client_name = models.CharField(max_length=255)
    client_email = models.EmailField()
    client_contact = models.CharField(max_length=15, blank=True, null=True)
    freelancer_name = models.CharField(max_length=255)
    project_description = models.TextField()
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    deadline = models.DateField(default=default_deadline)
    terms_conditions = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    # Malayalam Translations
    contract_type_ml = models.CharField(max_length=255, null=True, blank=True)
    client_name_ml = models.CharField(max_length=255, null=True, blank=True)
    freelancer_name_ml = models.CharField(max_length=255, null=True, blank=True)
    project_description_ml = models.CharField(max_length=255, blank=True, null=True)
    terms_conditions_ml = models.TextField(blank=True, null=True)



class PartnershipAgreement(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default='pending')
    contract_type=models.CharField(max_length=255,null=True)
    partner1_name = models.CharField(max_length=255)
    partner2_name = models.CharField(max_length=255)
    business_name = models.CharField(max_length=255)
    business_address = models.CharField(max_length=255, blank=True, null=True)
    profit_sharing = models.CharField(max_length=100, help_text="Profit sharing percentage")
    investment_details = models.TextField(blank=True, null=True)
    partnership_start_date = models.DateField(default=default_partnership_start_date)
    partnership_end_date = models.DateField(default=0)
    terms_conditions = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


   # Malayalam Translations
    contract_type_ml = models.CharField(max_length=255, null=True, blank=True)
    partner1_name_ml = models.CharField(max_length=255, null=True, blank=True)
    partner2_name_ml = models.CharField(max_length=255, null=True, blank=True)
    business_name_ml = models.CharField(max_length=255, null=True, blank=True)
    business_address_ml = models.CharField(max_length=255, blank=True, null=True)
    profit_sharing_ml = models.CharField(max_length=100, null=True, blank=True)
    investment_details_ml = models.TextField(blank=True, null=True)
    terms_conditions_ml = models.TextField(blank=True, null=True)


    from django.db import models

class TranslatedContract(models.Model):

    original_contract_id = models.IntegerField(null=True)
    contract_type = models.CharField(max_length=25, null=True)  # Fixed 'ChatField' to 'CharField'
    translated_text = models.TextField(null=True)
    language = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['original_contract_id', 'language']

    def __str__(self):
        return f"{self.original_contract_id} - {self.language} translation"



# from django.db import models
# from django.contrib.auth.models import User

# # Contract model
# class Contract(models.Model):
#     CONTRACT_TYPE_CHOICES = [
#         ('employment', 'Employment'),
#         ('rental', 'Rental'),
#         ('freelance', 'Freelance'),
#         ('partnership', 'Partnership'),
#     ]

#     STATUS_CHOICES = [
#         ('pending', 'Pending'),
#         ('approved', 'Approved'),
#         ('rejected', 'Rejected'),
#     ]

#     user = models.ForeignKey(User, on_delete=models.CASCADE)  # ForeignKey to the User model
#     contract_type = models.CharField(max_length=20, choices=CONTRACT_TYPE_CHOICES)
#     status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
#     date_created = models.DateTimeField(auto_now_add=True)  # Auto sets the date when created

#     def __str__(self):
#         return f"Contract {self.id} - {self.contract_type} ({self.status})"
