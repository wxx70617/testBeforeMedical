from algopy import *
from smart_contracts.authorization.contract import check_authorization


class StoreInfo(arc4.Struct):
    uploader_id: arc4.String
    patient_id: arc4.String
    file_id: arc4.String
    file_address: arc4.String


class Upload(ARC4Contract):
    @arc4.abimethod()
    def record_file(self, uploader_id:arc4.String, patient_id:arc4.String, file_id:arc4.String, file_address:arc4.String) -> String:
        return String("OK")


@subroutine
def upload(uploader_id: arc4.String, patient_id: arc4.String, file_id: arc4.String, file_address: arc4.String) -> String:
    
    store_info = StoreInfo(uploader_id,patient_id, file_id, file_address)

    success = op.Box.create(file_id.bytes,store_info.bytes.length)
    if success == True:
        op.Box.put(file_id.bytes,store_info.bytes)
    return String("upload success")


@subroutine
def search(searcher_id:arc4.String, patient_id:arc4.String) -> String:
    authorization = check_authorization(searcher_id, patient_id)
    if authorization == "No Authorisation":
        return String("No Authorisation")
    else:
        return String("null")
