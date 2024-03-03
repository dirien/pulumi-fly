// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Fly certificate resource
 */
export class Cert extends pulumi.CustomResource {
    /**
     * Get an existing Cert resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: CertState, opts?: pulumi.CustomResourceOptions): Cert {
        return new Cert(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'fly:index/cert:Cert';

    /**
     * Returns true if the given object is an instance of Cert.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Cert {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Cert.__pulumiType;
    }

    /**
     * The App this resource will be created in
     */
    public readonly app!: pulumi.Output<string>;
    public /*out*/ readonly check!: pulumi.Output<boolean>;
    public /*out*/ readonly dnsValidationHostname!: pulumi.Output<string>;
    public /*out*/ readonly dnsValidationInstructions!: pulumi.Output<string>;
    public /*out*/ readonly dnsValidationTarget!: pulumi.Output<string>;
    public readonly hostname!: pulumi.Output<string>;

    /**
     * Create a Cert resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: CertArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: CertArgs | CertState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as CertState | undefined;
            resourceInputs["app"] = state ? state.app : undefined;
            resourceInputs["check"] = state ? state.check : undefined;
            resourceInputs["dnsValidationHostname"] = state ? state.dnsValidationHostname : undefined;
            resourceInputs["dnsValidationInstructions"] = state ? state.dnsValidationInstructions : undefined;
            resourceInputs["dnsValidationTarget"] = state ? state.dnsValidationTarget : undefined;
            resourceInputs["hostname"] = state ? state.hostname : undefined;
        } else {
            const args = argsOrState as CertArgs | undefined;
            if ((!args || args.app === undefined) && !opts.urn) {
                throw new Error("Missing required property 'app'");
            }
            if ((!args || args.hostname === undefined) && !opts.urn) {
                throw new Error("Missing required property 'hostname'");
            }
            resourceInputs["app"] = args ? args.app : undefined;
            resourceInputs["hostname"] = args ? args.hostname : undefined;
            resourceInputs["check"] = undefined /*out*/;
            resourceInputs["dnsValidationHostname"] = undefined /*out*/;
            resourceInputs["dnsValidationInstructions"] = undefined /*out*/;
            resourceInputs["dnsValidationTarget"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Cert.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Cert resources.
 */
export interface CertState {
    /**
     * The App this resource will be created in
     */
    app?: pulumi.Input<string>;
    check?: pulumi.Input<boolean>;
    dnsValidationHostname?: pulumi.Input<string>;
    dnsValidationInstructions?: pulumi.Input<string>;
    dnsValidationTarget?: pulumi.Input<string>;
    hostname?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Cert resource.
 */
export interface CertArgs {
    /**
     * The App this resource will be created in
     */
    app: pulumi.Input<string>;
    hostname: pulumi.Input<string>;
}
