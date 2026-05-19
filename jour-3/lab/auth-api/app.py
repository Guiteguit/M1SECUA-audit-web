from flask import Flask, request, jsonify, redirect, make_response
import base64, json, hmac, hashlib, time, secrets

app = Flask(__name__)

USERS = {
    "alice": {"id": 1, "username": "alice", "password": "alice123", "role": "user", "email": "alice@target.local", "balance": 1000},
    "bob": {"id": 2, "username": "bob", "password": "bob123", "role": "user", "email": "bob@target.local", "balance": 750},
    "admin": {"id": 3, "username": "admin", "password": "admin123", "role": "admin", "email": "admin@target.local", "balance": 9999},
}
SESSIONS = {}
JWT_SECRET = b"m1secua-secret-faible"

def b64url(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode()

def b64url_decode(data: str) -> bytes:
    pad = "=" * (-len(data) % 4)
    return base64.urlsafe_b64decode(data + pad)

def sign(header_b64, payload_b64):
    msg = f"{header_b64}.{payload_b64}".encode()
    return b64url(hmac.new(JWT_SECRET, msg, hashlib.sha256).digest())

def make_jwt(user, alg="HS256"):
    header = {"typ": "JWT", "alg": alg}
    payload = {"sub": str(user["id"]), "username": user["username"], "role": user["role"], "iat": int(time.time())}
    h = b64url(json.dumps(header, separators=(",", ":")).encode())
    p = b64url(json.dumps(payload, separators=(",", ":")).encode())
    if alg == "none":
        return f"{h}.{p}."
    return f"{h}.{p}.{sign(h,p)}"

def verify_jwt(token):
    h, p, s = token.split(".")
    header = json.loads(b64url_decode(h))
    payload = json.loads(b64url_decode(p))
    # Vulnérabilité volontaire : alg=none accepté.
    if header.get("alg") == "none":
        return payload
    if header.get("alg") == "HS256" and hmac.compare_digest(s, sign(h, p)):
        return payload
    raise ValueError("invalid token")

@app.route("/")
def index():
    return """
    <h1>M1SECUA Auth API - Jour 3</h1>
    <p>Lab local authentification / autorisation.</p>
    <ul>
      <li>POST /login</li>
      <li>GET /me</li>
      <li>GET /api/users/&lt;id&gt;/profile</li>
      <li>POST /api/user/edit</li>
      <li>POST /transfer</li>
      <li>POST /jwt-login</li>
      <li>GET /api/jwt/me</li>
      <li>GET /api/jwt/admin</li>
      <li>GET /oauth/authorize</li>
    </ul>
    """

@app.route("/health")
def health():
    return jsonify({"status": "ok", "lab": "jour3"})

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username", "")
    password = request.form.get("password", "")
    user = USERS.get(username)
    if not user or user["password"] != password:
        return jsonify({"status": "error", "message": "invalid credentials"}), 401
    sid = secrets.token_hex(8)
    SESSIONS[sid] = username
    resp = make_response(jsonify({"status": "ok", "message": "logged in", "user": username}))
    # Vulnérabilité pédagogique : pas de Secure, SameSite faible/non défini selon contexte.
    resp.set_cookie("LABSESSID", sid, httponly=True)
    return resp

def current_user():
    sid = request.cookies.get("LABSESSID")
    username = SESSIONS.get(sid)
    return USERS.get(username) if username else None

@app.route("/me")
def me():
    u = current_user()
    if not u:
        return jsonify({"error": "not authenticated"}), 401
    return jsonify({"id": u["id"], "username": u["username"], "role": u["role"], "email": u["email"], "balance": u["balance"]})

@app.route("/transfer", methods=["POST"])
def transfer():
    # Vulnérabilité pédagogique : action sensible sans token CSRF.
    u = current_user()
    if not u:
        return jsonify({"error": "not authenticated"}), 401
    to = request.form.get("to", "")
    amount = int(request.form.get("amount", "0"))
    u["balance"] -= amount
    return jsonify({"status": "transfer_done", "from": u["username"], "to": to, "amount": amount, "new_balance": u["balance"]})

@app.route("/api/users/<int:uid>/profile")
def profile(uid):
    # Vulnérabilité pédagogique : IDOR, pas de vérification que uid == current_user.id.
    for u in USERS.values():
        if u["id"] == uid:
            return jsonify({"id": u["id"], "username": u["username"], "email": u["email"], "role": u["role"]})
    return jsonify({"error": "not found"}), 404

@app.route("/api/user/edit", methods=["POST"])
def edit_user():
    # Vulnérabilité pédagogique : mass assignment / privilege escalation.
    u = current_user()
    if not u:
        return jsonify({"error": "not authenticated"}), 401
    new_email = request.form.get("email")
    new_role = request.form.get("role")
    if new_email:
        u["email"] = new_email
    if new_role:
        u["role"] = new_role
    return jsonify({"status": "updated", "user": {"username": u["username"], "email": u["email"], "role": u["role"]}})

@app.route("/jwt-login", methods=["POST"])
def jwt_login():
    username = request.form.get("username", "")
    password = request.form.get("password", "")
    user = USERS.get(username)
    if not user or user["password"] != password:
        return jsonify({"error": "invalid credentials"}), 401
    return jsonify({"token": make_jwt(user)})

@app.route("/api/jwt/me")
def jwt_me():
    auth = request.headers.get("Authorization", "")
    token = auth.replace("Bearer ", "")
    try:
        payload = verify_jwt(token)
        return jsonify({"status": "ok", "payload": payload})
    except Exception as e:
        return jsonify({"error": str(e)}), 401

@app.route("/api/jwt/admin")
def jwt_admin():
    auth = request.headers.get("Authorization", "")
    token = auth.replace("Bearer ", "")
    try:
        payload = verify_jwt(token)
        if payload.get("role") == "admin":
            return jsonify({"status": "admin_access_granted", "flag": "JWT_ADMIN_BYPASS_OK"})
        return jsonify({"error": "admin required"}), 403
    except Exception as e:
        return jsonify({"error": str(e)}), 401

@app.route("/oauth/authorize")
def oauth_authorize():
    # Vulnérabilité pédagogique : redirect_uri non validée et state optionnel.
    client_id = request.args.get("client_id", "")
    redirect_uri = request.args.get("redirect_uri", "")
    state = request.args.get("state")
    code = "lab-auth-code-12345"
    if not redirect_uri:
        return jsonify({"error": "missing redirect_uri"}), 400
    separator = "&" if "?" in redirect_uri else "?"
    target = f"{redirect_uri}{separator}code={code}"
    if state:
        target += f"&state={state}"
    return redirect(target, code=302)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
