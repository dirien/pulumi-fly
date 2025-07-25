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
from . import outputs
from ._inputs import *

__all__ = ['MachineArgs', 'Machine']

@pulumi.input_type
class MachineArgs:
    def __init__(__self__, *,
                 app: pulumi.Input[builtins.str],
                 image: pulumi.Input[builtins.str],
                 region: pulumi.Input[builtins.str],
                 auto_destroy: Optional[pulumi.Input[builtins.bool]] = None,
                 cmds: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]] = None,
                 cpu_type: Optional[pulumi.Input[builtins.str]] = None,
                 cpus: Optional[pulumi.Input[builtins.int]] = None,
                 entrypoints: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]] = None,
                 env: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]] = None,
                 execs: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]] = None,
                 memory: Optional[pulumi.Input[builtins.int]] = None,
                 mounts: Optional[pulumi.Input[Sequence[pulumi.Input['MachineMountArgs']]]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 services: Optional[pulumi.Input[Sequence[pulumi.Input['MachineServiceArgs']]]] = None):
        """
        The set of arguments for constructing a Machine resource.
        :param pulumi.Input[builtins.str] app: The App this resource will be created in
        :param pulumi.Input[builtins.str] image: Protocol-less docker image, ex: `registry.fly.io/myapp:mytag`
        :param pulumi.Input[builtins.str] region: Fly region, ex `ord`, `sin`, `mad`
        :param pulumi.Input[builtins.bool] auto_destroy: Optional boolean telling the Machine to destroy itself once it's complete
        :param pulumi.Input[builtins.str] cpu_type: Which machine flavor, ex: `shared`
        :param pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]] env: Keys and values must be strings
        :param pulumi.Input[builtins.int] memory: Amount of memory in MB. `256`, `512`, `1024`, ...
        :param pulumi.Input[builtins.str] name: A user-provided identifier
        """
        pulumi.set(__self__, "app", app)
        pulumi.set(__self__, "image", image)
        pulumi.set(__self__, "region", region)
        if auto_destroy is not None:
            pulumi.set(__self__, "auto_destroy", auto_destroy)
        if cmds is not None:
            pulumi.set(__self__, "cmds", cmds)
        if cpu_type is not None:
            pulumi.set(__self__, "cpu_type", cpu_type)
        if cpus is not None:
            pulumi.set(__self__, "cpus", cpus)
        if entrypoints is not None:
            pulumi.set(__self__, "entrypoints", entrypoints)
        if env is not None:
            pulumi.set(__self__, "env", env)
        if execs is not None:
            pulumi.set(__self__, "execs", execs)
        if memory is not None:
            pulumi.set(__self__, "memory", memory)
        if mounts is not None:
            pulumi.set(__self__, "mounts", mounts)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if services is not None:
            pulumi.set(__self__, "services", services)

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
    def image(self) -> pulumi.Input[builtins.str]:
        """
        Protocol-less docker image, ex: `registry.fly.io/myapp:mytag`
        """
        return pulumi.get(self, "image")

    @image.setter
    def image(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "image", value)

    @property
    @pulumi.getter
    def region(self) -> pulumi.Input[builtins.str]:
        """
        Fly region, ex `ord`, `sin`, `mad`
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter(name="autoDestroy")
    def auto_destroy(self) -> Optional[pulumi.Input[builtins.bool]]:
        """
        Optional boolean telling the Machine to destroy itself once it's complete
        """
        return pulumi.get(self, "auto_destroy")

    @auto_destroy.setter
    def auto_destroy(self, value: Optional[pulumi.Input[builtins.bool]]):
        pulumi.set(self, "auto_destroy", value)

    @property
    @pulumi.getter
    def cmds(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]]:
        return pulumi.get(self, "cmds")

    @cmds.setter
    def cmds(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]]):
        pulumi.set(self, "cmds", value)

    @property
    @pulumi.getter(name="cpuType")
    def cpu_type(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        Which machine flavor, ex: `shared`
        """
        return pulumi.get(self, "cpu_type")

    @cpu_type.setter
    def cpu_type(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "cpu_type", value)

    @property
    @pulumi.getter
    def cpus(self) -> Optional[pulumi.Input[builtins.int]]:
        return pulumi.get(self, "cpus")

    @cpus.setter
    def cpus(self, value: Optional[pulumi.Input[builtins.int]]):
        pulumi.set(self, "cpus", value)

    @property
    @pulumi.getter
    def entrypoints(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]]:
        return pulumi.get(self, "entrypoints")

    @entrypoints.setter
    def entrypoints(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]]):
        pulumi.set(self, "entrypoints", value)

    @property
    @pulumi.getter
    def env(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]]:
        """
        Keys and values must be strings
        """
        return pulumi.get(self, "env")

    @env.setter
    def env(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]]):
        pulumi.set(self, "env", value)

    @property
    @pulumi.getter
    def execs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]]:
        return pulumi.get(self, "execs")

    @execs.setter
    def execs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]]):
        pulumi.set(self, "execs", value)

    @property
    @pulumi.getter
    def memory(self) -> Optional[pulumi.Input[builtins.int]]:
        """
        Amount of memory in MB. `256`, `512`, `1024`, ...
        """
        return pulumi.get(self, "memory")

    @memory.setter
    def memory(self, value: Optional[pulumi.Input[builtins.int]]):
        pulumi.set(self, "memory", value)

    @property
    @pulumi.getter
    def mounts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['MachineMountArgs']]]]:
        return pulumi.get(self, "mounts")

    @mounts.setter
    def mounts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['MachineMountArgs']]]]):
        pulumi.set(self, "mounts", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        A user-provided identifier
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def services(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['MachineServiceArgs']]]]:
        return pulumi.get(self, "services")

    @services.setter
    def services(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['MachineServiceArgs']]]]):
        pulumi.set(self, "services", value)


@pulumi.input_type
class _MachineState:
    def __init__(__self__, *,
                 app: Optional[pulumi.Input[builtins.str]] = None,
                 auto_destroy: Optional[pulumi.Input[builtins.bool]] = None,
                 cmds: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]] = None,
                 cpu_type: Optional[pulumi.Input[builtins.str]] = None,
                 cpus: Optional[pulumi.Input[builtins.int]] = None,
                 entrypoints: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]] = None,
                 env: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]] = None,
                 execs: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]] = None,
                 image: Optional[pulumi.Input[builtins.str]] = None,
                 memory: Optional[pulumi.Input[builtins.int]] = None,
                 mounts: Optional[pulumi.Input[Sequence[pulumi.Input['MachineMountArgs']]]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 private_ip: Optional[pulumi.Input[builtins.str]] = None,
                 region: Optional[pulumi.Input[builtins.str]] = None,
                 services: Optional[pulumi.Input[Sequence[pulumi.Input['MachineServiceArgs']]]] = None):
        """
        Input properties used for looking up and filtering Machine resources.
        :param pulumi.Input[builtins.str] app: The App this resource will be created in
        :param pulumi.Input[builtins.bool] auto_destroy: Optional boolean telling the Machine to destroy itself once it's complete
        :param pulumi.Input[builtins.str] cpu_type: Which machine flavor, ex: `shared`
        :param pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]] env: Keys and values must be strings
        :param pulumi.Input[builtins.str] image: Protocol-less docker image, ex: `registry.fly.io/myapp:mytag`
        :param pulumi.Input[builtins.int] memory: Amount of memory in MB. `256`, `512`, `1024`, ...
        :param pulumi.Input[builtins.str] name: A user-provided identifier
        :param pulumi.Input[builtins.str] region: Fly region, ex `ord`, `sin`, `mad`
        """
        if app is not None:
            pulumi.set(__self__, "app", app)
        if auto_destroy is not None:
            pulumi.set(__self__, "auto_destroy", auto_destroy)
        if cmds is not None:
            pulumi.set(__self__, "cmds", cmds)
        if cpu_type is not None:
            pulumi.set(__self__, "cpu_type", cpu_type)
        if cpus is not None:
            pulumi.set(__self__, "cpus", cpus)
        if entrypoints is not None:
            pulumi.set(__self__, "entrypoints", entrypoints)
        if env is not None:
            pulumi.set(__self__, "env", env)
        if execs is not None:
            pulumi.set(__self__, "execs", execs)
        if image is not None:
            pulumi.set(__self__, "image", image)
        if memory is not None:
            pulumi.set(__self__, "memory", memory)
        if mounts is not None:
            pulumi.set(__self__, "mounts", mounts)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if private_ip is not None:
            pulumi.set(__self__, "private_ip", private_ip)
        if region is not None:
            pulumi.set(__self__, "region", region)
        if services is not None:
            pulumi.set(__self__, "services", services)

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
    @pulumi.getter(name="autoDestroy")
    def auto_destroy(self) -> Optional[pulumi.Input[builtins.bool]]:
        """
        Optional boolean telling the Machine to destroy itself once it's complete
        """
        return pulumi.get(self, "auto_destroy")

    @auto_destroy.setter
    def auto_destroy(self, value: Optional[pulumi.Input[builtins.bool]]):
        pulumi.set(self, "auto_destroy", value)

    @property
    @pulumi.getter
    def cmds(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]]:
        return pulumi.get(self, "cmds")

    @cmds.setter
    def cmds(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]]):
        pulumi.set(self, "cmds", value)

    @property
    @pulumi.getter(name="cpuType")
    def cpu_type(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        Which machine flavor, ex: `shared`
        """
        return pulumi.get(self, "cpu_type")

    @cpu_type.setter
    def cpu_type(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "cpu_type", value)

    @property
    @pulumi.getter
    def cpus(self) -> Optional[pulumi.Input[builtins.int]]:
        return pulumi.get(self, "cpus")

    @cpus.setter
    def cpus(self, value: Optional[pulumi.Input[builtins.int]]):
        pulumi.set(self, "cpus", value)

    @property
    @pulumi.getter
    def entrypoints(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]]:
        return pulumi.get(self, "entrypoints")

    @entrypoints.setter
    def entrypoints(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]]):
        pulumi.set(self, "entrypoints", value)

    @property
    @pulumi.getter
    def env(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]]:
        """
        Keys and values must be strings
        """
        return pulumi.get(self, "env")

    @env.setter
    def env(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]]):
        pulumi.set(self, "env", value)

    @property
    @pulumi.getter
    def execs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]]:
        return pulumi.get(self, "execs")

    @execs.setter
    def execs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]]):
        pulumi.set(self, "execs", value)

    @property
    @pulumi.getter
    def image(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        Protocol-less docker image, ex: `registry.fly.io/myapp:mytag`
        """
        return pulumi.get(self, "image")

    @image.setter
    def image(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "image", value)

    @property
    @pulumi.getter
    def memory(self) -> Optional[pulumi.Input[builtins.int]]:
        """
        Amount of memory in MB. `256`, `512`, `1024`, ...
        """
        return pulumi.get(self, "memory")

    @memory.setter
    def memory(self, value: Optional[pulumi.Input[builtins.int]]):
        pulumi.set(self, "memory", value)

    @property
    @pulumi.getter
    def mounts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['MachineMountArgs']]]]:
        return pulumi.get(self, "mounts")

    @mounts.setter
    def mounts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['MachineMountArgs']]]]):
        pulumi.set(self, "mounts", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        A user-provided identifier
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="privateIp")
    def private_ip(self) -> Optional[pulumi.Input[builtins.str]]:
        return pulumi.get(self, "private_ip")

    @private_ip.setter
    def private_ip(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "private_ip", value)

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
    def services(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['MachineServiceArgs']]]]:
        return pulumi.get(self, "services")

    @services.setter
    def services(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['MachineServiceArgs']]]]):
        pulumi.set(self, "services", value)


@pulumi.type_token("fly:index/machine:Machine")
class Machine(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 app: Optional[pulumi.Input[builtins.str]] = None,
                 auto_destroy: Optional[pulumi.Input[builtins.bool]] = None,
                 cmds: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]] = None,
                 cpu_type: Optional[pulumi.Input[builtins.str]] = None,
                 cpus: Optional[pulumi.Input[builtins.int]] = None,
                 entrypoints: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]] = None,
                 env: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]] = None,
                 execs: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]] = None,
                 image: Optional[pulumi.Input[builtins.str]] = None,
                 memory: Optional[pulumi.Input[builtins.int]] = None,
                 mounts: Optional[pulumi.Input[Sequence[pulumi.Input[Union['MachineMountArgs', 'MachineMountArgsDict']]]]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 region: Optional[pulumi.Input[builtins.str]] = None,
                 services: Optional[pulumi.Input[Sequence[pulumi.Input[Union['MachineServiceArgs', 'MachineServiceArgsDict']]]]] = None,
                 __props__=None):
        """
        Create a Machine resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[builtins.str] app: The App this resource will be created in
        :param pulumi.Input[builtins.bool] auto_destroy: Optional boolean telling the Machine to destroy itself once it's complete
        :param pulumi.Input[builtins.str] cpu_type: Which machine flavor, ex: `shared`
        :param pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]] env: Keys and values must be strings
        :param pulumi.Input[builtins.str] image: Protocol-less docker image, ex: `registry.fly.io/myapp:mytag`
        :param pulumi.Input[builtins.int] memory: Amount of memory in MB. `256`, `512`, `1024`, ...
        :param pulumi.Input[builtins.str] name: A user-provided identifier
        :param pulumi.Input[builtins.str] region: Fly region, ex `ord`, `sin`, `mad`
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: MachineArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a Machine resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param MachineArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(MachineArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 app: Optional[pulumi.Input[builtins.str]] = None,
                 auto_destroy: Optional[pulumi.Input[builtins.bool]] = None,
                 cmds: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]] = None,
                 cpu_type: Optional[pulumi.Input[builtins.str]] = None,
                 cpus: Optional[pulumi.Input[builtins.int]] = None,
                 entrypoints: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]] = None,
                 env: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]] = None,
                 execs: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]] = None,
                 image: Optional[pulumi.Input[builtins.str]] = None,
                 memory: Optional[pulumi.Input[builtins.int]] = None,
                 mounts: Optional[pulumi.Input[Sequence[pulumi.Input[Union['MachineMountArgs', 'MachineMountArgsDict']]]]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 region: Optional[pulumi.Input[builtins.str]] = None,
                 services: Optional[pulumi.Input[Sequence[pulumi.Input[Union['MachineServiceArgs', 'MachineServiceArgsDict']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = MachineArgs.__new__(MachineArgs)

            if app is None and not opts.urn:
                raise TypeError("Missing required property 'app'")
            __props__.__dict__["app"] = app
            __props__.__dict__["auto_destroy"] = auto_destroy
            __props__.__dict__["cmds"] = cmds
            __props__.__dict__["cpu_type"] = cpu_type
            __props__.__dict__["cpus"] = cpus
            __props__.__dict__["entrypoints"] = entrypoints
            __props__.__dict__["env"] = env
            __props__.__dict__["execs"] = execs
            if image is None and not opts.urn:
                raise TypeError("Missing required property 'image'")
            __props__.__dict__["image"] = image
            __props__.__dict__["memory"] = memory
            __props__.__dict__["mounts"] = mounts
            __props__.__dict__["name"] = name
            if region is None and not opts.urn:
                raise TypeError("Missing required property 'region'")
            __props__.__dict__["region"] = region
            __props__.__dict__["services"] = services
            __props__.__dict__["private_ip"] = None
        super(Machine, __self__).__init__(
            'fly:index/machine:Machine',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            app: Optional[pulumi.Input[builtins.str]] = None,
            auto_destroy: Optional[pulumi.Input[builtins.bool]] = None,
            cmds: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]] = None,
            cpu_type: Optional[pulumi.Input[builtins.str]] = None,
            cpus: Optional[pulumi.Input[builtins.int]] = None,
            entrypoints: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]] = None,
            env: Optional[pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]]] = None,
            execs: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]] = None,
            image: Optional[pulumi.Input[builtins.str]] = None,
            memory: Optional[pulumi.Input[builtins.int]] = None,
            mounts: Optional[pulumi.Input[Sequence[pulumi.Input[Union['MachineMountArgs', 'MachineMountArgsDict']]]]] = None,
            name: Optional[pulumi.Input[builtins.str]] = None,
            private_ip: Optional[pulumi.Input[builtins.str]] = None,
            region: Optional[pulumi.Input[builtins.str]] = None,
            services: Optional[pulumi.Input[Sequence[pulumi.Input[Union['MachineServiceArgs', 'MachineServiceArgsDict']]]]] = None) -> 'Machine':
        """
        Get an existing Machine resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[builtins.str] app: The App this resource will be created in
        :param pulumi.Input[builtins.bool] auto_destroy: Optional boolean telling the Machine to destroy itself once it's complete
        :param pulumi.Input[builtins.str] cpu_type: Which machine flavor, ex: `shared`
        :param pulumi.Input[Mapping[str, pulumi.Input[builtins.str]]] env: Keys and values must be strings
        :param pulumi.Input[builtins.str] image: Protocol-less docker image, ex: `registry.fly.io/myapp:mytag`
        :param pulumi.Input[builtins.int] memory: Amount of memory in MB. `256`, `512`, `1024`, ...
        :param pulumi.Input[builtins.str] name: A user-provided identifier
        :param pulumi.Input[builtins.str] region: Fly region, ex `ord`, `sin`, `mad`
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _MachineState.__new__(_MachineState)

        __props__.__dict__["app"] = app
        __props__.__dict__["auto_destroy"] = auto_destroy
        __props__.__dict__["cmds"] = cmds
        __props__.__dict__["cpu_type"] = cpu_type
        __props__.__dict__["cpus"] = cpus
        __props__.__dict__["entrypoints"] = entrypoints
        __props__.__dict__["env"] = env
        __props__.__dict__["execs"] = execs
        __props__.__dict__["image"] = image
        __props__.__dict__["memory"] = memory
        __props__.__dict__["mounts"] = mounts
        __props__.__dict__["name"] = name
        __props__.__dict__["private_ip"] = private_ip
        __props__.__dict__["region"] = region
        __props__.__dict__["services"] = services
        return Machine(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def app(self) -> pulumi.Output[builtins.str]:
        """
        The App this resource will be created in
        """
        return pulumi.get(self, "app")

    @property
    @pulumi.getter(name="autoDestroy")
    def auto_destroy(self) -> pulumi.Output[builtins.bool]:
        """
        Optional boolean telling the Machine to destroy itself once it's complete
        """
        return pulumi.get(self, "auto_destroy")

    @property
    @pulumi.getter
    def cmds(self) -> pulumi.Output[Optional[Sequence[builtins.str]]]:
        return pulumi.get(self, "cmds")

    @property
    @pulumi.getter(name="cpuType")
    def cpu_type(self) -> pulumi.Output[builtins.str]:
        """
        Which machine flavor, ex: `shared`
        """
        return pulumi.get(self, "cpu_type")

    @property
    @pulumi.getter
    def cpus(self) -> pulumi.Output[builtins.int]:
        return pulumi.get(self, "cpus")

    @property
    @pulumi.getter
    def entrypoints(self) -> pulumi.Output[Optional[Sequence[builtins.str]]]:
        return pulumi.get(self, "entrypoints")

    @property
    @pulumi.getter
    def env(self) -> pulumi.Output[Mapping[str, builtins.str]]:
        """
        Keys and values must be strings
        """
        return pulumi.get(self, "env")

    @property
    @pulumi.getter
    def execs(self) -> pulumi.Output[Optional[Sequence[builtins.str]]]:
        return pulumi.get(self, "execs")

    @property
    @pulumi.getter
    def image(self) -> pulumi.Output[builtins.str]:
        """
        Protocol-less docker image, ex: `registry.fly.io/myapp:mytag`
        """
        return pulumi.get(self, "image")

    @property
    @pulumi.getter
    def memory(self) -> pulumi.Output[builtins.int]:
        """
        Amount of memory in MB. `256`, `512`, `1024`, ...
        """
        return pulumi.get(self, "memory")

    @property
    @pulumi.getter
    def mounts(self) -> pulumi.Output[Optional[Sequence['outputs.MachineMount']]]:
        return pulumi.get(self, "mounts")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[builtins.str]:
        """
        A user-provided identifier
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="privateIp")
    def private_ip(self) -> pulumi.Output[builtins.str]:
        return pulumi.get(self, "private_ip")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[builtins.str]:
        """
        Fly region, ex `ord`, `sin`, `mad`
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter
    def services(self) -> pulumi.Output[Optional[Sequence['outputs.MachineService']]]:
        return pulumi.get(self, "services")

