import random
import string

def random_string_generator(size=9, chars=string.ascii_uppercase + string.digits, core='VERA'):
    return core.join(random.choice(chars) for _ in range(size))