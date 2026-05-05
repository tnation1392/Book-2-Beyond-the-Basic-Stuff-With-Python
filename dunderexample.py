class Ticket:
    def __init__(self, id, status):
        self.id = id
        self.status = status

    def __repr__(self):
        return f"Ticket(id={self.id!r}, status={self.status!r})"

    def __str__(self):
        return f"Ticket #{self.id} ({self.status})"


t = Ticket(123, "OPEN")
t            # Ticket(id=123, status='OPEN')   (in REPL)
print(t)     # Ticket #123 (OPEN)