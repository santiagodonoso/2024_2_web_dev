from bottle import get, run, template, static_file

##############################
@get("/") # decorator
def index():
    return template("index")

##############################
@get("/app.css")
def _():
    return static_file("app.css", ".")



##############################
run(host="0.0.0.0", port=80, debug=True, reloader=True, interval=0.3)











