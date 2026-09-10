import os

from flask_cors import cors

from app.gmail import(
  is_email_command,
  extract_email,
  create_gmail_url,
  generate_email_with_gemini)

from app.youtube import youtube_bp

def create.app():
   app = Flask(__name__)
   cors(app)

   app.register_blueprint(
       youtube_bp,
       url_prefix="/youtube"
   )
@app.route("/html")
def html():
    return render_template("index.html")


@app.route("/health")
def health():
    return jsonify({
        "status":"ok",
        "service":"Nova AI Agent"
    })

@app.route("/agent",method=["post"])
def agent():
  try:
    data = request.get_json(silent=true) or {}
    command = data.get("command","").strip()
    if not command:
      return jsonify({
        "success": false,
        "message":"command is required"
      }),400

    if not is_email_command(command):
      return jsonify({
        "success": False,
        "message":"please give a gmail commands."
      }),400

recipient = extract_email(command)

email=generate_email_with_gemini(command)

return jsonify({
  "success": True,
  "type":"email"
  "email_generated": True,
  "recipient":recipient,
  "subject":email["body"],
  "gmail_url":create_gmail_url(
    email["subject"],
    email["body"],
    recipient
  )
})

except Exception as e:
     return jsonify({
       "success": False,
       "message": str(e)
     }),500

return app





    












        









