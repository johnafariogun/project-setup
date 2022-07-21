from uuid import uuid4



def generates_random_id(length = 6):
    random_id = str(uuid4())
    return random_id[:length]