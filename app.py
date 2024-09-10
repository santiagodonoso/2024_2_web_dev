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
        response.status = ex.args[1]
        return {
            "error":"yes",
            "message":ex.args[0]
        }
    finally:
        pass

##############################
@post("/signup")
def _():
    try:
        user_name = x.validate_user_name()
        return {"error":"no", "user_id":"1"}
    except Exception as ex:
        if len(ex.args) >= 2: # own created exception
            response.status = ex.args[1]
            return {"error":True, "message":ex.args[0]}
        else: # python exception, not under our control
            response.status = 500   
            return {"error":True, "message":ex.args[0]}
    finally:
        pass


##############################
application = default_app()


"""
    try:
        db = x.db()
        q = db.execute("SELECT * FROM items ORDER BY item_created_at LIMIT 0, ?", (x.ITEMS_PER_PAGE,))
        items = q.fetchall()
        ic(items)
        is_logged = False
        try:    
            x.validate_user_logged()
            is_logged = True
        except:
            pass

        return template("index.html", items=items, mapbox_token=credentials.mapbox_token, 
                        is_logged=is_logged)
    except Exception as ex:
        ic(ex)
        return ex
    finally:
        if "db" in locals(): db.close()
"""
