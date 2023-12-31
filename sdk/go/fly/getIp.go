// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package fly

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Fly ip data source
func LookupIp(ctx *pulumi.Context, args *LookupIpArgs, opts ...pulumi.InvokeOption) (*LookupIpResult, error) {
	opts = pkgInvokeDefaultOpts(opts)
	var rv LookupIpResult
	err := ctx.Invoke("fly:index/getIp:getIp", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getIp.
type LookupIpArgs struct {
	// IP address
	Address string `pulumi:"address"`
	// Name of app attached to
	App string `pulumi:"app"`
}

// A collection of values returned by getIp.
type LookupIpResult struct {
	// IP address
	Address string `pulumi:"address"`
	// Name of app attached to
	App string `pulumi:"app"`
	// ID of address
	Id string `pulumi:"id"`
	// region
	Region string `pulumi:"region"`
	// v4 or v6
	Type string `pulumi:"type"`
}

func LookupIpOutput(ctx *pulumi.Context, args LookupIpOutputArgs, opts ...pulumi.InvokeOption) LookupIpResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupIpResult, error) {
			args := v.(LookupIpArgs)
			r, err := LookupIp(ctx, &args, opts...)
			var s LookupIpResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupIpResultOutput)
}

// A collection of arguments for invoking getIp.
type LookupIpOutputArgs struct {
	// IP address
	Address pulumi.StringInput `pulumi:"address"`
	// Name of app attached to
	App pulumi.StringInput `pulumi:"app"`
}

func (LookupIpOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupIpArgs)(nil)).Elem()
}

// A collection of values returned by getIp.
type LookupIpResultOutput struct{ *pulumi.OutputState }

func (LookupIpResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupIpResult)(nil)).Elem()
}

func (o LookupIpResultOutput) ToLookupIpResultOutput() LookupIpResultOutput {
	return o
}

func (o LookupIpResultOutput) ToLookupIpResultOutputWithContext(ctx context.Context) LookupIpResultOutput {
	return o
}

// IP address
func (o LookupIpResultOutput) Address() pulumi.StringOutput {
	return o.ApplyT(func(v LookupIpResult) string { return v.Address }).(pulumi.StringOutput)
}

// Name of app attached to
func (o LookupIpResultOutput) App() pulumi.StringOutput {
	return o.ApplyT(func(v LookupIpResult) string { return v.App }).(pulumi.StringOutput)
}

// ID of address
func (o LookupIpResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupIpResult) string { return v.Id }).(pulumi.StringOutput)
}

// region
func (o LookupIpResultOutput) Region() pulumi.StringOutput {
	return o.ApplyT(func(v LookupIpResult) string { return v.Region }).(pulumi.StringOutput)
}

// v4 or v6
func (o LookupIpResultOutput) Type() pulumi.StringOutput {
	return o.ApplyT(func(v LookupIpResult) string { return v.Type }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupIpResultOutput{})
}
