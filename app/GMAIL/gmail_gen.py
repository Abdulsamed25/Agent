import os
import json
import re
import time
import random
import urllib.request
import urllib.error

 API_KEY = os.getenv("GEMINI_API_KEY","")
MODEL = os.getnev("GEMINI_MODEL","gemini-3.5-flash")

def generate_email_with_gemini(command):
  if not API_KEY:
    raise RuntimeError("GEMINI_API_KEY is missing.")

prompt = f"""

You are a professional gmail email writing assistant.

convert the user's voice command into a professional email.

RULES:
-Do not copy the command literally
-Do not explain anything.
-Do not invent names , dates, prices,companies,attachments,or facts.
-keep the email natural and concise.
-include an appropriate greeting and closing

Output exactly:

SUBJECT:<subject>

BODY:
<email body>

User command:
{command}
"""

   url=(
      f"https://generativelanguage.googleapis.com/"
      f"v1beta/models/{MODEL}:generatecontent"
   )

payload={
 "contents":[{"parts":[{"text":prompt}]}],
 "generationConfig":{
    "temperature":0.7,
    "maxoutputtokens":800
 }
}
req = urllib.request.Request(
     url,
     data=json.dumps(payload).encode(),
     header={
     "Content-Type": "application/json",
     "x-goog-api-key": API_KEY
     },
     methods="post"
)
for attempt in range(4):
 try:
  with urllib.request.urlopen(req,timeout=30) as response:
   data = json.loads(response.read().decode())

text = data["candidates"][0]["content"]["part"][0]["text"]
text = re.sub(r"'''(?:text)?|'''","",text).strip()

subject = re.search(r"SUBJECT:\S*(.+)",text,re.I)
body = re.search(r"body:\s*([\s\S]+)",text,re.I)

if not subject or not body:
 raise RuntimeError("Gemini returned an invalid email format.")

return{
   "subject":subject.group(1).strip(),
}

except urllib.error.httperror as e:
   if e.code != 429 or attempt == 3:
    try:
     detail = e.read().decode()
    except Exception:
     detail = str(e)
    raise RuntimeError(f"Gemini API error:{detail}")
    
    
time.sleep((2**attempt)+random.random())

except Exception:
   if attempt == 3:



                     













