from django.core.exceptions import ValidationError


class DomainValidator:
    BLACKLIST_DOMAINS = [
        'mail.ru',
        'yandex.ru'
    ]

    def __call__(self, value):

        _, _, domain = value.partition('@')

        if domain in self.BLACKLIST_DOMAINS:
            raise ValidationError('Prohibited domain')
