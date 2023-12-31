# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs

__all__ = [
    'MachineMount',
    'MachineService',
    'MachineServicePort',
]

@pulumi.output_type
class MachineMount(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "sizeGb":
            suggest = "size_gb"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in MachineMount. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        MachineMount.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        MachineMount.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 path: str,
                 volume: str,
                 encrypted: Optional[bool] = None,
                 size_gb: Optional[int] = None):
        """
        :param str path: Path for volume to be mounted on vm
        :param str volume: Name or ID of volume
        """
        pulumi.set(__self__, "path", path)
        pulumi.set(__self__, "volume", volume)
        if encrypted is not None:
            pulumi.set(__self__, "encrypted", encrypted)
        if size_gb is not None:
            pulumi.set(__self__, "size_gb", size_gb)

    @property
    @pulumi.getter
    def path(self) -> str:
        """
        Path for volume to be mounted on vm
        """
        return pulumi.get(self, "path")

    @property
    @pulumi.getter
    def volume(self) -> str:
        """
        Name or ID of volume
        """
        return pulumi.get(self, "volume")

    @property
    @pulumi.getter
    def encrypted(self) -> Optional[bool]:
        return pulumi.get(self, "encrypted")

    @property
    @pulumi.getter(name="sizeGb")
    def size_gb(self) -> Optional[int]:
        return pulumi.get(self, "size_gb")


@pulumi.output_type
class MachineService(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "internalPort":
            suggest = "internal_port"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in MachineService. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        MachineService.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        MachineService.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 internal_port: int,
                 ports: Sequence['outputs.MachineServicePort'],
                 protocol: str):
        """
        :param int internal_port: Port application listens on internally
        :param Sequence['MachineServicePortArgs'] ports: External ports and handlers
        :param str protocol: network protocol
        """
        pulumi.set(__self__, "internal_port", internal_port)
        pulumi.set(__self__, "ports", ports)
        pulumi.set(__self__, "protocol", protocol)

    @property
    @pulumi.getter(name="internalPort")
    def internal_port(self) -> int:
        """
        Port application listens on internally
        """
        return pulumi.get(self, "internal_port")

    @property
    @pulumi.getter
    def ports(self) -> Sequence['outputs.MachineServicePort']:
        """
        External ports and handlers
        """
        return pulumi.get(self, "ports")

    @property
    @pulumi.getter
    def protocol(self) -> str:
        """
        network protocol
        """
        return pulumi.get(self, "protocol")


@pulumi.output_type
class MachineServicePort(dict):
    def __init__(__self__, *,
                 port: int,
                 handlers: Optional[Sequence[str]] = None):
        pulumi.set(__self__, "port", port)
        if handlers is not None:
            pulumi.set(__self__, "handlers", handlers)

    @property
    @pulumi.getter
    def port(self) -> int:
        return pulumi.get(self, "port")

    @property
    @pulumi.getter
    def handlers(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "handlers")


