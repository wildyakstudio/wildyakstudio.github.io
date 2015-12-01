#!/usr/bin/env python

from livereload import Server, shell

server = Server()

server.watch("style.css")
server.watch("index.html")

server.serve(port=8080, host="localhost", open_url=True)
