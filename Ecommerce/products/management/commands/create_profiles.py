from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

# profiles gets created automatically using signals


class Command(BaseCommand):

    users = [
        {'username': 'ahmad'},
        {'username': 'zavier'},
        {'username': 'shafiq'},
        {'username': 'hadi'},
        {'username': 'salam'},
        {'username': 'omar'},
        {'username': 'amina'},
        {'username': 'sara'},
        {'username': 'tariq'},
        {'username': 'ibrahim'},
        {'username': 'rana'},
        {'username': 'khaled'},
        {'username': 'samira'},
        {'username': 'leila'},
        {'username': 'karim'},
        {'username': 'mansour'},
        {'username': 'rashid'},
        {'username': 'yusuf'},
        {'username': 'hamza'},
        {'username': 'amir'},
        {'username': 'layla'},
        {'username': 'hana'},
        {'username': 'tamer'},
        {'username': 'najwa'},
        {'username': 'jamil'},
        {'username': 'farida'},
        {'username': 'lina'},
        {'username': 'adil'},
        {'username': 'samih'},
        {'username': 'aziz'},
        {'username': 'hakim'},
    ]

    for user in users:
        new_user, created = User.objects.get_or_create(
            **user,
        )
        if created:
            new_user.set_password('test')
            new_user.save()
            