from django import forms
from django.contrib.auth.forms import AdminUserCreationForm, UserChangeForm, AuthenticationForm
from .models import CustomUser

class CustomUserCreationForm(AdminUserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("email", "username")

            
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Remove help text for all fields
        for field_name, field in self.fields.items():
            field.help_text = None  # Use None instead of "" for cleaner HTML

        # Explicitly remove help text for password fields
        if 'password1' in self.fields:
            self.fields['password1'].help_text = None
        if 'password2' in self.fields:
            self.fields['password2'].help_text = None


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("email", "username")

class PasskeyLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add webauthn autocomplete for Conditional UI
        self.fields['username'].widget.attrs.update({
            'autocomplete': 'username webauthn',
            'class': 'form-control'  # Match Lithium styling
        })
        self.fields['password'].widget.attrs.update({
            'class': 'form-control'  # Match Lithium styling
        })
        
    # Add hidden passkey field for the authentication data
    passkeys = forms.CharField(
        required=False,
        widget=forms.HiddenInput(),
        label=''
    )