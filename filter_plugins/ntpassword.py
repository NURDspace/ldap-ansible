from ansible import errors
import hashlib

def ntpassword(password):
    return hashlib.new('md4', password.encode('utf-16le')).digest().encode('hex').upper()

class FilterModule(object):
    ''' A filter to produce md4 Samba compatible passwords. '''
    def filters(self):
        return {
            'ntpassword': ntpassword
        }
