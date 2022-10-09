from django.core.exceptions import ValidationError
from django.utils import timezone


def validate_date(date):
    if date > timezone.now().year:
        raise ValidationError(
            ('Заданный год: %(date)s больше текущего времени.'),
            params={'date': date},
        )
