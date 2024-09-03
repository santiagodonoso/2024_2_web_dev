from bottle import get, run

##############################
@get("/")
def index():
    return "Santiago"



##############################
run(host="0.0.0.0", port=80, debug=True, reloader=True, interval=0.3)











