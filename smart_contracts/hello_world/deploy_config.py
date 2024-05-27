import logging

import algokit_utils
from algosdk.v2client.algod import AlgodClient
from algosdk.v2client.indexer import IndexerClient

logger = logging.getLogger(__name__)


# define deployment behaviour based on supplied app spec
def deploy(
    algod_client: AlgodClient,
    indexer_client: IndexerClient,
    app_spec: algokit_utils.ApplicationSpecification,
    deployer: algokit_utils.Account,
) -> None:
    from smart_contracts.artifacts.hello_world.client import (
        HelloWorldClient,
    )


    app_client = HelloWorldClient(
        algod_client,
        creator=deployer,
        indexer_client=indexer_client,
    )

    app_client.deploy(
        on_schema_break=algokit_utils.OnSchemaBreak.AppendApp,
        on_update=algokit_utils.OnUpdate.AppendApp,
    )
    uploader_id = "IF7ZNVFYFWQDZ6VVJDBXZE7XV2OQDSV72QS5U7ZXXU5AS5TEOXAU5ERMEE"
    patient_id = "IF7ZNVFYFWQDZ6VVJDBXZE7XV2OQDSV72QS5U7ZXXU5AS5TEOXAU5ERMEE"
    file_id = "QmcRD4wkPPi6dig81r5sLj9Zm1gDCL4zgpEj9CfuRrGbzF"
    file_address = "QmcRD4wkPPi6dig81r5sLj9Zm1gDCL4zgpEj9CfuRrGbzF"
    name = "world"
    #print(len(name.encode('utf-8')))
    response = app_client.hello(uploader_id=uploader_id, patient_id=patient_id, file_id=file_id, file_address=file_address)

    if response.return_value is "":
        print("empty string response")
    else:
        print(response.return_value)
    logger.info(
        f"Called hello on {app_spec.contract.name} ({app_client.app_id}) "
        f"with name={name}, received: {response.return_value}"
    )


