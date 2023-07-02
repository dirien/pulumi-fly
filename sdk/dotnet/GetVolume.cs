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
    public static class GetVolume
    {
        /// <summary>
        /// Fly volume resource
        /// </summary>
        public static Task<GetVolumeResult> InvokeAsync(GetVolumeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetVolumeResult>("fly:index/getVolume:getVolume", args ?? new GetVolumeArgs(), options.WithDefaults());

        /// <summary>
        /// Fly volume resource
        /// </summary>
        public static Output<GetVolumeResult> Invoke(GetVolumeInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetVolumeResult>("fly:index/getVolume:getVolume", args ?? new GetVolumeInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetVolumeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Name of app attached to
        /// </summary>
        [Input("app", required: true)]
        public string App { get; set; } = null!;

        /// <summary>
        /// ID of volume
        /// </summary>
        [Input("id", required: true)]
        public string Id { get; set; } = null!;

        public GetVolumeArgs()
        {
        }
        public static new GetVolumeArgs Empty => new GetVolumeArgs();
    }

    public sealed class GetVolumeInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Name of app attached to
        /// </summary>
        [Input("app", required: true)]
        public Input<string> App { get; set; } = null!;

        /// <summary>
        /// ID of volume
        /// </summary>
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        public GetVolumeInvokeArgs()
        {
        }
        public static new GetVolumeInvokeArgs Empty => new GetVolumeInvokeArgs();
    }


    [OutputType]
    public sealed class GetVolumeResult
    {
        /// <summary>
        /// Name of app attached to
        /// </summary>
        public readonly string App;
        /// <summary>
        /// ID of volume
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// name
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// region
        /// </summary>
        public readonly string Region;
        /// <summary>
        /// Size of volume in GB
        /// </summary>
        public readonly int Size;

        [OutputConstructor]
        private GetVolumeResult(
            string app,

            string id,

            string name,

            string region,

            int size)
        {
            App = app;
            Id = id;
            Name = name;
            Region = region;
            Size = size;
        }
    }
}
