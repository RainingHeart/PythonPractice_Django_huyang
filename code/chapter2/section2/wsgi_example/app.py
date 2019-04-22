# coding:utf-8


def simple_app(environ, start_response):
    """Simplest possible application object"""
    status = '200 OK'
    response_headers = [('Content-Type', 'text/plain')]
    start_response(status, response_headers)
    return [b'Hello world! -by the5fire \n']


class AppClass(object):
    status = '200 OK'
    response_headers = [('Content-Type', 'text/plain')]

    def __call__(self, environ, start_response):
        print(environ, start_response)
        start_response(self.status, self.response_headers)
        return [b'Hello Appclass.__call__\n']


class AppClassIter(object):
    status = '200 OK'
    response_headers = [('Content-Type', 'text/plain')]

    def __init__(self, environ, start_response):
        self.environ = environ
        self.start_response = start_response

    def __iter__(self):
        self.start_response(self.status, self.response_headers)
        yield b'Hello AppClassIter\n'

