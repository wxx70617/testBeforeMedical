import algopy
from algopy import *

class StoreInfo(arc4.Struct):
    uploader_id: arc4.String
    patient_id: arc4.String
    file_id: arc4.String
    file_address: arc4.String

class HelloWorld(ARC4Contract):
    @arc4.abimethod()
    def hello(self,uploader_id: arc4.String,patient_id: arc4.String,file_id:arc4.String,file_address:arc4.String) -> String:
        lists = arc4.DynamicArray[StoreInfo]()
        contents1 = arc4.String.from_bytes(lists.bytes)
        # name_byte_length = name.bytes.length
        # name_bytes = name.bytes
        length1 = lists.bytes.length
        store_info1 = StoreInfo(uploader_id,patient_id,file_id,file_address)
        file_address2 = arc4.String("QmcRD4wkPPi6dig81r5sLj9Zm1gDCL4zgpEj9CfuRrGwxx")
        store_info2 = StoreInfo(uploader_id,patient_id,file_id,file_address2)
        length3 = store_info1.bytes.length
        lists.append(store_info1.copy())
        lists.append(store_info2.copy())
        #item = lists.pop()
        # lists.append(name)
        # lists.append(name)
        #success = op.Box.create(id.bytes,200)
        # user = User(id)
        # contents2 = lists[0]
        # #contents2 = arc4.String.from_bytes(lists.bytes)
        results = String()
        i = UInt64(0)
        while i <= lists.length:
             results = String(",").join((lists[i].file_address.native,results))
        length2 = lists.bytes.length
        #return user.id.native
        return results


