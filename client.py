class Client:
    def __init__(self, id=None, first_name=None, last_name=None, membership=None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.membership = membership

    def __str__(self):
        return (f'{self.id:<5}{self.first_name:<15}{self.last_name:<15}{self.membership:>10}')
