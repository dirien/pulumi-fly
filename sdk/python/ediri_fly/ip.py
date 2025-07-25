# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import builtins
import copy
import warnings
import sys
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
if sys.version_info >= (3, 11):
    from typing import NotRequired, TypedDict, TypeAlias
else:
    from typing_extensions import NotRequired, TypedDict, TypeAlias
from . import _utilities

__all__ = ['IpArgs', 'Ip']

@pulumi.input_type
class IpArgs:
    def __init__(__self__, *,
                 app: pulumi.Input[builtins.str],
                 type: pulumi.Input[builtins.str],
                 region: Optional[pulumi.Input[builtins.str]] = None):
        """
        The set of arguments for constructing a Ip resource.
        :param pulumi.Input[builtins.str] app: The App this resource will be created in
        :param pulumi.Input[builtins.str] type: One of the following values (by regex): `^(v4|v6|private_v6)$`
        :param pulumi.Input[builtins.str] region: Fly region, ex `ord`, `sin`, `mad`
        """
        pulumi.set(__self__, "app", app)
        pulumi.set(__self__, "type", type)
        if region is not None:
            pulumi.set(__self__, "region", region)

    @property
    @pulumi.getter
    def app(self) -> pulumi.Input[builtins.str]:
        """
        The App this resource will be created in
        """
        return pulumi.get(self, "app")

    @app.setter
    def app(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "app", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[builtins.str]:
        """
        One of the following values (by regex): `^(v4|v6|private_v6)$`
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        Fly region, ex `ord`, `sin`, `mad`
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "region", value)


@pulumi.input_type
class _IpState:
    def __init__(__self__, *,
                 address: Optional[pulumi.Input[builtins.str]] = None,
                 app: Optional[pulumi.Input[builtins.str]] = None,
                 region: Optional[pulumi.Input[builtins.str]] = None,
                 type: Optional[pulumi.Input[builtins.str]] = None):
        """
        Input properties used for looking up and filtering Ip resources.
        :param pulumi.Input[builtins.str] address: Empty if using `shared_v4`
        :param pulumi.Input[builtins.str] app: The App this resource will be created in
        :param pulumi.Input[builtins.str] region: Fly region, ex `ord`, `sin`, `mad`
        :param pulumi.Input[builtins.str] type: One of the following values (by regex): `^(v4|v6|private_v6)$`
        """
        if address is not None:
            pulumi.set(__self__, "address", address)
        if app is not None:
            pulumi.set(__self__, "app", app)
        if region is not None:
            pulumi.set(__self__, "region", region)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def address(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        Empty if using `shared_v4`
        """
        return pulumi.get(self, "address")

    @address.setter
    def address(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "address", value)

    @property
    @pulumi.getter
    def app(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The App this resource will be created in
        """
        return pulumi.get(self, "app")

    @app.setter
    def app(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "app", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        Fly region, ex `ord`, `sin`, `mad`
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        One of the following values (by regex): `^(v4|v6|private_v6)$`
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "type", value)


@pulumi.type_token("fly:index/ip:Ip")
class Ip(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 app: Optional[pulumi.Input[builtins.str]] = None,
                 region: Optional[pulumi.Input[builtins.str]] = None,
                 type: Optional[pulumi.Input[builtins.str]] = None,
                 __props__=None):
        """
        Create a Ip resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[builtins.str] app: The App this resource will be created in
        :param pulumi.Input[builtins.str] region: Fly region, ex `ord`, `sin`, `mad`
        :param pulumi.Input[builtins.str] type: One of the following values (by regex): `^(v4|v6|private_v6)$`
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: IpArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a Ip resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param IpArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(IpArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 app: Optional[pulumi.Input[builtins.str]] = None,
                 region: Optional[pulumi.Input[builtins.str]] = None,
                 type: Optional[pulumi.Input[builtins.str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = IpArgs.__new__(IpArgs)

            if app is None and not opts.urn:
                raise TypeError("Missing required property 'app'")
            __props__.__dict__["app"] = app
            __props__.__dict__["region"] = region
            if type is None and not opts.urn:
                raise TypeError("Missing required property 'type'")
            __props__.__dict__["type"] = type
            __props__.__dict__["address"] = None
        super(Ip, __self__).__init__(
            'fly:index/ip:Ip',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            address: Optional[pulumi.Input[builtins.str]] = None,
            app: Optional[pulumi.Input[builtins.str]] = None,
            region: Optional[pulumi.Input[builtins.str]] = None,
            type: Optional[pulumi.Input[builtins.str]] = None) -> 'Ip':
        """
        Get an existing Ip resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[builtins.str] address: Empty if using `shared_v4`
        :param pulumi.Input[builtins.str] app: The App this resource will be created in
        :param pulumi.Input[builtins.str] region: Fly region, ex `ord`, `sin`, `mad`
        :param pulumi.Input[builtins.str] type: One of the following values (by regex): `^(v4|v6|private_v6)$`
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _IpState.__new__(_IpState)

        __props__.__dict__["address"] = address
        __props__.__dict__["app"] = app
        __props__.__dict__["region"] = region
        __props__.__dict__["type"] = type
        return Ip(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def address(self) -> pulumi.Output[builtins.str]:
        """
        Empty if using `shared_v4`
        """
        return pulumi.get(self, "address")

    @property
    @pulumi.getter
    def app(self) -> pulumi.Output[builtins.str]:
        """
        The App this resource will be created in
        """
        return pulumi.get(self, "app")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[builtins.str]:
        """
        Fly region, ex `ord`, `sin`, `mad`
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[builtins.str]:
        """
        One of the following values (by regex): `^(v4|v6|private_v6)$`
        """
        return pulumi.get(self, "type")

