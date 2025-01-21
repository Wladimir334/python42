import random
import string


class PasswordGenerator:
    special_chars = "!#$%&()_*@"

    def __init__(self, min_length=6,
                 max_length=12,
                 use_uppercase=False,
                 use_special_chars=False):
        self.min_length = min_length
        self.max_length = max_length
        self.use_uppercase = use_uppercase
        self.use_special_chars = use_special_chars

    def generate_password(self):
        if self.min_length > self.max_length:
            raise ValueError("Min length cann't be more then max length")
        length = random.randint(self.min_length, self.max_length)

        characters = string.ascii_lowercase + string.digits

        if self.use_uppercase:
            characters += string.ascii_uppercase

        if self.use_special_chars:
            characters += PasswordGenerator.special_chars

        password = "".join(random.choice(characters) for _ in range(length))

        return password

password_generator = PasswordGenerator(use_uppercase=True, use_special_chars=True)
print(password_generator.generate_password())
