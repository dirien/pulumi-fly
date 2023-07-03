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
    /// <summary>
    /// Fly app resource
    /// 
    /// ## Example Usage
    /// 
    /// ## Import
    /// 
    /// &lt;break&gt;&lt;break&gt;```sh&lt;break&gt; $ pulumi import fly:index/app:App exampleApp &lt;app_id&gt; &lt;break&gt;```&lt;break&gt;&lt;break&gt;
    /// </summary>
    [FlyResourceType("fly:index/app:App")]
    public partial class App : global::Pulumi.CustomResource
    {
        /// <summary>
        /// readonly appUrl
        /// </summary>
        [Output("appurl")]
        public Output<string> Appurl { get; private set; } = null!;

        /// <summary>
        /// Name of application
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// Optional org slug to operate upon
        /// </summary>
        [Output("org")]
        public Output<string> Org { get; private set; } = null!;

        /// <summary>
        /// readonly orgid
        /// </summary>
        [Output("orgid")]
        public Output<string> Orgid { get; private set; } = null!;


        /// <summary>
        /// Create a App resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public App(string name, AppArgs? args = null, CustomResourceOptions? options = null)
            : base("fly:index/app:App", name, args ?? new AppArgs(), MakeResourceOptions(options, ""))
        {
        }

        private App(string name, Input<string> id, AppState? state = null, CustomResourceOptions? options = null)
            : base("fly:index/app:App", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                PluginDownloadURL = "github://api.github.com/dirien/pulumi-fly",
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing App resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static App Get(string name, Input<string> id, AppState? state = null, CustomResourceOptions? options = null)
        {
            return new App(name, id, state, options);
        }
    }

    public sealed class AppArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Name of application
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// Optional org slug to operate upon
        /// </summary>
        [Input("org")]
        public Input<string>? Org { get; set; }

        public AppArgs()
        {
        }
        public static new AppArgs Empty => new AppArgs();
    }

    public sealed class AppState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// readonly appUrl
        /// </summary>
        [Input("appurl")]
        public Input<string>? Appurl { get; set; }

        /// <summary>
        /// Name of application
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// Optional org slug to operate upon
        /// </summary>
        [Input("org")]
        public Input<string>? Org { get; set; }

        /// <summary>
        /// readonly orgid
        /// </summary>
        [Input("orgid")]
        public Input<string>? Orgid { get; set; }

        public AppState()
        {
        }
        public static new AppState Empty => new AppState();
    }
}
