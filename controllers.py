from models import Member

def SignUp(_username,_password):
    if Member.query.exist("username",_username):
     raise Exception("this user already exists")
    member_obj=Member(username=_username,password=_password)
    member_obj.save()
    raise("you registerd successfully")


