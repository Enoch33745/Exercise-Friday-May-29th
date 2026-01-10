import random
import string

def auto_gene(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    pasw = ''.join(random.choice(characters) for i in range(length))
    return pasw 
