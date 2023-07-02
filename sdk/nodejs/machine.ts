// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * Fly machine resource
 *
 * ## Example Usage
 *
 * ## Import
 *
 * <break><break>```sh<break> $ pulumi import fly:index/machine:Machine exampleMachine <app_id>,<machine_id> <break>```<break><break>
 */
export class Machine extends pulumi.CustomResource {
    /**
     * Get an existing Machine resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: MachineState, opts?: pulumi.CustomResourceOptions): Machine {
        return new Machine(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'fly:index/machine:Machine';

    /**
     * Returns true if the given object is an instance of Machine.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Machine {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Machine.__pulumiType;
    }

    /**
     * fly app
     */
    public readonly app!: pulumi.Output<string>;
    /**
     * cmd
     */
    public readonly cmds!: pulumi.Output<string[] | undefined>;
    /**
     * cpu count
     */
    public readonly cpus!: pulumi.Output<number>;
    /**
     * cpu type
     */
    public readonly cputype!: pulumi.Output<string>;
    /**
     * image entrypoint
     */
    public readonly entrypoints!: pulumi.Output<string[] | undefined>;
    /**
     * Optional environment variables, keys and values must be strings
     */
    public readonly env!: pulumi.Output<{[key: string]: string}>;
    /**
     * exec command
     */
    public readonly execs!: pulumi.Output<string[] | undefined>;
    /**
     * docker image
     */
    public readonly image!: pulumi.Output<string>;
    /**
     * memory mb
     */
    public readonly memorymb!: pulumi.Output<number>;
    /**
     * Volume mounts
     */
    public readonly mounts!: pulumi.Output<outputs.MachineMount[] | undefined>;
    /**
     * machine name
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * Private IP
     */
    public /*out*/ readonly privateip!: pulumi.Output<string>;
    /**
     * machine region
     */
    public readonly region!: pulumi.Output<string>;
    /**
     * services
     */
    public readonly services!: pulumi.Output<outputs.MachineService[] | undefined>;

    /**
     * Create a Machine resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: MachineArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: MachineArgs | MachineState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as MachineState | undefined;
            resourceInputs["app"] = state ? state.app : undefined;
            resourceInputs["cmds"] = state ? state.cmds : undefined;
            resourceInputs["cpus"] = state ? state.cpus : undefined;
            resourceInputs["cputype"] = state ? state.cputype : undefined;
            resourceInputs["entrypoints"] = state ? state.entrypoints : undefined;
            resourceInputs["env"] = state ? state.env : undefined;
            resourceInputs["execs"] = state ? state.execs : undefined;
            resourceInputs["image"] = state ? state.image : undefined;
            resourceInputs["memorymb"] = state ? state.memorymb : undefined;
            resourceInputs["mounts"] = state ? state.mounts : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["privateip"] = state ? state.privateip : undefined;
            resourceInputs["region"] = state ? state.region : undefined;
            resourceInputs["services"] = state ? state.services : undefined;
        } else {
            const args = argsOrState as MachineArgs | undefined;
            if ((!args || args.app === undefined) && !opts.urn) {
                throw new Error("Missing required property 'app'");
            }
            if ((!args || args.image === undefined) && !opts.urn) {
                throw new Error("Missing required property 'image'");
            }
            if ((!args || args.region === undefined) && !opts.urn) {
                throw new Error("Missing required property 'region'");
            }
            resourceInputs["app"] = args ? args.app : undefined;
            resourceInputs["cmds"] = args ? args.cmds : undefined;
            resourceInputs["cpus"] = args ? args.cpus : undefined;
            resourceInputs["cputype"] = args ? args.cputype : undefined;
            resourceInputs["entrypoints"] = args ? args.entrypoints : undefined;
            resourceInputs["env"] = args ? args.env : undefined;
            resourceInputs["execs"] = args ? args.execs : undefined;
            resourceInputs["image"] = args ? args.image : undefined;
            resourceInputs["memorymb"] = args ? args.memorymb : undefined;
            resourceInputs["mounts"] = args ? args.mounts : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["region"] = args ? args.region : undefined;
            resourceInputs["services"] = args ? args.services : undefined;
            resourceInputs["privateip"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Machine.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Machine resources.
 */
export interface MachineState {
    /**
     * fly app
     */
    app?: pulumi.Input<string>;
    /**
     * cmd
     */
    cmds?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * cpu count
     */
    cpus?: pulumi.Input<number>;
    /**
     * cpu type
     */
    cputype?: pulumi.Input<string>;
    /**
     * image entrypoint
     */
    entrypoints?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Optional environment variables, keys and values must be strings
     */
    env?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * exec command
     */
    execs?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * docker image
     */
    image?: pulumi.Input<string>;
    /**
     * memory mb
     */
    memorymb?: pulumi.Input<number>;
    /**
     * Volume mounts
     */
    mounts?: pulumi.Input<pulumi.Input<inputs.MachineMount>[]>;
    /**
     * machine name
     */
    name?: pulumi.Input<string>;
    /**
     * Private IP
     */
    privateip?: pulumi.Input<string>;
    /**
     * machine region
     */
    region?: pulumi.Input<string>;
    /**
     * services
     */
    services?: pulumi.Input<pulumi.Input<inputs.MachineService>[]>;
}

/**
 * The set of arguments for constructing a Machine resource.
 */
export interface MachineArgs {
    /**
     * fly app
     */
    app: pulumi.Input<string>;
    /**
     * cmd
     */
    cmds?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * cpu count
     */
    cpus?: pulumi.Input<number>;
    /**
     * cpu type
     */
    cputype?: pulumi.Input<string>;
    /**
     * image entrypoint
     */
    entrypoints?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Optional environment variables, keys and values must be strings
     */
    env?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * exec command
     */
    execs?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * docker image
     */
    image: pulumi.Input<string>;
    /**
     * memory mb
     */
    memorymb?: pulumi.Input<number>;
    /**
     * Volume mounts
     */
    mounts?: pulumi.Input<pulumi.Input<inputs.MachineMount>[]>;
    /**
     * machine name
     */
    name?: pulumi.Input<string>;
    /**
     * machine region
     */
    region: pulumi.Input<string>;
    /**
     * services
     */
    services?: pulumi.Input<pulumi.Input<inputs.MachineService>[]>;
}
