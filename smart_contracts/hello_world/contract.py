import algopy
from algopy import *

class User(arc4.Struct):
    id : arc4.String

class HelloWorld(ARC4Contract):
    @arc4.abimethod()
    def hello(self,name: arc4.String,id: arc4.String) -> String:
        lists = arc4.DynamicArray[arc4.String]()
        contents1 = arc4.String.from_bytes(lists.bytes)
        name_byte_length = name.bytes.length
        name_bytes = name.bytes
        length1 = lists.bytes.length
        lists.append(name)
        lists.append(name)
        lists.append(name)
        #success = op.Box.create(id.bytes,200)
        user = User(id)
        contents2 = lists[0]
        #contents2 = arc4.String.from_bytes(lists.bytes)
        results = String()
        for item in lists:
            results = String(",").join((item.native,results))
        length2 = lists.bytes.length
        return user.id.native
