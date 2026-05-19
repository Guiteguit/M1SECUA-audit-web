from flask import Flask, request, jsonify
import sqlite3
import subprocess
import pickle
import base64
import yaml
import hashlib

app = Flask(__name__)

# Vulnérabilité volontaire : secret hardcodé
API_KEY = "SuperSecret123"
ADMIN_PASSWORD = "admin"

def get_db():
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE users(id INTEGER, username TEXT, password TEXT)")
    conn.execute("INSERT INTO users VALUES(1, 'alice', 'alice123')")
    conn.execute("INSERT INTO users VALUES(2, 'bob', 'bob123')")
    conn.execute("INSERT INTO users VALUES(3, 'admin', 'admin123')")
    return conn

@app.route("/health")
def health():
    return jsonify({"status": "ok", "lab": "jour4", "app": "python"})

@app.route("/search")
def search():
    username = request.args.get("username", "")
    db = get_db()
    # Vulnérabilité volontaire : SQL injection
    query = "SELECT id, username FROM users WHERE username = '" + username + "'"
    rows = db.execute(query).fetchall()
    return jsonify({"query": query, "results": rows})

@app.route("/ping")
def ping():
    host = request.args.get("host", "127.0.0.1")
    # Vulnérabilité volontaire : shell=True avec entrée utilisateur
    result = subprocess.check_output("ping -c 1 " + host, shell=True, timeout=3)
    return result

@app.route("/deserialize")
def deserialize():
    obj = request.args.get("obj", "")
    # Vulnérabilité volontaire : pickle.loads sur donnée utilisateur
    data = pickle.loads(base64.b64decode(obj))
    return jsonify({"data": str(data)})

@app.route("/yaml", methods=["POST"])
def yaml_load():
    # Vulnérabilité volontaire : yaml.load sans SafeLoader
    data = yaml.load(request.data, Loader=yaml.Loader)
    return jsonify({"parsed": str(data)})

@app.route("/hash")
def weak_hash():
    value = request.args.get("value", "password")
    # Vulnérabilité volontaire : MD5 pour un usage sensible
    return jsonify({"md5": hashlib.md5(value.encode()).hexdigest()})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
