import random
import string

def generate_strong_password(length=16):
    # List of characters
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    punctuation = string.punctuation

    # Assure-toi que le mot de passe a des caractères de chaque type
    all_characters = lower + upper + digits + punctuation

    # Créer un mot de passe avec au moins un de chaque type
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(punctuation)
    ]
    
    # Compléter le mot de passe jusqu'à la longueur demandée
    password += random.choices(all_characters, k=length-4)

    # Mélanger les caractères pour plus de sécurité
    random.shuffle(password)

    return ''.join(password)

# Exemple d'utilisation
print(generate_strong_password(16))  # Mot de passe de 16 caractères

# Ajout d'une entrée pour que le programme attende avant de se fermer
input("Appuyez sur Entrée pour fermer le programme...")
