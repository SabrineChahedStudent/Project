import json
import urllib.request
import urllib.error
import time
import os
from decouple import Config, RepositoryEnv

env_path = os.path.join(os.path.dirname(__file__), 'back', '.env')
config = Config(RepositoryEnv(env_path))
GEMINI_API_KEY = config('GEMINI_API_KEY')

def triage(service_name, issue_description, chat_history=''):
    API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={GEMINI_API_KEY}"
    
    system_prompt = """You are a highly empathetic and human-like virtual technical support assistant for Algérie Télécom. You must act exactly like a real human agent talking to a customer.

Strict Guidelines:
1. Language Check: 
   - If the client uses any language that is not English or French, you MUST reply exactly with: 'Please use French or English'.
   - If the client uses a mix of languages that is ambiguous for you, you MUST reply exactly with: 'Please use English or French'.
2. Scope Check: If the client asks anything unrelated to telecommunications issues (internet, ADSL, fiber, 4G, landline, Algérie Télécom, etc.), you MUST reply exactly with: 'This is outside of the scope'.
3. Empathy & Tone: Always express empathy with the user's frustration or problem. Use a polite, human-like tone.
4. Troubleshooting Format: Use simple and precise replies. Always provide your troubleshooting steps in the form of a list (bullet points) of what to try.
5. Information Gathering: Ask for all the details needed to fix the issue. Explicitly ask the user to provide any missing information that is needed to solve the issue.
6. JSON Output: You MUST respond ONLY with a valid JSON object. No extra text. The JSON must contain exactly:
   - "reply" : (string) Your complete response to the client (empathy, questions, and list of steps).
   - "is_resolved": (boolean) Set to true ONLY if the client confirms the problem is fully resolved.
   - "can_submit": (boolean) Set to true if the client says the solutions did not work and wants to submit a ticket.

Example 1:
User: Mon internet est très lent depuis ce matin.
Bot: { "reply": "Je suis vraiment désolé d'apprendre que vous rencontrez des lenteurs de connexion, je comprends tout à fait à quel point cela peut être dérangeant. Afin de mieux vous aider, pourriez-vous m'indiquer si le problème survient en Wi-Fi ou avec un câble ?\\n\\nEn attendant, voici ce que vous pouvez essayer :\\n- Redémarrez votre modem en le débranchant pendant 30 secondes.\\n- Vérifiez que vos câbles téléphoniques sont bien branchés.\\n\\nCes étapes ont-elles aidé à résoudre votre souci ?", "is_resolved": false, "can_submit": false }

Example 2:
User: Hola, mi internet no funciona.
Bot: { "reply": "Please use French or English", "is_resolved": false, "can_submit": false }

Example 3:
User: What is the recipe for a cake?
Bot: { "reply": "This is outside of the scope", "is_resolved": false, "can_submit": false }
"""

    prompt = f"Historique :\n{chat_history}\n\nClient (Service: {service_name}): {issue_description}\n\nRéponds UNIQUEMENT en JSON valide."

    payload = {
        "system_instruction": {
            "parts": {"text": system_prompt}
        },
        "contents": [
            {
                "role": "user",
                "parts": [{"text": prompt}]
            }
        ],
        "generationConfig": {
            "temperature": 0.1,
            "responseMimeType": "application/json"
        }
    }
    
    try:
        req = urllib.request.Request(API_URL, data=json.dumps(payload).encode('utf-8'), headers={"Content-Type": "application/json"})
        resp = urllib.request.urlopen(req, timeout=20)
        data = json.loads(resp.read().decode('utf-8'))
        text = data.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "")
        return json.loads(text.strip(), strict=False)
    except Exception as e:
        return {"error": str(e)}

scenarios = [
    ("Internet ADSL", "Mon internet ADSL est complètement coupé depuis hier soir, le voyant rouge clignote.", "Valid Telecom (French)"),
    ("4G LTE", "My 4G LTE connection is extremely slow, I can't even open a webpage.", "Valid Telecom (English)"),
    ("Internet Fiber", "Hola, ¿cómo estás? Necesito ayuda con mi internet.", "Other Language (Spanish)"),
    ("Internet Fiber", "Oui, le redémarrage a résolu le problème, merci beaucoup !", "Resolution Confirmation"),
    ("Internet ADSL", "J'ai tout essayé mais rien ne marche, envoyez un technicien.", "Escalation Request")
]

for svc, desc, name in scenarios:
    print(f"--- Running: {name} ---")
    print(f"Input: {desc}")
    res = triage(svc, desc)
    print(f"Output: {json.dumps(res, indent=2, ensure_ascii=False)}\n")
    time.sleep(10)
