##########################################################
# Web Server
# Mohammad Mahdavi
# moh.mahdavi.l@gmail.com
# March 2016
# All Rights Reserved
##########################################################


##########################################################
import flask
##########################################################


##########################################################
app = flask.Flask(__name__)
@app.route("/Application/", methods=["GET", "POST"])
def applicationFunction():
	text = flask.request.values.get("value")
	print text
	result = "This is the response."
	return result

app.run(host = "0.0.0.0", debug=True, port=8001)
##########################################################