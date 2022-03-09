from core import services
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from product.models import Channel
from product.serializers import ChannelExportSerializer
from openpyxl.writer.excel import save_workbook


class Command(BaseCommand):
    help = 'Channel data export'

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.MIGRATE_HEADING('\nThis command prepares channels\' data and exports.'))
        r = input('Would you like to continue? (y/N): ')
        if r not in ('y', 'Y'):
            raise CommandError('Command exited.')

        self.stdout.write(self.style.SUCCESS('\nExcel is creating...'))

        qs = Channel.objects.all()
        serializer_class = ChannelExportSerializer
        service = services.ExcelExportService(
            queryset=qs, serializer_class=serializer_class,
        )
        file_name = service.create_csv(False)

        self.stdout.write(self.style.SUCCESS(
            '\nAll processes successfully finished and the exported file saved into \'media\' folder as \'%s\'.' % file_name
        ))

