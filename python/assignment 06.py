class users:
    user_count=0
    def __init__(self,username):
        users.user_count +=1
        self.username=username
    
print(users.user_count)
my_instance=users("john deo")
print( my_instance.username)
sailee_instance=users("sailee mestry")
print( sailee_instance.username)
print(users.user_count) 