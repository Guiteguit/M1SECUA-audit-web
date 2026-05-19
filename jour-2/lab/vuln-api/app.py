from flask import Flask, request, jsonify, Response
import requests, base64, pickle
from lxml import etree
app = Flask(__name__)
@app.route("/")
def index():
    return """<h1>M1SECUA Vuln API - Jour 2</h1><ul><li>/health</li><li>/download?url=http://internal.target.local:8088</li><li>/xml - POST XML body</li><li>/deserialize?obj=BASE64_PICKLE</li></ul><p>Lab local uniquement.</p>"""
@app.route("/health")
def health():
    return jsonify({"status":"ok","lab":"jour2","scope":"local-only"})
@app.route("/download")
def download():
    url = request.args.get("url", "")
    if not url: return Response("Missing url parameter", status=400)
    try:
        r = requests.get(url, timeout=3)
        return Response(r.text[:5000], status=r.status_code, content_type=r.headers.get("content-type", "text/plain"))
    except Exception as e:
        return Response(f"Fetch error: {e}", status=502)
@app.route("/xml", methods=["POST"])
def xml_parser():
    data = request.data
    if not data: return Response("Missing XML body", status=400)
    try:
        parser = etree.XMLParser(resolve_entities=True, load_dtd=True, no_network=False)
        root = etree.fromstring(data, parser)
        return Response("Parsed XML content:\n"+"".join(root.itertext()), content_type="text/plain")
    except Exception as e:
        return Response(f"XML parse error: {e}", status=400)
@app.route("/deserialize")
def deserialize():
    obj = request.args.get("obj", "")
    if not obj: return Response("Missing obj parameter", status=400)
    try:
        result = pickle.loads(base64.b64decode(obj))
        return jsonify({"status":"deserialized","type":str(type(result)),"value":str(result)})
    except Exception as e:
        return Response(f"Deserialize error: {e}", status=400)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
