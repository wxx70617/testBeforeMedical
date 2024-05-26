from algopy import *


class Authorization(ARC4Contract):
    @arc4.abimethod()
    def authorization_or_revoke(self, executor: arc4.String, executee: arc4.String,method: arc4.String) -> String:
        if method == "revoke":
            return revoke(executor, executee)
        elif method == "authorization":
            return authorization(executor, executee)
        else:
            return String("Invalid method")


@subroutine
def authorization(authorizer: arc4.String, authorized: arc4.String) -> String:
    success = op.Box.create(authorizer.bytes, 32768)
    authorization_list_bytes, existed = op.Box.get(authorizer.bytes)
    if existed == True:
        authorization_list = arc4.DynamicArray[arc4.String].from_bytes(authorization_list_bytes)
        authorization_list.append(authorized)
        new_authorization_list_bytes = authorization_list.bytes
        op.Box.replace(authorizer.bytes, 0, new_authorization_list_bytes)
        return String("Authorization success")
    else:
        return String("Authorization failure")


@subroutine
def revoke(revoker: arc4.String, revoked: arc4.String) -> String:
    authorization_list_bytes, existed = op.Box.get(revoker.bytes)
    if existed == True:
        authorization_list = arc4.DynamicArray[arc4.String].from_bytes(authorization_list_bytes)
        new_authorization_list = arc4.DynamicArray[arc4.String]()
        for address in authorization_list:
            if address != revoked:
                new_authorization_list.append(address)
        new_authorization_list_bytes = new_authorization_list.bytes
        op.Box.replace(revoker.bytes, 0, new_authorization_list_bytes)
        return String("Revoke Authorization success")
    else:
        return String("Revoce Authorization failure")
