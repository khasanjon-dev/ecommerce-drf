import re

from rest_framework.exceptions import ValidationError

phone_pattern = r"^998([378]{2}|(9[013-57-9]))\d{7}$"


def validate_phone(phone_number: str):
    if not re.search(phone_pattern, phone_number):
        raise ValidationError(
            f"{phone_number} \nPhone number must be entered in the format: '998 99 999 99 99'"
        )
