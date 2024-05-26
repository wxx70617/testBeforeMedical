
from algopy import *


class User(arc4.Struct):
    id: arc4.String
    name: arc4.String
    sex: arc4.String
    phone_number: arc4.String
    password: arc4.String
    address: arc4.String
    account_address: arc4.String
    mnemonic: arc4.String


class Register(ARC4Contract):
    @arc4.abimethod()
    def register(self, id: arc4.String,
                 name: arc4.String,
                 sex: arc4.String,
                 phone_number: arc4.String,
                 password: arc4.String,
                 address: arc4.String,
                 account_address: arc4.String,
                 mnemonic: arc4.String) -> String:

        user = User(id, name, sex, phone_number, password, address, account_address, mnemonic)

        success = op.Box.create(id.bytes, user.bytes.length)

        if success == False:
            return String("User registration failed because existed")
        else:
            op.Box.put(id.bytes, user.bytes)
            return String("User registration success")
