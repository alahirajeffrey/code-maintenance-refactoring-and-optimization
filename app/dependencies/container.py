from app.services.user import UserService
from app.repositories.user import FakeUserRepository


class Container:
    def __init__(self):
        self._repo = FakeUserRepository()

    def init_app(self, app):
        pass

    def user_service(self):
        return UserService(self._repo)


container = Container()
