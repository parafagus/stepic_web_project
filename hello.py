"""
start
"""

def application(environ, start_response):
    status = "200 OK"
    headers = [("Content-Type", "text/plain")]
    start_response(status, headers)
    #body = "\n".join(environ["QUERY_STRING"].split("&"))
	body = environ['QUERY_STRING'].replace('&', '\n')
    return body
