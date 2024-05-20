// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package config

import (
	"github.com/dirien/pulumi-fly/sdk/go/fly/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi/config"
)

var _ = internal.GetEnvOrDefault

// fly.io api token. If not set checks env for FLY_API_TOKEN
func GetFlyApiToken(ctx *pulumi.Context) string {
	return config.Get(ctx, "fly:flyApiToken")
}

// Where the provider should look to find the fly http endpoint
func GetFlyHttpEndpoint(ctx *pulumi.Context) string {
	return config.Get(ctx, "fly:flyHttpEndpoint")
}
