// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace ediri.Fly.Outputs
{

    [OutputType]
    public sealed class MachineService
    {
        /// <summary>
        /// Port application listens on internally
        /// </summary>
        public readonly int InternalPort;
        /// <summary>
        /// External ports and handlers
        /// </summary>
        public readonly ImmutableArray<Outputs.MachineServicePort> Ports;
        /// <summary>
        /// network protocol
        /// </summary>
        public readonly string Protocol;

        [OutputConstructor]
        private MachineService(
            int internalPort,

            ImmutableArray<Outputs.MachineServicePort> ports,

            string protocol)
        {
            InternalPort = internalPort;
            Ports = ports;
            Protocol = protocol;
        }
    }
}