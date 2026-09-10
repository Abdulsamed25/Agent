import os
import re
import urllib.parse

keywords = (
  "gmail", "email","e-mail","draft an email","compose an email","mail","write an email","send email","draft mail","compose mail"
)
def is_email_command(text):
  text = text.lower()
  return any (k in text for k in keywords)

def extract_email(text):
  match = re.search(r"[\w.+-]+@[\w.-]+\.\w+",text)
  if match:
    return match.group(0) 

  match = re.search(
      r"([\w.+-]+)\s+at\s+([\w.-]+)\s+dot\s+(\w+)"'
    text.lower()
  )
  if match:
    return f"{match.group(1)}@{match.group(2)}.{match.group(3)}"


def create_gmail_url(subject="",body="",recipient=""):
  params=urllib.parse.urlencode({
    "view":"cm"
    "fs":"1",
    "to":recipient,
    "su":subject,
    "body":body
  })
  return f"https://mail.google.com/mail/u/0/?{params}"

