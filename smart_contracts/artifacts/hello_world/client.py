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
        "hello(string,string,string,string)string": {
            "call_config": {
                "no_op": "CALL"
            }
        }
    },
    "source": {
        "approval": "I3ByYWdtYSB2ZXJzaW9uIDEwCgpzbWFydF9jb250cmFjdHMuaGVsbG9fd29ybGQuY29udHJhY3QuSGVsbG9Xb3JsZC5hcHByb3ZhbF9wcm9ncmFtOgogICAgLy8gaGVsbG9fd29ybGQvY29udHJhY3QucHk6MTAKICAgIC8vIGNsYXNzIEhlbGxvV29ybGQoQVJDNENvbnRyYWN0KToKICAgIHR4biBOdW1BcHBBcmdzCiAgICBieiBtYWluX2JhcmVfcm91dGluZ0A1CiAgICBtZXRob2QgImhlbGxvKHN0cmluZyxzdHJpbmcsc3RyaW5nLHN0cmluZylzdHJpbmciCiAgICB0eG5hIEFwcGxpY2F0aW9uQXJncyAwCiAgICBtYXRjaCBtYWluX2hlbGxvX3JvdXRlQDIKICAgIGVyciAvLyByZWplY3QgdHJhbnNhY3Rpb24KCm1haW5faGVsbG9fcm91dGVAMjoKICAgIC8vIGhlbGxvX3dvcmxkL2NvbnRyYWN0LnB5OjExCiAgICAvLyBAYXJjNC5hYmltZXRob2QoKQogICAgdHhuIE9uQ29tcGxldGlvbgogICAgIQogICAgYXNzZXJ0IC8vIE9uQ29tcGxldGlvbiBpcyBOb09wCiAgICB0eG4gQXBwbGljYXRpb25JRAogICAgYXNzZXJ0IC8vIGlzIG5vdCBjcmVhdGluZwogICAgLy8gaGVsbG9fd29ybGQvY29udHJhY3QucHk6MTAKICAgIC8vIGNsYXNzIEhlbGxvV29ybGQoQVJDNENvbnRyYWN0KToKICAgIHR4bmEgQXBwbGljYXRpb25BcmdzIDEKICAgIHR4bmEgQXBwbGljYXRpb25BcmdzIDIKICAgIHR4bmEgQXBwbGljYXRpb25BcmdzIDMKICAgIHR4bmEgQXBwbGljYXRpb25BcmdzIDQKICAgIC8vIGhlbGxvX3dvcmxkL2NvbnRyYWN0LnB5OjExCiAgICAvLyBAYXJjNC5hYmltZXRob2QoKQogICAgY2FsbHN1YiBoZWxsbwogICAgZHVwCiAgICBsZW4KICAgIGl0b2IKICAgIGV4dHJhY3QgNiAyCiAgICBzd2FwCiAgICBjb25jYXQKICAgIGJ5dGUgMHgxNTFmN2M3NQogICAgc3dhcAogICAgY29uY2F0CiAgICBsb2cKICAgIGludCAxCiAgICByZXR1cm4KCm1haW5fYmFyZV9yb3V0aW5nQDU6CiAgICAvLyBoZWxsb193b3JsZC9jb250cmFjdC5weToxMAogICAgLy8gY2xhc3MgSGVsbG9Xb3JsZChBUkM0Q29udHJhY3QpOgogICAgdHhuIE9uQ29tcGxldGlvbgogICAgIQogICAgYXNzZXJ0IC8vIHJlamVjdCB0cmFuc2FjdGlvbgogICAgdHhuIEFwcGxpY2F0aW9uSUQKICAgICEKICAgIGFzc2VydCAvLyBpcyBjcmVhdGluZwogICAgaW50IDEKICAgIHJldHVybgoKCi8vIHNtYXJ0X2NvbnRyYWN0cy5oZWxsb193b3JsZC5jb250cmFjdC5IZWxsb1dvcmxkLmhlbGxvKHVwbG9hZGVyX2lkOiBieXRlcywgcGF0aWVudF9pZDogYnl0ZXMsIGZpbGVfaWQ6IGJ5dGVzLCBmaWxlX2FkZHJlc3M6IGJ5dGVzKSAtPiBieXRlczoKaGVsbG86CiAgICAvLyBoZWxsb193b3JsZC9jb250cmFjdC5weToxMS0xMgogICAgLy8gQGFyYzQuYWJpbWV0aG9kKCkKICAgIC8vIGRlZiBoZWxsbyhzZWxmLHVwbG9hZGVyX2lkOiBhcmM0LlN0cmluZyxwYXRpZW50X2lkOiBhcmM0LlN0cmluZyxmaWxlX2lkOmFyYzQuU3RyaW5nLGZpbGVfYWRkcmVzczphcmM0LlN0cmluZykgLT4gU3RyaW5nOgogICAgcHJvdG8gNCAxCiAgICAvLyBoZWxsb193b3JsZC9jb250cmFjdC5weToxOAogICAgLy8gc3RvcmVfaW5mbzEgPSBTdG9yZUluZm8odXBsb2FkZXJfaWQscGF0aWVudF9pZCxmaWxlX2lkLGZpbGVfYWRkcmVzcykKICAgIGZyYW1lX2RpZyAtNAogICAgbGVuCiAgICBpbnQgOAogICAgKwogICAgZHVwCiAgICBpdG9iCiAgICBleHRyYWN0IDYgMgogICAgYnl0ZSAweDAwMDgKICAgIHN3YXAKICAgIGNvbmNhdAogICAgc3dhcAogICAgZnJhbWVfZGlnIC0zCiAgICBsZW4KICAgICsKICAgIGR1cAogICAgaXRvYgogICAgZXh0cmFjdCA2IDIKICAgIHVuY292ZXIgMgogICAgc3dhcAogICAgY29uY2F0CiAgICBzd2FwCiAgICBmcmFtZV9kaWcgLTIKICAgIGxlbgogICAgKwogICAgaXRvYgogICAgZXh0cmFjdCA2IDIKICAgIGNvbmNhdAogICAgZnJhbWVfZGlnIC00CiAgICBjb25jYXQKICAgIGZyYW1lX2RpZyAtMwogICAgY29uY2F0CiAgICBmcmFtZV9kaWcgLTIKICAgIGNvbmNhdAogICAgZHVwCiAgICBmcmFtZV9kaWcgLTEKICAgIGNvbmNhdAogICAgc3dhcAogICAgLy8gaGVsbG9fd29ybGQvY29udHJhY3QucHk6MTkKICAgIC8vIGZpbGVfYWRkcmVzczIgPSBhcmM0LlN0cmluZygiUW1jUkQ0d2tQUGk2ZGlnODFyNXNMajlabTFnRENMNHpncEVqOUNmdVJyR3d4eCIpCiAgICBieXRlICJceDAwLlFtY1JENHdrUFBpNmRpZzgxcjVzTGo5Wm0xZ0RDTDR6Z3BFajlDZnVSckd3eHgiCiAgICAvLyBoZWxsb193b3JsZC9jb250cmFjdC5weToyMAogICAgLy8gc3RvcmVfaW5mbzIgPSBTdG9yZUluZm8odXBsb2FkZXJfaWQscGF0aWVudF9pZCxmaWxlX2lkLGZpbGVfYWRkcmVzczIpCiAgICBjb25jYXQKICAgIHN3YXAKICAgIC8vIGhlbGxvX3dvcmxkL2NvbnRyYWN0LnB5OjEzCiAgICAvLyBsaXN0cyA9IGFyYzQuRHluYW1pY0FycmF5W1N0b3JlSW5mb10oKQogICAgYnl0ZSAweDAwMDAKICAgIC8vIGhlbGxvX3dvcmxkL2NvbnRyYWN0LnB5OjIyCiAgICAvLyBsaXN0cy5hcHBlbmQoc3RvcmVfaW5mbzEuY29weSgpKQogICAgc3dhcAogICAgaW50IDEKICAgIGNhbGxzdWIgZHluYW1pY19hcnJheV9jb25jYXRfdmFyaWFibGVfc2l6ZQogICAgLy8gaGVsbG9fd29ybGQvY29udHJhY3QucHk6MjMKICAgIC8vIGxpc3RzLmFwcGVuZChzdG9yZV9pbmZvMi5jb3B5KCkpCiAgICBzd2FwCiAgICBpbnQgMQogICAgY2FsbHN1YiBkeW5hbWljX2FycmF5X2NvbmNhdF92YXJpYWJsZV9zaXplCiAgICAvLyBoZWxsb193b3JsZC9jb250cmFjdC5weToyNC0zMQogICAgLy8gI2l0ZW0gPSBsaXN0cy5wb3AoKQogICAgLy8gIyBsaXN0cy5hcHBlbmQobmFtZSkKICAgIC8vICMgbGlzdHMuYXBwZW5kKG5hbWUpCiAgICAvLyAjc3VjY2VzcyA9IG9wLkJveC5jcmVhdGUoaWQuYnl0ZXMsMjAwKQogICAgLy8gIyB1c2VyID0gVXNlcihpZCkKICAgIC8vICMgY29udGVudHMyID0gbGlzdHNbMF0KICAgIC8vICMgI2NvbnRlbnRzMiA9IGFyYzQuU3RyaW5nLmZyb21fYnl0ZXMobGlzdHMuYnl0ZXMpCiAgICAvLyByZXN1bHRzID0gU3RyaW5nKCkKICAgIGJ5dGUgIiIKCmhlbGxvX3doaWxlX3RvcEAxOgogICAgLy8gaGVsbG9fd29ybGQvY29udHJhY3QucHk6MzQKICAgIC8vIHJlc3VsdHMgPSBTdHJpbmcoIiwiKS5qb2luKChsaXN0c1tpXS5maWxlX2FkZHJlc3MubmF0aXZlLHJlc3VsdHMpKQogICAgZnJhbWVfZGlnIDAKICAgIGR1cAogICAgaW50IDAKICAgIGV4dHJhY3RfdWludDE2CiAgICBhc3NlcnQgLy8gSW5kZXggYWNjZXNzIGlzIG91dCBvZiBib3VuZHMKICAgIGV4dHJhY3QgMiAwCiAgICBkdXAKICAgIGludCAwCiAgICBleHRyYWN0X3VpbnQxNgogICAgZHVwMgogICAgZXh0cmFjdF91aW50MTYKICAgIGludCAyCiAgICArCiAgICBleHRyYWN0MwogICAgZHVwCiAgICBpbnQgNgogICAgZXh0cmFjdF91aW50MTYKICAgIGR1cDIKICAgIGV4dHJhY3RfdWludDE2CiAgICBpbnQgMgogICAgKwogICAgZXh0cmFjdDMKICAgIGV4dHJhY3QgMiAwCiAgICBieXRlICIsIgogICAgY29uY2F0CiAgICBzd2FwCiAgICBjb25jYXQKICAgIGIgaGVsbG9fd2hpbGVfdG9wQDEKCgovLyBhbGdvcHlfbGliX2FyYzQuZHluYW1pY19hcnJheV9jb25jYXRfdmFyaWFibGVfc2l6ZShzb3VyY2U6IGJ5dGVzLCBuZXdfaXRlbXNfYnl0ZXM6IGJ5dGVzLCBuZXdfaXRlbXNfY291bnQ6IHVpbnQ2NCkgLT4gYnl0ZXM6CmR5bmFtaWNfYXJyYXlfY29uY2F0X3ZhcmlhYmxlX3NpemU6CiAgICAvLyA8YWxnb3B5Pi9hbGdvcHlfbGliX2FyYzQucHk6MTY2LTE2OQogICAgcHJvdG8gMyAxCiAgICAvLyA8YWxnb3B5Pi9hbGdvcHlfbGliX2FyYzQucHk6MTc5CiAgICBmcmFtZV9kaWcgLTMKICAgIGludCAwCiAgICBleHRyYWN0X3VpbnQxNgogICAgLy8gPGFsZ29weT4vYWxnb3B5X2xpYl9hcmM0LnB5OjE4MAogICAgZHVwCiAgICBmcmFtZV9kaWcgLTEKICAgICsKICAgIHN3YXAKICAgIC8vIDxhbGdvcHk+L2FsZ29weV9saWJfYXJjNC5weToxODEKICAgIGludCAyCiAgICAqCiAgICBpbnQgMgogICAgKwogICAgc3dhcAogICAgLy8gPGFsZ29weT4vYWxnb3B5X2xpYl9hcmM0LnB5OjE4MwogICAgZHVwCiAgICBpdG9iCiAgICBleHRyYWN0IDYgMAogICAgc3dhcAogICAgLy8gPGFsZ29weT4vYWxnb3B5X2xpYl9hcmM0LnB5OjE4NQogICAgZnJhbWVfZGlnIC0zCiAgICBpbnQgMgogICAgZGlnIDQKICAgIHN1YnN0cmluZzMKICAgIC8vIDxhbGdvcHk+L2FsZ29weV9saWJfYXJjNC5weToxODYKICAgIGZyYW1lX2RpZyAtMQogICAgaW50IDIKICAgICoKICAgIGJ6ZXJvCiAgICAvLyA8YWxnb3B5Pi9hbGdvcHlfbGliX2FyYzQucHk6MTg1LTE4NgogICAgY29uY2F0CiAgICAvLyA8YWxnb3B5Pi9hbGdvcHlfbGliX2FyYzQucHk6MTg3CiAgICBmcmFtZV9kaWcgLTMKICAgIGxlbgogICAgZnJhbWVfZGlnIC0zCiAgICB1bmNvdmVyIDUKICAgIHVuY292ZXIgMgogICAgc3Vic3RyaW5nMwogICAgLy8gPGFsZ29weT4vYWxnb3B5X2xpYl9hcmM0LnB5OjE4NS0xODcKICAgIGNvbmNhdAogICAgLy8gPGFsZ29weT4vYWxnb3B5X2xpYl9hcmM0LnB5OjE4NS0xODgKICAgIGZyYW1lX2RpZyAtMgogICAgY29uY2F0CiAgICAvLyA8YWxnb3B5Pi9hbGdvcHlfbGliX2FyYzQucHk6MTgzLTE5MgogICAgc3dhcAogICAgLy8gPGFsZ29weT4vYWxnb3B5X2xpYl9hcmM0LnB5OjE5MQogICAgaW50IDAKICAgIC8vIDxhbGdvcHk+L2FsZ29weV9saWJfYXJjNC5weToxODMtMTkyCiAgICBjYWxsc3ViIHJlY2FsY3VsYXRlX2FycmF5X29mZnNldHNfc3RhdGljCiAgICBjb25jYXQKICAgIHJldHN1YgoKCi8vIGFsZ29weV9saWJfYXJjNC5yZWNhbGN1bGF0ZV9hcnJheV9vZmZzZXRzX3N0YXRpYyhhcnJheV9kYXRhOiBieXRlcywgbGVuZ3RoOiB1aW50NjQsIHN0YXJ0X2F0X2luZGV4OiB1aW50NjQpIC0+IGJ5dGVzOgpyZWNhbGN1bGF0ZV9hcnJheV9vZmZzZXRzX3N0YXRpYzoKICAgIC8vIDxhbGdvcHk+L2FsZ29weV9saWJfYXJjNC5weToxOTUtMTk4CiAgICBwcm90byAzIDEKICAgIGJ5dGUgIiIKICAgIGR1cAogICAgLy8gPGFsZ29weT4vYWxnb3B5X2xpYl9hcmM0LnB5OjIwOQogICAgZnJhbWVfZGlnIC0xCiAgICBpbnQgMgogICAgKgogICAgLy8gPGFsZ29weT4vYWxnb3B5X2xpYl9hcmM0LnB5OjIxMAogICAgZnJhbWVfZGlnIC0xCiAgICBibnogcmVjYWxjdWxhdGVfYXJyYXlfb2Zmc2V0c19zdGF0aWNfZWxzZV9ib2R5QDIKICAgIC8vIDxhbGdvcHk+L2FsZ29weV9saWJfYXJjNC5weToyMTEKICAgIGZyYW1lX2RpZyAtMgogICAgaW50IDIKICAgICoKICAgIGZyYW1lX2J1cnkgMQogICAgYiByZWNhbGN1bGF0ZV9hcnJheV9vZmZzZXRzX3N0YXRpY19hZnRlcl9pZl9lbHNlQDMKCnJlY2FsY3VsYXRlX2FycmF5X29mZnNldHNfc3RhdGljX2Vsc2VfYm9keUAyOgogICAgLy8gPGFsZ29weT4vYWxnb3B5X2xpYl9hcmM0LnB5OjIxMwogICAgZnJhbWVfZGlnIC0zCiAgICBmcmFtZV9kaWcgMgogICAgZXh0cmFjdF91aW50MTYKICAgIGZyYW1lX2J1cnkgMQoKcmVjYWxjdWxhdGVfYXJyYXlfb2Zmc2V0c19zdGF0aWNfYWZ0ZXJfaWZfZWxzZUAzOgogICAgZnJhbWVfZGlnIC0xCiAgICBmcmFtZV9idXJ5IDAKCnJlY2FsY3VsYXRlX2FycmF5X29mZnNldHNfc3RhdGljX2Zvcl9oZWFkZXJANDoKICAgIC8vIDxhbGdvcHk+L2FsZ29weV9saWJfYXJjNC5weToyMTUKICAgIGZyYW1lX2RpZyAwCiAgICBmcmFtZV9kaWcgLTIKICAgIDwKICAgIGJ6IHJlY2FsY3VsYXRlX2FycmF5X29mZnNldHNfc3RhdGljX2FmdGVyX2ZvckA4CiAgICAvLyA8YWxnb3B5Pi9hbGdvcHlfbGliX2FyYzQucHk6MjE2CiAgICBmcmFtZV9kaWcgMQogICAgZHVwCiAgICBpdG9iCiAgICBleHRyYWN0IDYgMAogICAgLy8gPGFsZ29weT4vYWxnb3B5X2xpYl9hcmM0LnB5OjIxNwogICAgZnJhbWVfZGlnIC0zCiAgICBmcmFtZV9kaWcgMgogICAgZHVwCiAgICBjb3ZlciA0CiAgICB1bmNvdmVyIDIKICAgIHJlcGxhY2UzCiAgICBkdXAKICAgIGZyYW1lX2J1cnkgLTMKICAgIC8vIDxhbGdvcHk+L2FsZ29weV9saWJfYXJjNC5weToyMTgKICAgIGRpZyAxCiAgICBleHRyYWN0X3VpbnQxNgogICAgaW50IDIKICAgICsKICAgICsKICAgIGZyYW1lX2J1cnkgMQogICAgLy8gPGFsZ29weT4vYWxnb3B5X2xpYl9hcmM0LnB5OjIxOQogICAgaW50IDIKICAgICsKICAgIGZyYW1lX2J1cnkgMgogICAgLy8gPGFsZ29weT4vYWxnb3B5X2xpYl9hcmM0LnB5OjIxNQogICAgZnJhbWVfZGlnIDAKICAgIGludCAxCiAgICArCiAgICBmcmFtZV9idXJ5IDAKICAgIGIgcmVjYWxjdWxhdGVfYXJyYXlfb2Zmc2V0c19zdGF0aWNfZm9yX2hlYWRlckA0CgpyZWNhbGN1bGF0ZV9hcnJheV9vZmZzZXRzX3N0YXRpY19hZnRlcl9mb3JAODoKICAgIC8vIDxhbGdvcHk+L2FsZ29weV9saWJfYXJjNC5weToyMjEKICAgIGZyYW1lX2RpZyAtMwogICAgZnJhbWVfYnVyeSAwCiAgICByZXRzdWIK",
        "clear": "I3ByYWdtYSB2ZXJzaW9uIDEwCgpzbWFydF9jb250cmFjdHMuaGVsbG9fd29ybGQuY29udHJhY3QuSGVsbG9Xb3JsZC5jbGVhcl9zdGF0ZV9wcm9ncmFtOgogICAgLy8gaGVsbG9fd29ybGQvY29udHJhY3QucHk6MTAKICAgIC8vIGNsYXNzIEhlbGxvV29ybGQoQVJDNENvbnRyYWN0KToKICAgIGludCAxCiAgICByZXR1cm4K"
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
        "name": "HelloWorld",
        "methods": [
            {
                "name": "hello",
                "args": [
                    {
                        "type": "string",
                        "name": "uploader_id"
                    },
                    {
                        "type": "string",
                        "name": "patient_id"
                    },
                    {
                        "type": "string",
                        "name": "file_id"
                    },
                    {
                        "type": "string",
                        "name": "file_address"
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
class HelloArgs(_ArgsBase[str]):
    uploader_id: str
    patient_id: str
    file_id: str
    file_address: str

    @staticmethod
    def method() -> str:
        return "hello(string,string,string,string)string"


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

    def hello(
        self,
        *,
        uploader_id: str,
        patient_id: str,
        file_id: str,
        file_address: str,
        transaction_parameters: algokit_utils.TransactionParameters | None = None,
    ) -> "Composer":
        """Adds a call to `hello(string,string,string,string)string` ABI method
        
        :param str uploader_id: The `uploader_id` ABI parameter
        :param str patient_id: The `patient_id` ABI parameter
        :param str file_id: The `file_id` ABI parameter
        :param str file_address: The `file_address` ABI parameter
        :param algokit_utils.TransactionParameters transaction_parameters: (optional) Additional transaction parameters
        :returns Composer: This Composer instance"""

        args = HelloArgs(
            uploader_id=uploader_id,
            patient_id=patient_id,
            file_id=file_id,
            file_address=file_address,
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


class HelloWorldClient:
    """A class for interacting with the HelloWorld app providing high productivity and
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
        HelloWorldClient can be created with an app_id to interact with an existing application, alternatively
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

    def hello(
        self,
        *,
        uploader_id: str,
        patient_id: str,
        file_id: str,
        file_address: str,
        transaction_parameters: algokit_utils.TransactionParameters | None = None,
    ) -> algokit_utils.ABITransactionResponse[str]:
        """Calls `hello(string,string,string,string)string` ABI method
        
        :param str uploader_id: The `uploader_id` ABI parameter
        :param str patient_id: The `patient_id` ABI parameter
        :param str file_id: The `file_id` ABI parameter
        :param str file_address: The `file_address` ABI parameter
        :param algokit_utils.TransactionParameters transaction_parameters: (optional) Additional transaction parameters
        :returns algokit_utils.ABITransactionResponse[str]: The result of the transaction"""

        args = HelloArgs(
            uploader_id=uploader_id,
            patient_id=patient_id,
            file_id=file_id,
            file_address=file_address,
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
