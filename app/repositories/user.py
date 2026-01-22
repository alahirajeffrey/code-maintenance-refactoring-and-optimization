class FakeUserRepository:
    def __init__(self):
        self._users = [
            {"id": 1, "first_name": "John", "last_name": "Shinggu"},
            {"id": 2, "first_name": "Shinggu", "last_name": "John"},
        ]

    def get_all(self):
        return self._users

    def get_by_id(self, user_id):
        return next(
            (user for user in self._users if user["id"] == user_id),
            None,
        )
