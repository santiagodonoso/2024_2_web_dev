from bottle import get, run, template, static_file, post, put, delete, response
import json

##############################
@get("/") # decorator
def index():
    return template("index")

##############################
@get("/about-us")
def _():
    return template("about_us")


##############################
@get("/app.css")
def _():
    return static_file("app.css", ".")

##############################
@get("/app.js")
def _():
    return static_file("app.js", ".")

# API
##############################
"""
CREATE READ UPDATE DELETE ALSO KNOWN AS THE CRUD

HTTP METHOD GET to READ data
/items

HTTP METHOD POST TO CREATE DATA
/items

HTTP METHOD PUT TO UPDATE DATA
/items/<id>

HTTP METHOD DELETE TO DELETE DATA
/items/<id>



"""

##############################
@get("/items")
def _():
    # list is an array
    item = {"id":1, "name":"a"}
    # convert list to string
    # type casting or cast
    # dumps stands for dump string
    response.content_type = "application/json"
    return json.dumps([item])

##############################
@get("/items/<id>")
def _(id):
    # dictionary
    item = {
        "id" : 1,
        "name" : "a"
    }
    return item

##############################
@post("/items")
def _():
    return "items created"

##############################
# f string
@put("/items/<id>")
def _(id):
    return f"item {id} updated"

##############################
@delete("/items/<id>")
def _(id):
    return f"item {id} deleted"

##############################
run(host="0.0.0.0", port=80, debug=True, reloader=True, interval=0.3)











