def application(environ, start_response):
    qs = environ['QUERY_STRING']
	#print(qs)
    ls = qs.split("&")
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return [ "\n".join(ls) ]
