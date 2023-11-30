from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext as _

class CustomUser(AbstractUser):
    email_confirmed = models.BooleanField(default=False)
    email_confirmation_token = models.CharField(max_length=100, blank=True, null=True)
    is_approved = models.BooleanField(default=False)  # Adicione esta linha
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        related_name="%(app_label)s_%(class)s_related",
        related_query_name="%(app_label)s_%(class)ss",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name="%(app_label)s_%(class)s_related",
        related_query_name="%(app_label)s_%(class)ss",
    )

def create_groups():
    try:
        admin_group, _ = Group.objects.get_or_create(name='Administrador')
        user_group, _ = Group.objects.get_or_create(name='Usuário')

        admin_permissions = Permission.objects.filter(content_type__app_label='home')
        admin_group.permissions.set(admin_permissions)

        user_permissions = Permission.objects.filter(
            content_type__app_label='home',
            codename__in=['add_manutencao', 'change_manutencao']
        )
        user_group.permissions.set(user_permissions)
    except Exception as e:
        print('\033[92m' + 'Ocorreu um erro padrão de não existência de grupo.' + '\033[0m')
        print('\033[91m' + str(e) + '\033[0m')
        print('\033[92m' + 'Realize a migration normalmente.' + '\033[0m')
        pass
