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










