from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType

from core.models import Customer, PaymentsCustomer

def set_up_super_admin_group(super_admin_group):
    # Get content types for each model
    customer_content_type = ContentType.objects.get_for_model(
        model=Customer
    )
    payments_content_type = ContentType.objects.get_for_model(
        model=PaymentsCustomer
    )

    # Get permissions based on the content types
    customer_permissions = Permission.objects.filter(
        content_type=customer_content_type
    )
    payment_permissions = Permission.objects.filter(
        content_type=payments_content_type
    )

    # Add permissions to super_admin_group
    super_admin_group.permissions.add(*customer_permissions, *payment_permissions)


def set_user_as_super_administrator(user):
    super_administrator_group, created = Group.objects.get_or_create(name='super_administrator')

    if created is True:
        set_up_super_admin_group(super_administrator_group)
    
    super_administrator_group.user_set.add(user)