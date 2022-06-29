def two_fer(name='you'):
    return ('One for ' + name + ', one for me.')

##improved version 1
def two_fer(name='you'):
    return 'One for {}, one for me.'.format(name)
