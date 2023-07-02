// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";

export interface MachineMount {
    encrypted: boolean;
    /**
     * Path for volume to be mounted on vm
     */
    path: string;
    sizeGb: number;
    /**
     * Name or ID of volume
     */
    volume: string;
}

export interface MachineService {
    /**
     * Port application listens on internally
     */
    internalPort: number;
    /**
     * External ports and handlers
     */
    ports: outputs.MachineServicePort[];
    /**
     * network protocol
     */
    protocol: string;
}

export interface MachineServicePort {
    handlers?: string[];
    port: number;
}
