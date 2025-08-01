// *** WARNING: this file was generated by pulumi-language-dotnet. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace ediri.Fly.Inputs
{

    public sealed class MachineServicePortGetArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// For a port range, the last port to listen on
        /// </summary>
        [Input("endPort")]
        public Input<int>? EndPort { get; set; }

        /// <summary>
        /// Automatically redirect to HTTPS on "http" handler
        /// </summary>
        [Input("forceHttps")]
        public Input<bool>? ForceHttps { get; set; }

        [Input("handlers")]
        private InputList<string>? _handlers;

        /// <summary>
        /// How the edge should process requests; ex empty, or `tls` to attach app's certificate
        /// </summary>
        public InputList<string> Handlers
        {
            get => _handlers ?? (_handlers = new InputList<string>());
            set => _handlers = value;
        }

        /// <summary>
        /// Mapped external port number, either `port` or `start_port` and `end_port` must be set.
        /// </summary>
        [Input("port")]
        public Input<int>? Port { get; set; }

        /// <summary>
        /// For a port range, the first port to listen on.
        /// </summary>
        [Input("startPort")]
        public Input<int>? StartPort { get; set; }

        public MachineServicePortGetArgs()
        {
        }
        public static new MachineServicePortGetArgs Empty => new MachineServicePortGetArgs();
    }
}
