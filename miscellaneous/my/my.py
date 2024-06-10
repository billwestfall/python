class My:
    def __init__(self, code):
        self.code = code
        self.line_nr = 0
        self.token_feed = self.tokens()
        self.returned_token = None

    def raise_error(self, message):
        raise ValueError(f'{self.line_nr}: {message}')

    def tokens(self):
        for line in self.code.strip().split('\n'):
            self.line_nr += 1
            for token in line.strip().split(' '):
                if token == 'print':
                    yield (token,)
                elif token.isnumeric():
                    yield ('number', int(token))
                else:
                    self.raise_error(f'Syntax Error: Invalid token {token}')
            yield ('\n',)
            
    def next_token(self):
        if self.returned_token:
            token = self.returned_token
            self.returned_token = None
        else:
            try:
                token = next(self.token_feed)
            except StopIteration:
                token = None
        return token

    def return_token(self, token):
        if self.returned_token is not None:
            raise RuntimeError('Cannot return more than one token at a time')
        self.returned_token = token

    def parse_program(self):
        if not self.parse_statement():
            self.raise_error('Expected: statement')
        token = self.next_token()
        while token is not None:
            self.return_token(token)
            if not self.parse_statement():
               self.raise_error('Expected: statement')
            token = self.next_token()
        return True

    def parse_statement(self):
        if not self.parse_print_statement():
            self.raise_error('Expected: print statement')
        token = self.next_token()
        if token[0] != '\n':
            self.raise_error('Expected: end of line')
        return True