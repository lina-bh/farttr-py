from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, BooleanField
import wtforms.validators as validators

things = ("maxlength", "maximum of {} characters"), (
    "minlength",
    "at least {} characters",
)


class DescriptiveForm(FlaskForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self:
            if field.description:
                field.description += ". "
            field.description += ", ".join(
                msg.format(getattr(field.flags, attr))
                for attr, msg in things
                if getattr(field.flags, attr)
            )


class JoinForm(DescriptiveForm):
    username = StringField(
        "username", (validators.DataRequired(), validators.Length(max=25))
    )
    email = EmailField("email")
    password = PasswordField(
        "password",
        validators=(
            validators.DataRequired(),
            validators.EqualTo("verify"),
            validators.Length(8),
        ),
    )
    verify = PasswordField("verify", (validators.DataRequired(), validators.Length(8)))
    accept_terms = BooleanField("accept terms", validators=(validators.DataRequired(),))
