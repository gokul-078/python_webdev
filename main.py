# import fastapi
from fastapi import FastAPI
from typing import Optional
import uvicorn  

# To run the application
app = FastAPI()

# Simple api call
@app.get("/")
def abc():
    return "hello"

# Dynamic route
@app.get("/about/{id}")
def about(id):
    return { "blog": id}

# Here, it will show error because above path also have the same path and the first one expecting int so it shows error python runs in a line by line so it happens.
# Suppose if we don't give 'int' conditionally then it should looks for other paths below and then run
# So in python we should always gives the static routes at first and dynamic routes at last. If we give this route above the dynamic route the above one it should run properly
@app.get("/about/unpublish")   
def unpublish():
    return "unpublished blogs"

@app.get("/about/{id}/comments")
def comments(id: int):
    return {"comments": id}

# query params
# query params also should be written in the function params, we can also write in route path but it should be hardcoded eg:- "/blog?limit"
@app.get("/blog")
def blog(limit):                                         # Here, the 'limit' is the query params, Even for query params also we can set data type 'limit : int'
    return {"blog": f'{limit} blogs are published'}

# query params with data type
# If we expect the query params and if it is not giving in the url then the route should not run shows error at default the query params all are required.
@app.get("/blog/d")
def blogd(limit: int, published):
    return {"Limited blog with type expecting": f'{limit} blogs are published - {published}'}

# query params with data type
@app.get("/blog/data")
def blogdata(limit: int, published: bool):
    if(published):
        return {"blog": f'Published {limit} blog posts'}
    else:
        return {"blog": f'{limit} blog posts are not published'}
    
# default values and optional with the query params and data type
# params with default values. Eg:- params = default_value
# params with data type and default value. Eg:- params: data_type = default_value
# params with optional and data type values. Eg:- params: Optional[data_type] = default_value
@app.get("/blog/default")
def blogdefault(limit: int = 100, published: bool = True, sort: Optional[str] = None): 
    if(published):
        return {"blog": f'Published {limit} blog posts'}
    elif(sort == "latest"):
        return {"blog": f'This are the {sort} posts'}
    else:
        return {"blog": f'{limit} blog posts are not published'}
    






# To run our application on different port number we have to define it in the main file and run the file in terminal like python3 file_name.py. Eg:- python3 main.py
# if __name__ == "__main__" :
#     uvicorn.run(app, host = "127.0.0.1", port=3033)
