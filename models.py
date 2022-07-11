import uuid
class BaseUser:
    type=None
    def __init__(self,username,password) -> None:
        self.username=username
        self.id=self._generate_id()
        self.password=self._set_password(password)

    def _generate_id(self):
        return uuid.uuid4()

    def _set_password(pasw):
        return hash(pasw)

    def save(self):
        pass

class Admin(BaseUser):
    type="admin"
    
    def save(self):
        pass

class Member(BaseUser):
    type="member"

    def save(self):
        pass
    