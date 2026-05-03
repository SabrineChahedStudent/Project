import sys
import os
import types

sys.stdout.reconfigure(encoding='utf-8')

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

print("Testing auto_submit trigger...")
res = run_hf_triage("ADSL", "yes", "Bot: These solutions did not work. Would you like me to submit a ticket?\nUser: Yes please.")
print(res)
