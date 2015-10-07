#!/usr/bin python3

def application(environ, start_response):
	start_response('200 OK' , [('Content-Type', 'text/html')])
	return [b'<h1>Hello,Web!</h1>']


