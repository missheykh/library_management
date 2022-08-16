import pickle
import settings

# class BaseQuery:
#     file=None
#     def loadall(self):
#         db_file=open(self.__class__.file,'rb')
#         while True:
#             try:
#                 yield pickle.load(db_file)
#             except EOFError:
#                 break

#         db_file.close()

#     def get(self,unique_search_params,unique_data):
#         pass

#     def filter(self):
#         pass


# class QueryUsers(BaseQuery):
#     file=settings.USER_DATA_PATH/"users.db"


# class QueryBooks(BaseQuery):
#     file=settings.USER_DATA_PATH/"admins.db"



# the second soluthion by composition relation 

class BaseQuery:
    def __init__(self,file_path) -> None:
        self.file_path=file_path
        
    def loadall(self):
        db_file=open(self.file_path,'rb')
        while True:
            try:
                yield pickle.load(db_file)
            except EOFError:
                break

        db_file.close()

    def get(self,unique_search_params,unique_data):
        pass

    def filter(self):
        pass

    def exist(self,query_params,query_value):
        for elm in self.loadall():
            if getattr(elm,query_params)==query_value:
                return True
        return False