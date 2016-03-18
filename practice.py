from BaseHTTPServer import BaseHTTPRequestHandler
import urlparse

class GetHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        parsed_path=urlparse.urlparse(self.path)
        message_parts=[
            'Client Values:',
            'client_address=%s (%s)' %(self.client_address, self.address_string()),
            'command=%s' %self.command,
            'path=%s' %self.path,
            'real path=%s' %parsed_path.path,
            'query=%s' %parsed_path.query,
            'request version=%s' %self.request_version,
            '',
            'Server Values:',
            'server version=%s' %self.server_version,
            'sys_version=%s' %self.sys_version,
            'protocol_version=%s' %self.protocol_version,
            '',
            'HEADERS RECIEVED',
        ]

        """message_parts=[
            '<a href="http://www.naver.com">Naver</a>',
            '<a href="http://www.google.com">Google</a>',
            '<a href="http://www.gachon.ac.kr">Gachon</a>'
        ]"""

        for name, value in sorted(self.headers.items()):
            message_parts.append('%s-%s' %(name, value.rstrip()))
            message='\r\n'.join(message_parts)
            self.send_response(200)
            self.end_headers()
            self.wfile.write(message)
            return


if __name__=='__main__':
    from BaseHTTPServer import HTTPServer
    server=HTTPServer(('localhost', 8080), GetHandler)
    print 'Starting server'
    server.serve_forever()