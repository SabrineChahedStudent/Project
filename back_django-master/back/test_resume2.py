import os
import sys

sys.path.append(os.path.abspath('.'))

from apps.tickets.hf_triage import generer_resume_ia

hist = "Client: Hello\nAssistant: Hi, how can I help?\nClient: Internet doesn't work\nAssistant: Try restarting"
res = generer_resume_ia(hist)
print("RESULT:")
print(res)
