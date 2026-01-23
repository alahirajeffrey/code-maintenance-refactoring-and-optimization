class UserService:
    def __init__(self, repository):
        self.repository = repository

    def list_users(self):
        return self.repository.get_all()

    def get_user_by_id(self, user_id):
        user = self.repository.get_by_id(user_id)
        if user:
            return user
        return None
