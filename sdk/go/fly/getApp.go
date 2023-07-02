// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package fly

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Retrieve info about graphql app
//
// ## Example Usage
func LookupApp(ctx *pulumi.Context, args *LookupAppArgs, opts ...pulumi.InvokeOption) (*LookupAppResult, error) {
	opts = pkgInvokeDefaultOpts(opts)
	var rv LookupAppResult
	err := ctx.Invoke("fly:index/getApp:getApp", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getApp.
type LookupAppArgs struct {
	// Name of app
	Name string `pulumi:"name"`
}

// A collection of values returned by getApp.
type LookupAppResult struct {
	Appurl         string   `pulumi:"appurl"`
	Currentrelease string   `pulumi:"currentrelease"`
	Deployed       bool     `pulumi:"deployed"`
	Healthchecks   []string `pulumi:"healthchecks"`
	Hostname       string   `pulumi:"hostname"`
	// The ID of this resource.
	Id          string   `pulumi:"id"`
	Ipaddresses []string `pulumi:"ipaddresses"`
	// Name of app
	Name   string `pulumi:"name"`
	Status string `pulumi:"status"`
}

func LookupAppOutput(ctx *pulumi.Context, args LookupAppOutputArgs, opts ...pulumi.InvokeOption) LookupAppResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupAppResult, error) {
			args := v.(LookupAppArgs)
			r, err := LookupApp(ctx, &args, opts...)
			var s LookupAppResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupAppResultOutput)
}

// A collection of arguments for invoking getApp.
type LookupAppOutputArgs struct {
	// Name of app
	Name pulumi.StringInput `pulumi:"name"`
}

func (LookupAppOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupAppArgs)(nil)).Elem()
}

// A collection of values returned by getApp.
type LookupAppResultOutput struct{ *pulumi.OutputState }

func (LookupAppResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupAppResult)(nil)).Elem()
}

func (o LookupAppResultOutput) ToLookupAppResultOutput() LookupAppResultOutput {
	return o
}

func (o LookupAppResultOutput) ToLookupAppResultOutputWithContext(ctx context.Context) LookupAppResultOutput {
	return o
}

func (o LookupAppResultOutput) Appurl() pulumi.StringOutput {
	return o.ApplyT(func(v LookupAppResult) string { return v.Appurl }).(pulumi.StringOutput)
}

func (o LookupAppResultOutput) Currentrelease() pulumi.StringOutput {
	return o.ApplyT(func(v LookupAppResult) string { return v.Currentrelease }).(pulumi.StringOutput)
}

func (o LookupAppResultOutput) Deployed() pulumi.BoolOutput {
	return o.ApplyT(func(v LookupAppResult) bool { return v.Deployed }).(pulumi.BoolOutput)
}

func (o LookupAppResultOutput) Healthchecks() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupAppResult) []string { return v.Healthchecks }).(pulumi.StringArrayOutput)
}

func (o LookupAppResultOutput) Hostname() pulumi.StringOutput {
	return o.ApplyT(func(v LookupAppResult) string { return v.Hostname }).(pulumi.StringOutput)
}

// The ID of this resource.
func (o LookupAppResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupAppResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o LookupAppResultOutput) Ipaddresses() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupAppResult) []string { return v.Ipaddresses }).(pulumi.StringArrayOutput)
}

// Name of app
func (o LookupAppResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v LookupAppResult) string { return v.Name }).(pulumi.StringOutput)
}

func (o LookupAppResultOutput) Status() pulumi.StringOutput {
	return o.ApplyT(func(v LookupAppResult) string { return v.Status }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupAppResultOutput{})
}