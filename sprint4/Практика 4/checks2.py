def division_on_zero(a,b):
    return a/b
def get_user_by_id(id):
    users={998:'Huesos', 1:'Mike'}
    return users[id]
def set_new_password(password):
    if len(password)<8:
        raise ValueError('Пароль слишком короткий')
    
