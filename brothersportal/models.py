from django.db import models
from django.urls import reverse #Used to generate URLs by reversing the URL patterns
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import date


class Brother(models.Model):
    """
    Used to represent the model for Brothers
    """

    # Fields
    first_name = models.CharField(max_length=25, help_text="Enter first name")
    last_name = models.CharField(max_length=25, help_text="Enter last name")
    # To allow current brothers to see year distributions
    year = models.CharField(max_length=25,
                            help_text="Select current year at UVA",
                            choices=[('1st', '1st'), ('2nd', '2nd'),
                                     ('3rd', '3rd'), ('4th', '4th'),
                                     ('5th', '5th'), ('Alumni', "Alumni")],
                            default="1st")
    # To allow searching based on grad year (maybe tie to composites eventually?)
    grad_year = models.IntegerField(default=2000, validators=[MaxValueValidator(date.today().year + 6),
                                                              MinValueValidator(2012)])
    pledge_class = models.CharField(max_length=25, help_text="Enter your pledge class (eg. Alpha, Beta, ...)")
    # Both majors for people to match up and ask advice
    major = models.CharField(max_length=25, help_text="Enter your primary major")
    second_major = models.CharField(max_length=25,
                                    help_text="Enter second major (if applicable)",
                                    null=True,
                                    blank=True)
    # Company information for networking
    company = models.CharField(max_length=25,
                               help_text="Enter current company (if applicable)",
                               null=True,
                               blank=True)
    state = models.CharField(max_length=25, help_text="Enter home/work state")
    city = models.CharField(max_length=25, help_text="Enter home/work city")
    phone_number = PhoneNumberField()
    email = models.EmailField(unique=True)

    # Metadata
    class Meta:
        ordering = ["first_name"]

    # Methods
    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of Brother.
        """
        return reverse('brother-detail', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return self.first_name + " " + self.last_name
