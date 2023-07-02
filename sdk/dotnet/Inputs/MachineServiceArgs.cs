// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace ediri.Fly.Inputs
{

    public sealed class MachineServiceArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Port application listens on internally
        /// </summary>
        [Input("internalPort", required: true)]
        public Input<int> InternalPort { get; set; } = null!;

        [Input("ports", required: true)]
        private InputList<Inputs.MachineServicePortArgs>? _ports;

        /// <summary>
        /// External ports and handlers
        /// </summary>
        public InputList<Inputs.MachineServicePortArgs> Ports
        {
            get => _ports ?? (_ports = new InputList<Inputs.MachineServicePortArgs>());
            set => _ports = value;
        }

        /// <summary>
        /// network protocol
        /// </summary>
        [Input("protocol", required: true)]
        public Input<string> Protocol { get; set; } = null!;

        public MachineServiceArgs()
        {
        }
        public static new MachineServiceArgs Empty => new MachineServiceArgs();
    }
}
