from django.db import models

from .utils import validate_consecutive_digits, validate_credit_card


class CreditCardNumberManager(models.Manager):

    def create_from_file(self, _file):
        """Create credit cards from the file submitted by the form
        """
        cards = list()
        for number in _file.readlines()[1:]:
            clean_number = str(number, 'utf-8').replace('\n', '')
            credit_card, _ = self.get_or_create(number=clean_number)

            if validate_credit_card(clean_number) and validate_consecutive_digits(clean_number):
                credit_card.is_valid = True
            else:
                credit_card.is_valid = False
            credit_card.save()
            cards.append(credit_card)

        return cards


class CreditCardNumber(models.Model):
    """A credit card register
    """

    number = models.CharField('Credit card number', max_length=100)
    is_valid = models.BooleanField('Is valid?', default=False)

    objects = CreditCardNumberManager()

    def __str__(self):
        return '{} - {}'.format(self.number, self.is_valid)

    @property
    def is_valid_number(self):
        if self.is_valid:
            return 'Valid'
        return 'Invalid'
