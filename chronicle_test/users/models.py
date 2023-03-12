from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, DateField, TextField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
    Default custom user model for Chronicle Test App.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    FEMALE = "female"
    MALE = "male"
    OTHER = "other"

    SEX_CHOICES = (
        (FEMALE, FEMALE.capitalize()),
        (MALE, MALE.capitalize()),
        (OTHER, OTHER.capitalize()),
    )

    #: First and last name do not cover name patterns around the globe
    name = None  # type: ignore
    first_name = CharField(_("First Name of User"), null=True, max_length=255)
    last_name = CharField(_("Last Name of User"), null=True, blank=True, max_length=255)
    sex = CharField(
        _("Sex"), null=True, choices=SEX_CHOICES, default=OTHER, max_length=255
    )
    pob = CharField(_("Place of Birth"), null=True, blank=True, max_length=255)
    dob = DateField(_("Date of Birth"), null=True)
    address = TextField(_("Address"), null=True, blank=True)

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
