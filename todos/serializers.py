class TodoSerializer:
    def __init__(self, todo):
        self.todo = todo

    def parse(self):
        return {
            'title': self.todo.title,
            'body': self.todo.body,
        }
