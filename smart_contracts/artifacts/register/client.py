# flake8: noqa
# fmt: off
# mypy: disable-error-code="no-any-return, no-untyped-call, misc, type-arg"
# This file was automatically generated by algokit-client-generator.
# DO NOT MODIFY IT BY HAND.
# requires: algokit-utils@^1.2.0
import base64
import dataclasses
import decimal
import typing
from abc import ABC, abstractmethod

import algokit_utils
import algosdk
from algosdk.v2client import models
from algosdk.atomic_transaction_composer import (
    AtomicTransactionComposer,
    AtomicTransactionResponse,
    SimulateAtomicTransactionResponse,
    TransactionSigner,
    TransactionWithSigner
)

_APP_SPEC_JSON = r"""{
    "hints": {
        "register(string,string,string,string,string,string,string,string)string": {
            "call_config": {
                "no_op": "CALL"
            }
        }
    },
    "source": {
        "approval": "I3ByYWdtYSB2ZXJzaW9uIDEwCgpzbWFydF9jb250cmFjdHMucmVnaXN0ZXIuY29udHJhY3QuUmVnaXN0ZXIuYXBwcm92YWxfcHJvZ3JhbToKICAgIC8vIHJlZ2lzdGVyL2NvbnRyYWN0LnB5OjE2CiAgICAvLyBjbGFzcyBSZWdpc3RlcihBUkM0Q29udHJhY3QpOgogICAgdHhuIE51bUFwcEFyZ3MKICAgIGJ6IG1haW5fYmFyZV9yb3V0aW5nQDUKICAgIG1ldGhvZCAicmVnaXN0ZXIoc3RyaW5nLHN0cmluZyxzdHJpbmcsc3RyaW5nLHN0cmluZyxzdHJpbmcsc3RyaW5nLHN0cmluZylzdHJpbmciCiAgICB0eG5hIEFwcGxpY2F0aW9uQXJncyAwCiAgICBtYXRjaCBtYWluX3JlZ2lzdGVyX3JvdXRlQDIKICAgIGVyciAvLyByZWplY3QgdHJhbnNhY3Rpb24KCm1haW5fcmVnaXN0ZXJfcm91dGVAMjoKICAgIC8vIHJlZ2lzdGVyL2NvbnRyYWN0LnB5OjE3CiAgICAvLyBAYXJjNC5hYmltZXRob2QoKQogICAgdHhuIE9uQ29tcGxldGlvbgogICAgIQogICAgYXNzZXJ0IC8vIE9uQ29tcGxldGlvbiBpcyBOb09wCiAgICB0eG4gQXBwbGljYXRpb25JRAogICAgYXNzZXJ0IC8vIGlzIG5vdCBjcmVhdGluZwogICAgLy8gcmVnaXN0ZXIvY29udHJhY3QucHk6MTYKICAgIC8vIGNsYXNzIFJlZ2lzdGVyKEFSQzRDb250cmFjdCk6CiAgICB0eG5hIEFwcGxpY2F0aW9uQXJncyAxCiAgICB0eG5hIEFwcGxpY2F0aW9uQXJncyAyCiAgICB0eG5hIEFwcGxpY2F0aW9uQXJncyAzCiAgICB0eG5hIEFwcGxpY2F0aW9uQXJncyA0CiAgICB0eG5hIEFwcGxpY2F0aW9uQXJncyA1CiAgICB0eG5hIEFwcGxpY2F0aW9uQXJncyA2CiAgICB0eG5hIEFwcGxpY2F0aW9uQXJncyA3CiAgICB0eG5hIEFwcGxpY2F0aW9uQXJncyA4CiAgICAvLyByZWdpc3Rlci9jb250cmFjdC5weToxNwogICAgLy8gQGFyYzQuYWJpbWV0aG9kKCkKICAgIGNhbGxzdWIgcmVnaXN0ZXIKICAgIGR1cAogICAgbGVuCiAgICBpdG9iCiAgICBleHRyYWN0IDYgMgogICAgc3dhcAogICAgY29uY2F0CiAgICBieXRlIDB4MTUxZjdjNzUKICAgIHN3YXAKICAgIGNvbmNhdAogICAgbG9nCiAgICBpbnQgMQogICAgcmV0dXJuCgptYWluX2JhcmVfcm91dGluZ0A1OgogICAgLy8gcmVnaXN0ZXIvY29udHJhY3QucHk6MTYKICAgIC8vIGNsYXNzIFJlZ2lzdGVyKEFSQzRDb250cmFjdCk6CiAgICB0eG4gT25Db21wbGV0aW9uCiAgICAhCiAgICBhc3NlcnQgLy8gcmVqZWN0IHRyYW5zYWN0aW9uCiAgICB0eG4gQXBwbGljYXRpb25JRAogICAgIQogICAgYXNzZXJ0IC8vIGlzIGNyZWF0aW5nCiAgICBpbnQgMQogICAgcmV0dXJuCgoKLy8gc21hcnRfY29udHJhY3RzLnJlZ2lzdGVyLmNvbnRyYWN0LlJlZ2lzdGVyLnJlZ2lzdGVyKGlkOiBieXRlcywgbmFtZTogYnl0ZXMsIHNleDogYnl0ZXMsIHBob25lX251bWJlcjogYnl0ZXMsIHBhc3N3b3JkOiBieXRlcywgYWRkcmVzczogYnl0ZXMsIGFjY291bnRfYWRkcmVzczogYnl0ZXMsIG1uZW1vbmljOiBieXRlcykgLT4gYnl0ZXM6CnJlZ2lzdGVyOgogICAgLy8gcmVnaXN0ZXIvY29udHJhY3QucHk6MTctMjUKICAgIC8vIEBhcmM0LmFiaW1ldGhvZCgpCiAgICAvLyBkZWYgcmVnaXN0ZXIoc2VsZiwgaWQ6IGFyYzQuU3RyaW5nLAogICAgLy8gICAgICAgICAgICAgIG5hbWU6IGFyYzQuU3RyaW5nLAogICAgLy8gICAgICAgICAgICAgIHNleDogYXJjNC5TdHJpbmcsCiAgICAvLyAgICAgICAgICAgICAgcGhvbmVfbnVtYmVyOiBhcmM0LlN0cmluZywKICAgIC8vICAgICAgICAgICAgICBwYXNzd29yZDogYXJjNC5TdHJpbmcsCiAgICAvLyAgICAgICAgICAgICAgYWRkcmVzczogYXJjNC5TdHJpbmcsCiAgICAvLyAgICAgICAgICAgICAgYWNjb3VudF9hZGRyZXNzOiBhcmM0LlN0cmluZywKICAgIC8vICAgICAgICAgICAgICBtbmVtb25pYzogYXJjNC5TdHJpbmcpIC0+IFN0cmluZzoKICAgIHByb3RvIDggMQogICAgLy8gcmVnaXN0ZXIvY29udHJhY3QucHk6MjcKICAgIC8vIHVzZXIgPSBVc2VyKGlkLCBuYW1lLCBzZXgsIHBob25lX251bWJlciwgcGFzc3dvcmQsIGFkZHJlc3MsIGFjY291bnRfYWRkcmVzcywgbW5lbW9uaWMpCiAgICBmcmFtZV9kaWcgLTgKICAgIGxlbgogICAgaW50IDE2CiAgICArCiAgICBkdXAKICAgIGl0b2IKICAgIGV4dHJhY3QgNiAyCiAgICBieXRlIDB4MDAxMAogICAgc3dhcAogICAgY29uY2F0CiAgICBzd2FwCiAgICBmcmFtZV9kaWcgLTcKICAgIGxlbgogICAgKwogICAgZHVwCiAgICBpdG9iCiAgICBleHRyYWN0IDYgMgogICAgdW5jb3ZlciAyCiAgICBzd2FwCiAgICBjb25jYXQKICAgIHN3YXAKICAgIGZyYW1lX2RpZyAtNgogICAgbGVuCiAgICArCiAgICBkdXAKICAgIGl0b2IKICAgIGV4dHJhY3QgNiAyCiAgICB1bmNvdmVyIDIKICAgIHN3YXAKICAgIGNvbmNhdAogICAgc3dhcAogICAgZnJhbWVfZGlnIC01CiAgICBsZW4KICAgICsKICAgIGR1cAogICAgaXRvYgogICAgZXh0cmFjdCA2IDIKICAgIHVuY292ZXIgMgogICAgc3dhcAogICAgY29uY2F0CiAgICBzd2FwCiAgICBmcmFtZV9kaWcgLTQKICAgIGxlbgogICAgKwogICAgZHVwCiAgICBpdG9iCiAgICBleHRyYWN0IDYgMgogICAgdW5jb3ZlciAyCiAgICBzd2FwCiAgICBjb25jYXQKICAgIHN3YXAKICAgIGZyYW1lX2RpZyAtMwogICAgbGVuCiAgICArCiAgICBkdXAKICAgIGl0b2IKICAgIGV4dHJhY3QgNiAyCiAgICB1bmNvdmVyIDIKICAgIHN3YXAKICAgIGNvbmNhdAogICAgc3dhcAogICAgZnJhbWVfZGlnIC0yCiAgICBsZW4KICAgICsKICAgIGl0b2IKICAgIGV4dHJhY3QgNiAyCiAgICBjb25jYXQKICAgIGZyYW1lX2RpZyAtOAogICAgY29uY2F0CiAgICBmcmFtZV9kaWcgLTcKICAgIGNvbmNhdAogICAgZnJhbWVfZGlnIC02CiAgICBjb25jYXQKICAgIGZyYW1lX2RpZyAtNQogICAgY29uY2F0CiAgICBmcmFtZV9kaWcgLTQKICAgIGNvbmNhdAogICAgZnJhbWVfZGlnIC0zCiAgICBjb25jYXQKICAgIGZyYW1lX2RpZyAtMgogICAgY29uY2F0CiAgICBmcmFtZV9kaWcgLTEKICAgIGNvbmNhdAogICAgZHVwCiAgICAvLyByZWdpc3Rlci9jb250cmFjdC5weToyOQogICAgLy8gc3VjY2VzcyA9IG9wLkJveC5jcmVhdGUoaWQuYnl0ZXMsIHVzZXIuYnl0ZXMubGVuZ3RoKQogICAgbGVuCiAgICBmcmFtZV9kaWcgLTgKICAgIHN3YXAKICAgIGJveF9jcmVhdGUKICAgIC8vIHJlZ2lzdGVyL2NvbnRyYWN0LnB5OjMwCiAgICAvLyBpZiBzdWNjZXNzID09IEZhbHNlOgogICAgYm56IHJlZ2lzdGVyX2Vsc2VfYm9keUAyCiAgICAvLyByZWdpc3Rlci9jb250cmFjdC5weTozMQogICAgLy8gcmV0dXJuIFN0cmluZygiVXNlciByZWdpc3RyYXRpb24gZmFpbGVkIGJlY2F1c2UgZXhpc3RlZCIpCiAgICBieXRlICJVc2VyIHJlZ2lzdHJhdGlvbiBmYWlsZWQgYmVjYXVzZSBleGlzdGVkIgogICAgc3dhcAogICAgcmV0c3ViCgpyZWdpc3Rlcl9lbHNlX2JvZHlAMjoKICAgIC8vIHJlZ2lzdGVyL2NvbnRyYWN0LnB5OjMzCiAgICAvLyBvcC5Cb3gucHV0KGlkLmJ5dGVzLCB1c2VyLmJ5dGVzKQogICAgZnJhbWVfZGlnIC04CiAgICBmcmFtZV9kaWcgMAogICAgYm94X3B1dAogICAgLy8gcmVnaXN0ZXIvY29udHJhY3QucHk6MzQKICAgIC8vIHJldHVybiBTdHJpbmcoIlVzZXIgcmVnaXN0cmF0aW9uIHN1Y2Nlc3MiKQogICAgYnl0ZSAiVXNlciByZWdpc3RyYXRpb24gc3VjY2VzcyIKICAgIHN3YXAKICAgIHJldHN1Ygo=",
        "clear": "I3ByYWdtYSB2ZXJzaW9uIDEwCgpzbWFydF9jb250cmFjdHMucmVnaXN0ZXIuY29udHJhY3QuUmVnaXN0ZXIuY2xlYXJfc3RhdGVfcHJvZ3JhbToKICAgIC8vIHJlZ2lzdGVyL2NvbnRyYWN0LnB5OjE2CiAgICAvLyBjbGFzcyBSZWdpc3RlcihBUkM0Q29udHJhY3QpOgogICAgaW50IDEKICAgIHJldHVybgo="
    },
    "state": {
        "global": {
            "num_byte_slices": 0,
            "num_uints": 0
        },
        "local": {
            "num_byte_slices": 0,
            "num_uints": 0
        }
    },
    "schema": {
        "global": {
            "declared": {},
            "reserved": {}
        },
        "local": {
            "declared": {},
            "reserved": {}
        }
    },
    "contract": {
        "name": "Register",
        "methods": [
            {
                "name": "register",
                "args": [
                    {
                        "type": "string",
                        "name": "id"
                    },
                    {
                        "type": "string",
                        "name": "name"
                    },
                    {
                        "type": "string",
                        "name": "sex"
                    },
                    {
                        "type": "string",
                        "name": "phone_number"
                    },
                    {
                        "type": "string",
                        "name": "password"
                    },
                    {
                        "type": "string",
                        "name": "address"
                    },
                    {
                        "type": "string",
                        "name": "account_address"
                    },
                    {
                        "type": "string",
                        "name": "mnemonic"
                    }
                ],
                "returns": {
                    "type": "string"
                }
            }
        ],
        "networks": {}
    },
    "bare_call_config": {
        "no_op": "CREATE"
    }
}"""
APP_SPEC = algokit_utils.ApplicationSpecification.from_json(_APP_SPEC_JSON)
_TReturn = typing.TypeVar("_TReturn")


class _ArgsBase(ABC, typing.Generic[_TReturn]):
    @staticmethod
    @abstractmethod
    def method() -> str:
        ...


_TArgs = typing.TypeVar("_TArgs", bound=_ArgsBase[typing.Any])


@dataclasses.dataclass(kw_only=True)
class _TArgsHolder(typing.Generic[_TArgs]):
    args: _TArgs


def _filter_none(value: dict | typing.Any) -> dict | typing.Any:
    if isinstance(value, dict):
        return {k: _filter_none(v) for k, v in value.items() if v is not None}
    return value


def _as_dict(data: typing.Any, *, convert_all: bool = True) -> dict[str, typing.Any]:
    if data is None:
        return {}
    if not dataclasses.is_dataclass(data):
        raise TypeError(f"{data} must be a dataclass")
    if convert_all:
        result = dataclasses.asdict(data)
    else:
        result = {f.name: getattr(data, f.name) for f in dataclasses.fields(data)}
    return _filter_none(result)


def _convert_transaction_parameters(
    transaction_parameters: algokit_utils.TransactionParameters | None,
) -> algokit_utils.TransactionParametersDict:
    return typing.cast(algokit_utils.TransactionParametersDict, _as_dict(transaction_parameters))


def _convert_call_transaction_parameters(
    transaction_parameters: algokit_utils.TransactionParameters | None,
) -> algokit_utils.OnCompleteCallParametersDict:
    return typing.cast(algokit_utils.OnCompleteCallParametersDict, _as_dict(transaction_parameters))


def _convert_create_transaction_parameters(
    transaction_parameters: algokit_utils.TransactionParameters | None,
    on_complete: algokit_utils.OnCompleteActionName,
) -> algokit_utils.CreateCallParametersDict:
    result = typing.cast(algokit_utils.CreateCallParametersDict, _as_dict(transaction_parameters))
    on_complete_enum = on_complete.replace("_", " ").title().replace(" ", "") + "OC"
    result["on_complete"] = getattr(algosdk.transaction.OnComplete, on_complete_enum)
    return result


def _convert_deploy_args(
    deploy_args: algokit_utils.DeployCallArgs | None,
) -> algokit_utils.ABICreateCallArgsDict | None:
    if deploy_args is None:
        return None

    deploy_args_dict = typing.cast(algokit_utils.ABICreateCallArgsDict, _as_dict(deploy_args))
    if isinstance(deploy_args, _TArgsHolder):
        deploy_args_dict["args"] = _as_dict(deploy_args.args)
        deploy_args_dict["method"] = deploy_args.args.method()

    return deploy_args_dict


@dataclasses.dataclass(kw_only=True)
class RegisterArgs(_ArgsBase[str]):
    id: str
    name: str
    sex: str
    phone_number: str
    password: str
    address: str
    account_address: str
    mnemonic: str

    @staticmethod
    def method() -> str:
        return "register(string,string,string,string,string,string,string,string)string"


@dataclasses.dataclass(kw_only=True)
class SimulateOptions:
    allow_more_logs: bool = dataclasses.field(default=False)
    allow_empty_signatures: bool = dataclasses.field(default=False)
    extra_opcode_budget: int = dataclasses.field(default=0)
    exec_trace_config: models.SimulateTraceConfig | None         = dataclasses.field(default=None)


class Composer:

    def __init__(self, app_client: algokit_utils.ApplicationClient, atc: AtomicTransactionComposer):
        self.app_client = app_client
        self.atc = atc

    def build(self) -> AtomicTransactionComposer:
        return self.atc

    def simulate(self, options: SimulateOptions | None = None) -> SimulateAtomicTransactionResponse:
        request = models.SimulateRequest(
            allow_more_logs=options.allow_more_logs,
            allow_empty_signatures=options.allow_empty_signatures,
            extra_opcode_budget=options.extra_opcode_budget,
            exec_trace_config=options.exec_trace_config,
            txn_groups=[]
        ) if options else None
        result = self.atc.simulate(self.app_client.algod_client, request)
        return result

    def execute(self) -> AtomicTransactionResponse:
        return self.app_client.execute_atc(self.atc)

    def register(
        self,
        *,
        id: str,
        name: str,
        sex: str,
        phone_number: str,
        password: str,
        address: str,
        account_address: str,
        mnemonic: str,
        transaction_parameters: algokit_utils.TransactionParameters | None = None,
    ) -> "Composer":
        """Adds a call to `register(string,string,string,string,string,string,string,string)string` ABI method
        
        :param str id: The `id` ABI parameter
        :param str name: The `name` ABI parameter
        :param str sex: The `sex` ABI parameter
        :param str phone_number: The `phone_number` ABI parameter
        :param str password: The `password` ABI parameter
        :param str address: The `address` ABI parameter
        :param str account_address: The `account_address` ABI parameter
        :param str mnemonic: The `mnemonic` ABI parameter
        :param algokit_utils.TransactionParameters transaction_parameters: (optional) Additional transaction parameters
        :returns Composer: This Composer instance"""

        args = RegisterArgs(
            id=id,
            name=name,
            sex=sex,
            phone_number=phone_number,
            password=password,
            address=address,
            account_address=account_address,
            mnemonic=mnemonic,
        )
        self.app_client.compose_call(
            self.atc,
            call_abi_method=args.method(),
            transaction_parameters=_convert_call_transaction_parameters(transaction_parameters),
            **_as_dict(args, convert_all=True),
        )
        return self

    def create_bare(
        self,
        *,
        on_complete: typing.Literal["no_op"] = "no_op",
        transaction_parameters: algokit_utils.CreateTransactionParameters | None = None,
    ) -> "Composer":
        """Adds a call to create an application using the no_op bare method
        
        :param typing.Literal[no_op] on_complete: On completion type to use
        :param algokit_utils.CreateTransactionParameters transaction_parameters: (optional) Additional transaction parameters
        :returns Composer: This Composer instance"""

        self.app_client.compose_create(
            self.atc,
            call_abi_method=False,
            transaction_parameters=_convert_create_transaction_parameters(transaction_parameters, on_complete),
        )
        return self

    def clear_state(
        self,
        transaction_parameters: algokit_utils.TransactionParameters | None = None,
        app_args: list[bytes] | None = None,
    ) -> "Composer":
        """Adds a call to the application with on completion set to ClearState
    
        :param algokit_utils.TransactionParameters transaction_parameters: (optional) Additional transaction parameters
        :param list[bytes] | None app_args: (optional) Application args to pass"""
    
        self.app_client.compose_clear_state(self.atc, _convert_transaction_parameters(transaction_parameters), app_args)
        return self


class RegisterClient:
    """A class for interacting with the Register app providing high productivity and
    strongly typed methods to deploy and call the app"""

    @typing.overload
    def __init__(
        self,
        algod_client: algosdk.v2client.algod.AlgodClient,
        *,
        app_id: int = 0,
        signer: TransactionSigner | algokit_utils.Account | None = None,
        sender: str | None = None,
        suggested_params: algosdk.transaction.SuggestedParams | None = None,
        template_values: algokit_utils.TemplateValueMapping | None = None,
        app_name: str | None = None,
    ) -> None:
        ...

    @typing.overload
    def __init__(
        self,
        algod_client: algosdk.v2client.algod.AlgodClient,
        *,
        creator: str | algokit_utils.Account,
        indexer_client: algosdk.v2client.indexer.IndexerClient | None = None,
        existing_deployments: algokit_utils.AppLookup | None = None,
        signer: TransactionSigner | algokit_utils.Account | None = None,
        sender: str | None = None,
        suggested_params: algosdk.transaction.SuggestedParams | None = None,
        template_values: algokit_utils.TemplateValueMapping | None = None,
        app_name: str | None = None,
    ) -> None:
        ...

    def __init__(
        self,
        algod_client: algosdk.v2client.algod.AlgodClient,
        *,
        creator: str | algokit_utils.Account | None = None,
        indexer_client: algosdk.v2client.indexer.IndexerClient | None = None,
        existing_deployments: algokit_utils.AppLookup | None = None,
        app_id: int = 0,
        signer: TransactionSigner | algokit_utils.Account | None = None,
        sender: str | None = None,
        suggested_params: algosdk.transaction.SuggestedParams | None = None,
        template_values: algokit_utils.TemplateValueMapping | None = None,
        app_name: str | None = None,
    ) -> None:
        """
        RegisterClient can be created with an app_id to interact with an existing application, alternatively
        it can be created with a creator and indexer_client specified to find existing applications by name and creator.
        
        :param AlgodClient algod_client: AlgoSDK algod client
        :param int app_id: The app_id of an existing application, to instead find the application by creator and name
        use the creator and indexer_client parameters
        :param str | Account creator: The address or Account of the app creator to resolve the app_id
        :param IndexerClient indexer_client: AlgoSDK indexer client, only required if deploying or finding app_id by
        creator and app name
        :param AppLookup existing_deployments:
        :param TransactionSigner | Account signer: Account or signer to use to sign transactions, if not specified and
        creator was passed as an Account will use that.
        :param str sender: Address to use as the sender for all transactions, will use the address associated with the
        signer if not specified.
        :param TemplateValueMapping template_values: Values to use for TMPL_* template variables, dictionary keys should
        *NOT* include the TMPL_ prefix
        :param str | None app_name: Name of application to use when deploying, defaults to name defined on the
        Application Specification
            """

        self.app_spec = APP_SPEC
        
        # calling full __init__ signature, so ignoring mypy warning about overloads
        self.app_client = algokit_utils.ApplicationClient(  # type: ignore[call-overload, misc]
            algod_client=algod_client,
            app_spec=self.app_spec,
            app_id=app_id,
            creator=creator,
            indexer_client=indexer_client,
            existing_deployments=existing_deployments,
            signer=signer,
            sender=sender,
            suggested_params=suggested_params,
            template_values=template_values,
            app_name=app_name,
        )

    @property
    def algod_client(self) -> algosdk.v2client.algod.AlgodClient:
        return self.app_client.algod_client

    @property
    def app_id(self) -> int:
        return self.app_client.app_id

    @app_id.setter
    def app_id(self, value: int) -> None:
        self.app_client.app_id = value

    @property
    def app_address(self) -> str:
        return self.app_client.app_address

    @property
    def sender(self) -> str | None:
        return self.app_client.sender

    @sender.setter
    def sender(self, value: str) -> None:
        self.app_client.sender = value

    @property
    def signer(self) -> TransactionSigner | None:
        return self.app_client.signer

    @signer.setter
    def signer(self, value: TransactionSigner) -> None:
        self.app_client.signer = value

    @property
    def suggested_params(self) -> algosdk.transaction.SuggestedParams | None:
        return self.app_client.suggested_params

    @suggested_params.setter
    def suggested_params(self, value: algosdk.transaction.SuggestedParams | None) -> None:
        self.app_client.suggested_params = value

    def register(
        self,
        *,
        id: str,
        name: str,
        sex: str,
        phone_number: str,
        password: str,
        address: str,
        account_address: str,
        mnemonic: str,
        transaction_parameters: algokit_utils.TransactionParameters | None = None,
    ) -> algokit_utils.ABITransactionResponse[str]:
        """Calls `register(string,string,string,string,string,string,string,string)string` ABI method
        
        :param str id: The `id` ABI parameter
        :param str name: The `name` ABI parameter
        :param str sex: The `sex` ABI parameter
        :param str phone_number: The `phone_number` ABI parameter
        :param str password: The `password` ABI parameter
        :param str address: The `address` ABI parameter
        :param str account_address: The `account_address` ABI parameter
        :param str mnemonic: The `mnemonic` ABI parameter
        :param algokit_utils.TransactionParameters transaction_parameters: (optional) Additional transaction parameters
        :returns algokit_utils.ABITransactionResponse[str]: The result of the transaction"""

        args = RegisterArgs(
            id=id,
            name=name,
            sex=sex,
            phone_number=phone_number,
            password=password,
            address=address,
            account_address=account_address,
            mnemonic=mnemonic,
        )
        result = self.app_client.call(
            call_abi_method=args.method(),
            transaction_parameters=_convert_call_transaction_parameters(transaction_parameters),
            **_as_dict(args, convert_all=True),
        )
        return result

    def create_bare(
        self,
        *,
        on_complete: typing.Literal["no_op"] = "no_op",
        transaction_parameters: algokit_utils.CreateTransactionParameters | None = None,
    ) -> algokit_utils.TransactionResponse:
        """Creates an application using the no_op bare method
        
        :param typing.Literal[no_op] on_complete: On completion type to use
        :param algokit_utils.CreateTransactionParameters transaction_parameters: (optional) Additional transaction parameters
        :returns algokit_utils.TransactionResponse: The result of the transaction"""

        result = self.app_client.create(
            call_abi_method=False,
            transaction_parameters=_convert_create_transaction_parameters(transaction_parameters, on_complete),
        )
        return result

    def clear_state(
        self,
        transaction_parameters: algokit_utils.TransactionParameters | None = None,
        app_args: list[bytes] | None = None,
    ) -> algokit_utils.TransactionResponse:
        """Calls the application with on completion set to ClearState
    
        :param algokit_utils.TransactionParameters transaction_parameters: (optional) Additional transaction parameters
        :param list[bytes] | None app_args: (optional) Application args to pass
        :returns algokit_utils.TransactionResponse: The result of the transaction"""
    
        return self.app_client.clear_state(_convert_transaction_parameters(transaction_parameters), app_args)

    def deploy(
        self,
        version: str | None = None,
        *,
        signer: TransactionSigner | None = None,
        sender: str | None = None,
        allow_update: bool | None = None,
        allow_delete: bool | None = None,
        on_update: algokit_utils.OnUpdate = algokit_utils.OnUpdate.Fail,
        on_schema_break: algokit_utils.OnSchemaBreak = algokit_utils.OnSchemaBreak.Fail,
        template_values: algokit_utils.TemplateValueMapping | None = None,
        create_args: algokit_utils.DeployCallArgs | None = None,
        update_args: algokit_utils.DeployCallArgs | None = None,
        delete_args: algokit_utils.DeployCallArgs | None = None,
    ) -> algokit_utils.DeployResponse:
        """Deploy an application and update client to reference it.
        
        Idempotently deploy (create, update/delete if changed) an app against the given name via the given creator
        account, including deploy-time template placeholder substitutions.
        To understand the architecture decisions behind this functionality please see
        <https://github.com/algorandfoundation/algokit-cli/blob/main/docs/architecture-decisions/2023-01-12_smart-contract-deployment.md>
        
        ```{note}
        If there is a breaking state schema change to an existing app (and `on_schema_break` is set to
        'ReplaceApp' the existing app will be deleted and re-created.
        ```
        
        ```{note}
        If there is an update (different TEAL code) to an existing app (and `on_update` is set to 'ReplaceApp')
        the existing app will be deleted and re-created.
        ```
        
        :param str version: version to use when creating or updating app, if None version will be auto incremented
        :param algosdk.atomic_transaction_composer.TransactionSigner signer: signer to use when deploying app
        , if None uses self.signer
        :param str sender: sender address to use when deploying app, if None uses self.sender
        :param bool allow_delete: Used to set the `TMPL_DELETABLE` template variable to conditionally control if an app
        can be deleted
        :param bool allow_update: Used to set the `TMPL_UPDATABLE` template variable to conditionally control if an app
        can be updated
        :param OnUpdate on_update: Determines what action to take if an application update is required
        :param OnSchemaBreak on_schema_break: Determines what action to take if an application schema requirements
        has increased beyond the current allocation
        :param dict[str, int|str|bytes] template_values: Values to use for `TMPL_*` template variables, dictionary keys
        should *NOT* include the TMPL_ prefix
        :param algokit_utils.DeployCallArgs | None create_args: Arguments used when creating an application
        :param algokit_utils.DeployCallArgs | None update_args: Arguments used when updating an application
        :param algokit_utils.DeployCallArgs | None delete_args: Arguments used when deleting an application
        :return DeployResponse: details action taken and relevant transactions
        :raises DeploymentError: If the deployment failed"""

        return self.app_client.deploy(
            version,
            signer=signer,
            sender=sender,
            allow_update=allow_update,
            allow_delete=allow_delete,
            on_update=on_update,
            on_schema_break=on_schema_break,
            template_values=template_values,
            create_args=_convert_deploy_args(create_args),
            update_args=_convert_deploy_args(update_args),
            delete_args=_convert_deploy_args(delete_args),
        )

    def compose(self, atc: AtomicTransactionComposer | None = None) -> Composer:
        return Composer(self.app_client, atc or AtomicTransactionComposer())
