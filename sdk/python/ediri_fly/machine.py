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
from ._inputs import *

__all__ = ['MachineArgs', 'Machine']

@pulumi.input_type
class MachineArgs:
    def __init__(__self__, *,
                 app: pulumi.Input[str],
                 image: pulumi.Input[str],
                 region: pulumi.Input[str],
                 cmds: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 cpus: Optional[pulumi.Input[int]] = None,
                 cputype: Optional[pulumi.Input[str]] = None,
                 entrypoints: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 env: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 execs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 memorymb: Optional[pulumi.Input[int]] = None,
                 mounts: Optional[pulumi.Input[Sequence[pulumi.Input['MachineMountArgs']]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 services: Optional[pulumi.Input[Sequence[pulumi.Input['MachineServiceArgs']]]] = None):
        """
        The set of arguments for constructing a Machine resource.
        :param pulumi.Input[str] app: fly app
        :param pulumi.Input[str] image: docker image
        :param pulumi.Input[str] region: machine region
        :param pulumi.Input[Sequence[pulumi.Input[str]]] cmds: cmd
        :param pulumi.Input[int] cpus: cpu count
        :param pulumi.Input[str] cputype: cpu type
        :param pulumi.Input[Sequence[pulumi.Input[str]]] entrypoints: image entrypoint
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] env: Optional environment variables, keys and values must be strings
        :param pulumi.Input[Sequence[pulumi.Input[str]]] execs: exec command
        :param pulumi.Input[int] memorymb: memory mb
        :param pulumi.Input[Sequence[pulumi.Input['MachineMountArgs']]] mounts: Volume mounts
        :param pulumi.Input[str] name: machine name
        :param pulumi.Input[Sequence[pulumi.Input['MachineServiceArgs']]] services: services
        """
        pulumi.set(__self__, "app", app)
        pulumi.set(__self__, "image", image)
        pulumi.set(__self__, "region", region)
        if cmds is not None:
            pulumi.set(__self__, "cmds", cmds)
        if cpus is not None:
            pulumi.set(__self__, "cpus", cpus)
        if cputype is not None:
            pulumi.set(__self__, "cputype", cputype)
        if entrypoints is not None:
            pulumi.set(__self__, "entrypoints", entrypoints)
        if env is not None:
            pulumi.set(__self__, "env", env)
        if execs is not None:
            pulumi.set(__self__, "execs", execs)
        if memorymb is not None:
            pulumi.set(__self__, "memorymb", memorymb)
        if mounts is not None:
            pulumi.set(__self__, "mounts", mounts)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if services is not None:
            pulumi.set(__self__, "services", services)

    @property
    @pulumi.getter
    def app(self) -> pulumi.Input[str]:
        """
        fly app
        """
        return pulumi.get(self, "app")

    @app.setter
    def app(self, value: pulumi.Input[str]):
        pulumi.set(self, "app", value)

    @property
    @pulumi.getter
    def image(self) -> pulumi.Input[str]:
        """
        docker image
        """
        return pulumi.get(self, "image")

    @image.setter
    def image(self, value: pulumi.Input[str]):
        pulumi.set(self, "image", value)

    @property
    @pulumi.getter
    def region(self) -> pulumi.Input[str]:
        """
        machine region
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: pulumi.Input[str]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter
    def cmds(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        cmd
        """
        return pulumi.get(self, "cmds")

    @cmds.setter
    def cmds(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "cmds", value)

    @property
    @pulumi.getter
    def cpus(self) -> Optional[pulumi.Input[int]]:
        """
        cpu count
        """
        return pulumi.get(self, "cpus")

    @cpus.setter
    def cpus(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "cpus", value)

    @property
    @pulumi.getter
    def cputype(self) -> Optional[pulumi.Input[str]]:
        """
        cpu type
        """
        return pulumi.get(self, "cputype")

    @cputype.setter
    def cputype(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cputype", value)

    @property
    @pulumi.getter
    def entrypoints(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        image entrypoint
        """
        return pulumi.get(self, "entrypoints")

    @entrypoints.setter
    def entrypoints(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "entrypoints", value)

    @property
    @pulumi.getter
    def env(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Optional environment variables, keys and values must be strings
        """
        return pulumi.get(self, "env")

    @env.setter
    def env(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "env", value)

    @property
    @pulumi.getter
    def execs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        exec command
        """
        return pulumi.get(self, "execs")

    @execs.setter
    def execs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "execs", value)

    @property
    @pulumi.getter
    def memorymb(self) -> Optional[pulumi.Input[int]]:
        """
        memory mb
        """
        return pulumi.get(self, "memorymb")

    @memorymb.setter
    def memorymb(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "memorymb", value)

    @property
    @pulumi.getter
    def mounts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['MachineMountArgs']]]]:
        """
        Volume mounts
        """
        return pulumi.get(self, "mounts")

    @mounts.setter
    def mounts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['MachineMountArgs']]]]):
        pulumi.set(self, "mounts", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        machine name
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def services(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['MachineServiceArgs']]]]:
        """
        services
        """
        return pulumi.get(self, "services")

    @services.setter
    def services(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['MachineServiceArgs']]]]):
        pulumi.set(self, "services", value)


@pulumi.input_type
class _MachineState:
    def __init__(__self__, *,
                 app: Optional[pulumi.Input[str]] = None,
                 cmds: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 cpus: Optional[pulumi.Input[int]] = None,
                 cputype: Optional[pulumi.Input[str]] = None,
                 entrypoints: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 env: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 execs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 image: Optional[pulumi.Input[str]] = None,
                 memorymb: Optional[pulumi.Input[int]] = None,
                 mounts: Optional[pulumi.Input[Sequence[pulumi.Input['MachineMountArgs']]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 privateip: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 services: Optional[pulumi.Input[Sequence[pulumi.Input['MachineServiceArgs']]]] = None):
        """
        Input properties used for looking up and filtering Machine resources.
        :param pulumi.Input[str] app: fly app
        :param pulumi.Input[Sequence[pulumi.Input[str]]] cmds: cmd
        :param pulumi.Input[int] cpus: cpu count
        :param pulumi.Input[str] cputype: cpu type
        :param pulumi.Input[Sequence[pulumi.Input[str]]] entrypoints: image entrypoint
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] env: Optional environment variables, keys and values must be strings
        :param pulumi.Input[Sequence[pulumi.Input[str]]] execs: exec command
        :param pulumi.Input[str] image: docker image
        :param pulumi.Input[int] memorymb: memory mb
        :param pulumi.Input[Sequence[pulumi.Input['MachineMountArgs']]] mounts: Volume mounts
        :param pulumi.Input[str] name: machine name
        :param pulumi.Input[str] privateip: Private IP
        :param pulumi.Input[str] region: machine region
        :param pulumi.Input[Sequence[pulumi.Input['MachineServiceArgs']]] services: services
        """
        if app is not None:
            pulumi.set(__self__, "app", app)
        if cmds is not None:
            pulumi.set(__self__, "cmds", cmds)
        if cpus is not None:
            pulumi.set(__self__, "cpus", cpus)
        if cputype is not None:
            pulumi.set(__self__, "cputype", cputype)
        if entrypoints is not None:
            pulumi.set(__self__, "entrypoints", entrypoints)
        if env is not None:
            pulumi.set(__self__, "env", env)
        if execs is not None:
            pulumi.set(__self__, "execs", execs)
        if image is not None:
            pulumi.set(__self__, "image", image)
        if memorymb is not None:
            pulumi.set(__self__, "memorymb", memorymb)
        if mounts is not None:
            pulumi.set(__self__, "mounts", mounts)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if privateip is not None:
            pulumi.set(__self__, "privateip", privateip)
        if region is not None:
            pulumi.set(__self__, "region", region)
        if services is not None:
            pulumi.set(__self__, "services", services)

    @property
    @pulumi.getter
    def app(self) -> Optional[pulumi.Input[str]]:
        """
        fly app
        """
        return pulumi.get(self, "app")

    @app.setter
    def app(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "app", value)

    @property
    @pulumi.getter
    def cmds(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        cmd
        """
        return pulumi.get(self, "cmds")

    @cmds.setter
    def cmds(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "cmds", value)

    @property
    @pulumi.getter
    def cpus(self) -> Optional[pulumi.Input[int]]:
        """
        cpu count
        """
        return pulumi.get(self, "cpus")

    @cpus.setter
    def cpus(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "cpus", value)

    @property
    @pulumi.getter
    def cputype(self) -> Optional[pulumi.Input[str]]:
        """
        cpu type
        """
        return pulumi.get(self, "cputype")

    @cputype.setter
    def cputype(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cputype", value)

    @property
    @pulumi.getter
    def entrypoints(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        image entrypoint
        """
        return pulumi.get(self, "entrypoints")

    @entrypoints.setter
    def entrypoints(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "entrypoints", value)

    @property
    @pulumi.getter
    def env(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Optional environment variables, keys and values must be strings
        """
        return pulumi.get(self, "env")

    @env.setter
    def env(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "env", value)

    @property
    @pulumi.getter
    def execs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        exec command
        """
        return pulumi.get(self, "execs")

    @execs.setter
    def execs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "execs", value)

    @property
    @pulumi.getter
    def image(self) -> Optional[pulumi.Input[str]]:
        """
        docker image
        """
        return pulumi.get(self, "image")

    @image.setter
    def image(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "image", value)

    @property
    @pulumi.getter
    def memorymb(self) -> Optional[pulumi.Input[int]]:
        """
        memory mb
        """
        return pulumi.get(self, "memorymb")

    @memorymb.setter
    def memorymb(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "memorymb", value)

    @property
    @pulumi.getter
    def mounts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['MachineMountArgs']]]]:
        """
        Volume mounts
        """
        return pulumi.get(self, "mounts")

    @mounts.setter
    def mounts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['MachineMountArgs']]]]):
        pulumi.set(self, "mounts", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        machine name
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def privateip(self) -> Optional[pulumi.Input[str]]:
        """
        Private IP
        """
        return pulumi.get(self, "privateip")

    @privateip.setter
    def privateip(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "privateip", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        machine region
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter
    def services(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['MachineServiceArgs']]]]:
        """
        services
        """
        return pulumi.get(self, "services")

    @services.setter
    def services(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['MachineServiceArgs']]]]):
        pulumi.set(self, "services", value)


class Machine(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 app: Optional[pulumi.Input[str]] = None,
                 cmds: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 cpus: Optional[pulumi.Input[int]] = None,
                 cputype: Optional[pulumi.Input[str]] = None,
                 entrypoints: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 env: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 execs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 image: Optional[pulumi.Input[str]] = None,
                 memorymb: Optional[pulumi.Input[int]] = None,
                 mounts: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['MachineMountArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 services: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['MachineServiceArgs']]]]] = None,
                 __props__=None):
        """
        Fly machine resource

        ## Example Usage

        ## Import

        <break><break>```sh<break> $ pulumi import fly:index/machine:Machine exampleMachine <app_id>,<machine_id> <break>```<break><break>

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] app: fly app
        :param pulumi.Input[Sequence[pulumi.Input[str]]] cmds: cmd
        :param pulumi.Input[int] cpus: cpu count
        :param pulumi.Input[str] cputype: cpu type
        :param pulumi.Input[Sequence[pulumi.Input[str]]] entrypoints: image entrypoint
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] env: Optional environment variables, keys and values must be strings
        :param pulumi.Input[Sequence[pulumi.Input[str]]] execs: exec command
        :param pulumi.Input[str] image: docker image
        :param pulumi.Input[int] memorymb: memory mb
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['MachineMountArgs']]]] mounts: Volume mounts
        :param pulumi.Input[str] name: machine name
        :param pulumi.Input[str] region: machine region
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['MachineServiceArgs']]]] services: services
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: MachineArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Fly machine resource

        ## Example Usage

        ## Import

        <break><break>```sh<break> $ pulumi import fly:index/machine:Machine exampleMachine <app_id>,<machine_id> <break>```<break><break>

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
                 app: Optional[pulumi.Input[str]] = None,
                 cmds: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 cpus: Optional[pulumi.Input[int]] = None,
                 cputype: Optional[pulumi.Input[str]] = None,
                 entrypoints: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 env: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 execs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 image: Optional[pulumi.Input[str]] = None,
                 memorymb: Optional[pulumi.Input[int]] = None,
                 mounts: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['MachineMountArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 services: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['MachineServiceArgs']]]]] = None,
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
            __props__.__dict__["cmds"] = cmds
            __props__.__dict__["cpus"] = cpus
            __props__.__dict__["cputype"] = cputype
            __props__.__dict__["entrypoints"] = entrypoints
            __props__.__dict__["env"] = env
            __props__.__dict__["execs"] = execs
            if image is None and not opts.urn:
                raise TypeError("Missing required property 'image'")
            __props__.__dict__["image"] = image
            __props__.__dict__["memorymb"] = memorymb
            __props__.__dict__["mounts"] = mounts
            __props__.__dict__["name"] = name
            if region is None and not opts.urn:
                raise TypeError("Missing required property 'region'")
            __props__.__dict__["region"] = region
            __props__.__dict__["services"] = services
            __props__.__dict__["privateip"] = None
        super(Machine, __self__).__init__(
            'fly:index/machine:Machine',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            app: Optional[pulumi.Input[str]] = None,
            cmds: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            cpus: Optional[pulumi.Input[int]] = None,
            cputype: Optional[pulumi.Input[str]] = None,
            entrypoints: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            env: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            execs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            image: Optional[pulumi.Input[str]] = None,
            memorymb: Optional[pulumi.Input[int]] = None,
            mounts: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['MachineMountArgs']]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            privateip: Optional[pulumi.Input[str]] = None,
            region: Optional[pulumi.Input[str]] = None,
            services: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['MachineServiceArgs']]]]] = None) -> 'Machine':
        """
        Get an existing Machine resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] app: fly app
        :param pulumi.Input[Sequence[pulumi.Input[str]]] cmds: cmd
        :param pulumi.Input[int] cpus: cpu count
        :param pulumi.Input[str] cputype: cpu type
        :param pulumi.Input[Sequence[pulumi.Input[str]]] entrypoints: image entrypoint
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] env: Optional environment variables, keys and values must be strings
        :param pulumi.Input[Sequence[pulumi.Input[str]]] execs: exec command
        :param pulumi.Input[str] image: docker image
        :param pulumi.Input[int] memorymb: memory mb
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['MachineMountArgs']]]] mounts: Volume mounts
        :param pulumi.Input[str] name: machine name
        :param pulumi.Input[str] privateip: Private IP
        :param pulumi.Input[str] region: machine region
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['MachineServiceArgs']]]] services: services
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _MachineState.__new__(_MachineState)

        __props__.__dict__["app"] = app
        __props__.__dict__["cmds"] = cmds
        __props__.__dict__["cpus"] = cpus
        __props__.__dict__["cputype"] = cputype
        __props__.__dict__["entrypoints"] = entrypoints
        __props__.__dict__["env"] = env
        __props__.__dict__["execs"] = execs
        __props__.__dict__["image"] = image
        __props__.__dict__["memorymb"] = memorymb
        __props__.__dict__["mounts"] = mounts
        __props__.__dict__["name"] = name
        __props__.__dict__["privateip"] = privateip
        __props__.__dict__["region"] = region
        __props__.__dict__["services"] = services
        return Machine(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def app(self) -> pulumi.Output[str]:
        """
        fly app
        """
        return pulumi.get(self, "app")

    @property
    @pulumi.getter
    def cmds(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        cmd
        """
        return pulumi.get(self, "cmds")

    @property
    @pulumi.getter
    def cpus(self) -> pulumi.Output[int]:
        """
        cpu count
        """
        return pulumi.get(self, "cpus")

    @property
    @pulumi.getter
    def cputype(self) -> pulumi.Output[str]:
        """
        cpu type
        """
        return pulumi.get(self, "cputype")

    @property
    @pulumi.getter
    def entrypoints(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        image entrypoint
        """
        return pulumi.get(self, "entrypoints")

    @property
    @pulumi.getter
    def env(self) -> pulumi.Output[Mapping[str, str]]:
        """
        Optional environment variables, keys and values must be strings
        """
        return pulumi.get(self, "env")

    @property
    @pulumi.getter
    def execs(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        exec command
        """
        return pulumi.get(self, "execs")

    @property
    @pulumi.getter
    def image(self) -> pulumi.Output[str]:
        """
        docker image
        """
        return pulumi.get(self, "image")

    @property
    @pulumi.getter
    def memorymb(self) -> pulumi.Output[int]:
        """
        memory mb
        """
        return pulumi.get(self, "memorymb")

    @property
    @pulumi.getter
    def mounts(self) -> pulumi.Output[Optional[Sequence['outputs.MachineMount']]]:
        """
        Volume mounts
        """
        return pulumi.get(self, "mounts")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        machine name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def privateip(self) -> pulumi.Output[str]:
        """
        Private IP
        """
        return pulumi.get(self, "privateip")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        machine region
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter
    def services(self) -> pulumi.Output[Optional[Sequence['outputs.MachineService']]]:
        """
        services
        """
        return pulumi.get(self, "services")
