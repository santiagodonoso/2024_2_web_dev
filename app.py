from bottle import default_app, get, post, response
import x


# docker compose up --build
##############################
@get("/")
def _():
    return "x"

##############################
@post("/login")
def _():
    try:
        # Validate the data from the client
        user_email = x.validate_user_email()        
        user_password = x.validate_user_password()    
        return {
            "error":"no",
            "message":""
        }
    except Exception as ex:
        print("#"*30)
        print(ex.args[0])
        print(ex.args[1])
        response.status = ex.args[1]
        return {
            "error":"yes",
            "message":ex.args[0]
        }
    finally:
        pass

##############################
application = default_app()



