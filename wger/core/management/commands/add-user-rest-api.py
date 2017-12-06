from django.core.management.base import BaseCommand
from wger.core.models import UserProfile, User
'''
Custom command permitting users to create user accounts
'''


class Command(BaseCommand):

    help = 'Permit user to create user accounts'

    # Named (optional arguments)
    def add_arguments(self, parser):
        parser.add_argument('name', type=str)

        parser.add_argument(
            '--disable',
            action='store_true',
            dest='disable',
            default=False
        )

    def handle(self, *args, **options):
        name = options['name']

        try:
            user = User.objects.get(username=name)
            profile = UserProfile.objects.get(user=user)
            if options['disable']:
                profile.can_add_user = False
                self.stdout.write(self.style.SUCCESS(
                    "{0} is 'DISABLED' from adding users via the API".format(options['name'])))

            else:
                profile.can_add_user = True
                self.stdout.write(self.style.SUCCESS(
                    "{0} can add users via the API".format(options['name'])))
            profile.save()

        except Exception as exc:
            self.stdout.write(self.style.WARNING(exc))
