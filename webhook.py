from flask Import Flask, request

app = Flask(__name__)

@app.route("/", methods=["POST"])
def handle_webhook():
	data = request.json
	print("Neue Newsletter-Anmeldung: ", data)
	return " ", 200