from .formats import (
    server_hello_format, server_certificate_format, server_key_exchange_format,
    server_hello_done_format
)


class ParsedResponse:
    def __init__(self, msg_bytes=b'', msg_struct=None):
        self.msg_bytes = msg_bytes
        self.msg_struct = msg_struct


class HelloResponseParser:
    def __init__(self, response=b''):
        self.response = response

    def parse(self):
        offset = 0
        self.server_hello, offset = self._parse_response_chunk(
            offset, server_hello_format
        )
        self.server_certificate, offset = self._parse_response_chunk(
            offset, server_certificate_format
        )
        self.server_key_exchange, offset = self._parse_response_chunk(
            offset, server_key_exchange_format
        )
        self.server_hello_done, offset = self._parse_response_chunk(
            offset, server_hello_done_format
        )
        print('Server Hello: \n{}\n\n'.format(self.server_hello.msg_struct))
        print('Server Certificate: \n{}\n\n'.format(self.server_certificate.msg_struct))
        print('Server Key Exchange: \n{}\n\n'.format(self.server_key_exchange.msg_struct))
        print('Server Hello Done: \n{}\n\n'.format(self.server_hello_done.msg_struct))
        return self

    def _parse_response_chunk(self, start_offset, format):
        msg_struct = format.parse(self.response[start_offset:])
        length = msg_struct.record_length + 5
        msg_bytes = self.response[start_offset:length]
        return ParsedResponse(msg_bytes, msg_struct), start_offset + length
