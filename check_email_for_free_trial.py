
# Vérification d'email et activation d'un essai gratuit

import time

# Base de données simulée
user_db = {
    "Joanvouts@gmail.com": {
        'free_trial_used': False,
        'trial_start_date': 0
    }
}

# Fonction pour gérer l'inscription avec essai gratuit
def check_email_for_free_trial(email, user_db):
    # Liste des emails avec un essai gratuit
    free_trial_emails = ["Joanvouts@gmail.com"]
    
    # Vérification si l'email a déjà utilisé l'essai gratuit
    if email in free_trial_emails:
        if email in user_db:
            # Vérifier si l'utilisateur a déjà utilisé l'essai gratuit
            user_info = user_db[email]
            if user_info['free_trial_used']:
                return "Cet email a déjà utilisé l'essai gratuit."
            else:
                # Activer l'accès complet pendant un mois
                user_info['free_trial_used'] = True
                user_info['trial_start_date'] = time.time()  # Date du début de l'essai
                return "Essai gratuit activé pendant 1 mois."
        else:
            # Ajouter l'utilisateur au système avec essai gratuit
            user_db[email] = {
                'free_trial_used': True,
                'trial_start_date': time.time()
            }
            return "Essai gratuit activé pendant 1 mois."
    else:
        return "Abonnement requis."
