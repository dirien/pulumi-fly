// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace ediri.Fly
{
    public static class GetIp
    {
        /// <summary>
        /// Fly ip data source
        /// </summary>
        public static Task<GetIpResult> InvokeAsync(GetIpArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetIpResult>("fly:index/getIp:getIp", args ?? new GetIpArgs(), options.WithDefaults());

        /// <summary>
        /// Fly ip data source
        /// </summary>
        public static Output<GetIpResult> Invoke(GetIpInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetIpResult>("fly:index/getIp:getIp", args ?? new GetIpInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetIpArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// IP address
        /// </summary>
        [Input("address", required: true)]
        public string Address { get; set; } = null!;

        /// <summary>
        /// Name of app attached to
        /// </summary>
        [Input("app", required: true)]
        public string App { get; set; } = null!;

        public GetIpArgs()
        {
        }
        public static new GetIpArgs Empty => new GetIpArgs();
    }

    public sealed class GetIpInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// IP address
        /// </summary>
        [Input("address", required: true)]
        public Input<string> Address { get; set; } = null!;

        /// <summary>
        /// Name of app attached to
        /// </summary>
        [Input("app", required: true)]
        public Input<string> App { get; set; } = null!;

        public GetIpInvokeArgs()
        {
        }
        public static new GetIpInvokeArgs Empty => new GetIpInvokeArgs();
    }


    [OutputType]
    public sealed class GetIpResult
    {
        /// <summary>
        /// IP address
        /// </summary>
        public readonly string Address;
        /// <summary>
        /// Name of app attached to
        /// </summary>
        public readonly string App;
        /// <summary>
        /// ID of address
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// region
        /// </summary>
        public readonly string Region;
        /// <summary>
        /// v4 or v6
        /// </summary>
        public readonly string Type;

        [OutputConstructor]
        private GetIpResult(
            string address,

            string app,

            string id,

            string region,

            string type)
        {
            Address = address;
            App = app;
            Id = id;
            Region = region;
            Type = type;
        }
    }
}
