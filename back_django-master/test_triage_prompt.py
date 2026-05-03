import sys
import os
import types

sys.stdout.reconfigure(encoding='utf-8')
import types

class MockConfig:
    def __call__(self, name, default=''):
        if name == 'GEMINI_API_KEY':
            env_path = os.path.join(os.path.dirname(__file__), 'back', '.env')
            if os.path.exists(env_path):
                with open(env_path) as f:
                    for line in f:
                        if line.startswith('GEMINI_API_KEY='):
                            return line.split('=', 1)[1].strip().strip("'\"")
        return default

mock_decouple = types.ModuleType('decouple')
mock_decouple.config = MockConfig()
sys.modules['decouple'] = mock_decouple

sys.path.append(os.path.abspath('.'))

from back.apps.tickets.hf_triage import run_hf_triage

tests = [
    {
        "service": "ADSL",
        "description": "El connexion diali rahet kima kanet, chwia temchi chwia lala w ki nji na9ra mafhemt walo.",
        "history": ""
    },
    {
        "service": "Fibre",
        "description": "My internet is completely down since yesterday.",
        "history": ""
    },
    {
        "service": "4G",
        "description": "Je n'arrive pas à me connecter, le voyant est rouge.",
        "history": "Bot: Je suis désolé pour ce problème. Pouvez-vous vérifier si la carte SIM est bien insérée ?\nUser: oui, elle est bien insérée mais ça marche pas."
    },
    {
        "service": "ADSL",
        "description": "How do I bake a chocolate cake?",
        "history": ""
    }
]

for i, test in enumerate(tests):
    print(f"--- Test {i+1} ---")
    print(f"User: {test['description']}")
    try:
        res = run_hf_triage(test["service"], test["description"], test["history"])
        print(f"Bot: {res.get('reply', 'No reply key')}")
        print(f"is_resolved: {res.get('is_resolved', False)}, can_submit: {res.get('can_submit', False)}\n")
    except Exception as e:
        print(f"Error: {e}\n")
