// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";

export interface MachineMount {
    /**
     * Path for volume to be mounted on vm, ex: `/data`
     */
    path: string;
    /**
     * ID of volume
     */
    volume: string;
}

export interface MachineService {
    /**
     * Port the machine listens on
     */
    internalPort: number;
    /**
     * How the port is exposed
     */
    ports: outputs.MachineServicePort[];
    /**
     * `udp` or `tcp`
     */
    protocol: string;
}

export interface MachineServicePort {
    /**
     * Automatically redirect to HTTPS on "http" handler
     */
    forceHttps: boolean;
    /**
     * How the edge should process requests; ex empty, or `tls` to attach app's certificate
     */
    handlers?: string[];
    /**
     * Mapped external port number
     */
    port: number;
}

