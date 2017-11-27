from django.core.management.base import BaseCommand
from wger.core.models import UserProfile, User
'''
Custom command permitting users to create user accounts
'''

class Command(BaseCommand):

    help = 'List All users created by the indicated'

    # Named (optional arguments)
    def add_arguments(self, parser):
        parser.add_argument('name', type=str)


    def handle (self, *args, **options): 
        name = options['name']

        try:
            user = User.objects.get(username=name)
            profiles = UserProfile.objects.filter(added_by=user)

        except User.DoesNotExist:
            raise CommandError("User %s does not exist" % name)


        self.stdout.write(self.style.SUCCESS("These users were created by:%s" %name))
        for profile in profiles:
           self.stdout.write("User: %s" % profile.user.username)




