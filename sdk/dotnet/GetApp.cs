// *** WARNING: this file was generated by pulumi-language-dotnet. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace ediri.Fly
{
    public static class GetApp
    {
        public static Task<GetAppResult> InvokeAsync(GetAppArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetAppResult>("fly:index/getApp:getApp", args ?? new GetAppArgs(), options.WithDefaults());

        public static Output<GetAppResult> Invoke(GetAppInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetAppResult>("fly:index/getApp:getApp", args ?? new GetAppInvokeArgs(), options.WithDefaults());

        public static Output<GetAppResult> Invoke(GetAppInvokeArgs args, InvokeOutputOptions options)
            => global::Pulumi.Deployment.Instance.Invoke<GetAppResult>("fly:index/getApp:getApp", args ?? new GetAppInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetAppArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Name of app
        /// </summary>
        [Input("name", required: true)]
        public string Name { get; set; } = null!;

        public GetAppArgs()
        {
        }
        public static new GetAppArgs Empty => new GetAppArgs();
    }

    public sealed class GetAppInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Name of app
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        public GetAppInvokeArgs()
        {
        }
        public static new GetAppInvokeArgs Empty => new GetAppInvokeArgs();
    }


    [OutputType]
    public sealed class GetAppResult
    {
        public readonly string Appurl;
        public readonly string Currentrelease;
        public readonly bool Deployed;
        public readonly ImmutableArray<string> Healthchecks;
        public readonly string Hostname;
        /// <summary>
        /// The ID of this resource.
        /// </summary>
        public readonly string Id;
        public readonly ImmutableArray<string> Ipaddresses;
        /// <summary>
        /// Name of app
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// A shared ipv4 address, automatically attached in certain conditions or if explicitly requested
        /// </summary>
        public readonly string Sharedipaddress;
        public readonly string Status;

        [OutputConstructor]
        private GetAppResult(
            string appurl,

            string currentrelease,

            bool deployed,

            ImmutableArray<string> healthchecks,

            string hostname,

            string id,

            ImmutableArray<string> ipaddresses,

            string name,

            string sharedipaddress,

            string status)
        {
            Appurl = appurl;
            Currentrelease = currentrelease;
            Deployed = deployed;
            Healthchecks = healthchecks;
            Hostname = hostname;
            Id = id;
            Ipaddresses = ipaddresses;
            Name = name;
            Sharedipaddress = sharedipaddress;
            Status = status;
        }
    }
}
