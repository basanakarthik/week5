
class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []
        self.max_books = 5

    def to_dict(self):
        return self.__dict__

    @classmethod
    def from_dict(cls, data):
        member = cls(data['name'], data['member_id'])
        member.borrowed_books = data['borrowed_books']
        return member
