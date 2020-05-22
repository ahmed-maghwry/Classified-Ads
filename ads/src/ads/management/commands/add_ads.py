import datetime
import random
from django.core.management.base import BaseCommand
from ads.models import catugry , ads





class Command(BaseCommand):


    def handle(self, *args, **kwargs):

        main=catugry.objects.get(id=43)
        print(main)
        cat = ads.objects.get_or_create(
            title= 'test from command',
            description='test from command',
            main=main
            # sub=
            # end=
            # last=
            )

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))