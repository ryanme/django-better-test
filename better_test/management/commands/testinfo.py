from __future__ import absolute_import

from django.core.management.base import BaseCommand

from ...database import read_database


class Command(BaseCommand):
    def handle(self, *args, **options):
        database = read_database()
        if not database:
            self.stdout.write("No database found\n")
            return
        self.stdout.write("Last run test results\n")
        self.stdout.write("=====================\n\n")
        self.stdout.write("\n")
        self.stdout.write("Timings\n\n")
        for test, duration in sorted(database.get('timings', {}).items(),
                                     key=lambda x: -x[1]):
            self.stdout.write(
                "{duration:-7.3f} {test}\n".format(
                    test=test, duration=duration
                )
            )
        self.stdout.write("\n")
        self.stdout.write("Failed tests:\n\n")
        for failed in database.get('failed', []):
            self.stdout.write('    ' + failed + '\n')
