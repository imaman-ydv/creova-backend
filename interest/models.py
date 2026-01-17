from django.db import models


class InterestSubmission(models.Model):
    INTEREST_CHOICES = [
        ('yes', 'Yes'),
        ('maybe', 'Maybe'),
        ('no', 'No'),
    ]

    interest = models.CharField(
        max_length=10,
        choices=INTEREST_CHOICES
    )

    price = models.PositiveIntegerField(
        null=True,
        blank=True
    )

    email = models.EmailField(
        null=True,
        blank=True
    )

    feedback = models.TextField(
        null=True,
        blank=True
    )

    ip_address = models.GenericIPAddressField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.interest} - {self.ip_address}"
