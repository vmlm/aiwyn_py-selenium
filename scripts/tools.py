import secrets
import string

HASH_LEN = 6
def append_random_hash(input_string):
    # Define the characters to choose from for the random hash
    characters = string.ascii_letters + string.digits  # includes letters (both cases) and digits

    # Generate a random 6-character hash
    random_hash = ''.join(secrets.choice(characters) for _ in range(HASH_LEN))

    # Append the random hash to the input string
    output_string = input_string + random_hash

    return output_string