from pypi_org.services import user_service
from pypi_org.viewmodels.shared.viewmodelbase import ViewModelBase
import regex as re

valid_email = re.compile("^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$")

class RegisterViewModel(ViewModelBase):
    def __init__(self):
        super().__init__()
        self.name = self.request_dict.name
        self.email = self.request_dict.email.lower().strip()
        self.password = self.request_dict.password.strip()
        self.age = self.request_dict.age.strip()

    def validate(self):
        if not self.name or not self.name.strip():
            self.error = 'You must specify a name'
        elif user_service.find_user_by_email(self.email):
            self.error = 'A user with that email already exists'
        elif not self.email or not self.email.lower().strip():
            self.error = 'You must specify an email'
        elif not valid_email.match(self.email.strip()):
            self.error = 'Please provide a valid email'
        elif not self.password or not self.password.strip():
            self.error = 'You must specify a password'
        elif len(self.password.strip()) < 8:
            self.error = 'The password must be at least 8 characters'
