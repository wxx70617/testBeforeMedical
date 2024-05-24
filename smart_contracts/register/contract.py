from algopy import *


class User(arc4.Struct):
    id: arc4.String
    name: arc4.String
    sex: arc4.String
    phone_number: arc4.String
    password: arc4.String
    address: arc4.String
    mnemonic:arc4.String

class Register(ARC4Contract):
    @arc4.abimethod()
    def register(self, users: arc4.DynamicArray[User],user:User) -> arc4.String:
        users_bytes_len = users.bytes.length

        if op.Box.create(b"users",users_bytes_len):
            users_list_Bytes , existed = op.Box.get(b"users")
            if existed:
                users_list = arc4.DynamicArray[User].from_bytes(users_list_Bytes)
                users_list.append(user.copy())
                users_list_bytes = users_list.bytes
                op.Box.put(b"users",users_list_bytes)
        return arc4.String("ok")
