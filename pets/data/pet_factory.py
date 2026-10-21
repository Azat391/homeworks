import random,string

def create_data(id=None,suffix=None, status=None):
    if id is None:
        id=random.randint(1234567890123, 9999999999999)
    if suffix==None:
        suffix = 'Laich_'+''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
    if status==None:
        status = random.choice(["available", "pending", "sold"])
    return {
                "id": id,
                "name": suffix,
                "photoUrls": [],
                "status":status
                }