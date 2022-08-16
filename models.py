import uuid
import pickle
import settings
from db import BaseQuery

class MetaBase(type):
    def __init__(self,*args,**kwargs):
        self.query=BaseQuery(self.file_path)
        super().__init__(*args,**kwargs)


class BaseUser(metaclass=MetaBase):
    type=None
    db=None
    file_path=None
    def __init__(self,username,password) -> None:
        self.username=username
        self.id=self._generate_id()
        self.password=self._set_password(password)

    @staticmethod
    def _generate_id():
        return str(uuid.uuid4())

    @staticmethod
    def _set_password(pasw):
        return hash(pasw)

    def save(self):
        try:
            with open(settings.USER_DATA_PATH/self.db,'ab') as db_flie:
                pickle.dump(self,db_flie)
        except Exception as e:
            print(e)


class Admin(BaseUser):
    type="admin"
    db="admins.db"
    file_path=settings.BASE_DIR/"users_data"/db
    
    def add_user(self):
      pass


class Member(BaseUser):
    type="member"
    db="users.db"
    file_path=settings.BASE_DIR/"users_data"/db


#Book Medel    
class BaseBook(metaclass=MetaBase):
    db=None
    file_path=None
    def __init__(self,name,author) -> None:
        self.name=name
        self.id=self._generate_id()
        self.author=author

    @staticmethod
    def _generate_id():
        return str(uuid.uuid4())

    def save(self):
        try:
            with open(settings.BOOKS_DATA_PATH/self.db,'ab') as db_flie:
                pickle.dump(self,db_flie)
        except Exception as e:
            print(e)


class Book(BaseBook):
    db="books.db"
    file_path=settings.BASE_DIR/"books_data"/db