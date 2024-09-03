from bottle import get, run, template

##############################
@get("/") # decorator
def index():
    return template("index")



##############################
run(host="0.0.0.0", port=80, debug=True, reloader=True, interval=0.3)











