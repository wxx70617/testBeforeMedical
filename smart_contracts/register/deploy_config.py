import logging

import algokit_utils
from algosdk.v2client.algod import AlgodClient
from algosdk.v2client.indexer import IndexerClient
from .User import User
logger = logging.getLogger(__name__)


# define deployment behaviour based on supplied app spec
def deploy(
    algod_client: AlgodClient,
    indexer_client: IndexerClient,
    app_spec: algokit_utils.ApplicationSpecification,
    deployer: algokit_utils.Account,
) -> None:

    from smart_contracts.artifacts.register.client import (
    RegisterClient,
    )

    app_client = RegisterClient(
        algod_client,
        creator=deployer,
        indexer_client=indexer_client,
    )

    app_client.deploy(
        on_schema_break=algokit_utils.OnSchemaBreak.AppendApp,
        on_update=algokit_utils.OnUpdate.AppendApp,
    )
    name = "wxx test register"
    id = "230000199999993333"
    sex = "male"

    phone_number = "18366688588"
    password = "password"
    address = "address"
    mnemonic = "mnemonic"
    #user = User(id,name,sex,phone_number,password, address, mnemonic)
    #response = app_client.register(id=id,name=name,sex=sex,phone_number=phone_number,password = password,address = address,mnemonic = mnemonic)
    #response = app_client.register(name=name)
    # logger.info(
    #     f"Called register on {app_spec.contract.name} ({app_client.app_id}) "
    #     f"with user={user.name}, received: {response.return_value}"
    # )
    # print(user.name)
    # #print(response.return_value)
