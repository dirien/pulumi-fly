# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

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

__all__ = ['AppArgs', 'App']

@pulumi.input_type
class AppArgs:
    def __init__(__self__, *,
                 assign_shared_ip_address: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 org: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a App resource.
        :param pulumi.Input[bool] assign_shared_ip_address: Assign a shared ipv4 address to the app. Note that depending on conditions an app may get a shared ip automatically.
        :param pulumi.Input[str] name: Name of application
        :param pulumi.Input[str] org: The name of the organization to generate the app in, ex: `personal` (your initial org)
        """
        if assign_shared_ip_address is not None:
            pulumi.set(__self__, "assign_shared_ip_address", assign_shared_ip_address)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if org is not None:
            pulumi.set(__self__, "org", org)

    @property
    @pulumi.getter(name="assignSharedIpAddress")
    def assign_shared_ip_address(self) -> Optional[pulumi.Input[bool]]:
        """
        Assign a shared ipv4 address to the app. Note that depending on conditions an app may get a shared ip automatically.
        """
        return pulumi.get(self, "assign_shared_ip_address")

    @assign_shared_ip_address.setter
    def assign_shared_ip_address(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "assign_shared_ip_address", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of application
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def org(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the organization to generate the app in, ex: `personal` (your initial org)
        """
        return pulumi.get(self, "org")

    @org.setter
    def org(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "org", value)


@pulumi.input_type
class _AppState:
    def __init__(__self__, *,
                 app_url: Optional[pulumi.Input[str]] = None,
                 assign_shared_ip_address: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 org: Optional[pulumi.Input[str]] = None,
                 org_id: Optional[pulumi.Input[str]] = None,
                 shared_ip_address: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering App resources.
        :param pulumi.Input[bool] assign_shared_ip_address: Assign a shared ipv4 address to the app. Note that depending on conditions an app may get a shared ip automatically.
        :param pulumi.Input[str] name: Name of application
        :param pulumi.Input[str] org: The name of the organization to generate the app in, ex: `personal` (your initial org)
        :param pulumi.Input[str] shared_ip_address: A shared ipv4 address, automatically attached in certain conditions or if explicitly requested
        """
        if app_url is not None:
            pulumi.set(__self__, "app_url", app_url)
        if assign_shared_ip_address is not None:
            pulumi.set(__self__, "assign_shared_ip_address", assign_shared_ip_address)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if org is not None:
            pulumi.set(__self__, "org", org)
        if org_id is not None:
            pulumi.set(__self__, "org_id", org_id)
        if shared_ip_address is not None:
            pulumi.set(__self__, "shared_ip_address", shared_ip_address)

    @property
    @pulumi.getter(name="appUrl")
    def app_url(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "app_url")

    @app_url.setter
    def app_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "app_url", value)

    @property
    @pulumi.getter(name="assignSharedIpAddress")
    def assign_shared_ip_address(self) -> Optional[pulumi.Input[bool]]:
        """
        Assign a shared ipv4 address to the app. Note that depending on conditions an app may get a shared ip automatically.
        """
        return pulumi.get(self, "assign_shared_ip_address")

    @assign_shared_ip_address.setter
    def assign_shared_ip_address(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "assign_shared_ip_address", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of application
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def org(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the organization to generate the app in, ex: `personal` (your initial org)
        """
        return pulumi.get(self, "org")

    @org.setter
    def org(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "org", value)

    @property
    @pulumi.getter(name="orgId")
    def org_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "org_id")

    @org_id.setter
    def org_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "org_id", value)

    @property
    @pulumi.getter(name="sharedIpAddress")
    def shared_ip_address(self) -> Optional[pulumi.Input[str]]:
        """
        A shared ipv4 address, automatically attached in certain conditions or if explicitly requested
        """
        return pulumi.get(self, "shared_ip_address")

    @shared_ip_address.setter
    def shared_ip_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "shared_ip_address", value)


class App(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 assign_shared_ip_address: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 org: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a App resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] assign_shared_ip_address: Assign a shared ipv4 address to the app. Note that depending on conditions an app may get a shared ip automatically.
        :param pulumi.Input[str] name: Name of application
        :param pulumi.Input[str] org: The name of the organization to generate the app in, ex: `personal` (your initial org)
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[AppArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a App resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param AppArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AppArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 assign_shared_ip_address: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 org: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AppArgs.__new__(AppArgs)

            __props__.__dict__["assign_shared_ip_address"] = assign_shared_ip_address
            __props__.__dict__["name"] = name
            __props__.__dict__["org"] = org
            __props__.__dict__["app_url"] = None
            __props__.__dict__["org_id"] = None
            __props__.__dict__["shared_ip_address"] = None
        super(App, __self__).__init__(
            'fly:index/app:App',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            app_url: Optional[pulumi.Input[str]] = None,
            assign_shared_ip_address: Optional[pulumi.Input[bool]] = None,
            name: Optional[pulumi.Input[str]] = None,
            org: Optional[pulumi.Input[str]] = None,
            org_id: Optional[pulumi.Input[str]] = None,
            shared_ip_address: Optional[pulumi.Input[str]] = None) -> 'App':
        """
        Get an existing App resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] assign_shared_ip_address: Assign a shared ipv4 address to the app. Note that depending on conditions an app may get a shared ip automatically.
        :param pulumi.Input[str] name: Name of application
        :param pulumi.Input[str] org: The name of the organization to generate the app in, ex: `personal` (your initial org)
        :param pulumi.Input[str] shared_ip_address: A shared ipv4 address, automatically attached in certain conditions or if explicitly requested
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AppState.__new__(_AppState)

        __props__.__dict__["app_url"] = app_url
        __props__.__dict__["assign_shared_ip_address"] = assign_shared_ip_address
        __props__.__dict__["name"] = name
        __props__.__dict__["org"] = org
        __props__.__dict__["org_id"] = org_id
        __props__.__dict__["shared_ip_address"] = shared_ip_address
        return App(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="appUrl")
    def app_url(self) -> pulumi.Output[str]:
        return pulumi.get(self, "app_url")

    @property
    @pulumi.getter(name="assignSharedIpAddress")
    def assign_shared_ip_address(self) -> pulumi.Output[bool]:
        """
        Assign a shared ipv4 address to the app. Note that depending on conditions an app may get a shared ip automatically.
        """
        return pulumi.get(self, "assign_shared_ip_address")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of application
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def org(self) -> pulumi.Output[str]:
        """
        The name of the organization to generate the app in, ex: `personal` (your initial org)
        """
        return pulumi.get(self, "org")

    @property
    @pulumi.getter(name="orgId")
    def org_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "org_id")

    @property
    @pulumi.getter(name="sharedIpAddress")
    def shared_ip_address(self) -> pulumi.Output[str]:
        """
        A shared ipv4 address, automatically attached in certain conditions or if explicitly requested
        """
        return pulumi.get(self, "shared_ip_address")

