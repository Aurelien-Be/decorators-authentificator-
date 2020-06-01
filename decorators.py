user1 = {'name': 'sonia',

         'valid': False}

user2 = {'name': 'Delphine',

         'valid': True}


def authenticated(fn):
    def wrappers(*args, **kwargs):
        if args[0]['valid']:
            return fn(*args, **kwargs)
        else:
            print('request invalid')
    return(wrappers)  # code here


@authenticated
def message_friends(user):
    print('message has been sent')


message_friends(user1)
message_friends(user2)
