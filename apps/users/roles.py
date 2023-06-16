from rolepermissions.roles import AbstractUserRole


class Admin(AbstractUserRole):
    available_permissions = {
        'full_permission': True,
    }


class Owner(AbstractUserRole):
    available_permissions = {
        'add_field': True,
        'delete_reservation': True,
    }


class User(AbstractUserRole):
    available_permissions = {
        'add_reservation': True,
        'view_field': True,
    }
