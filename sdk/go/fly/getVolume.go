// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package fly

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Fly volume resource
func LookupVolume(ctx *pulumi.Context, args *LookupVolumeArgs, opts ...pulumi.InvokeOption) (*LookupVolumeResult, error) {
	opts = pkgInvokeDefaultOpts(opts)
	var rv LookupVolumeResult
	err := ctx.Invoke("fly:index/getVolume:getVolume", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getVolume.
type LookupVolumeArgs struct {
	// Name of app attached to
	App string `pulumi:"app"`
	// ID of volume
	Id string `pulumi:"id"`
}

// A collection of values returned by getVolume.
type LookupVolumeResult struct {
	// Name of app attached to
	App string `pulumi:"app"`
	// ID of volume
	Id string `pulumi:"id"`
	// name
	Name string `pulumi:"name"`
	// region
	Region string `pulumi:"region"`
	// Size of volume in GB
	Size int `pulumi:"size"`
}

func LookupVolumeOutput(ctx *pulumi.Context, args LookupVolumeOutputArgs, opts ...pulumi.InvokeOption) LookupVolumeResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupVolumeResult, error) {
			args := v.(LookupVolumeArgs)
			r, err := LookupVolume(ctx, &args, opts...)
			var s LookupVolumeResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupVolumeResultOutput)
}

// A collection of arguments for invoking getVolume.
type LookupVolumeOutputArgs struct {
	// Name of app attached to
	App pulumi.StringInput `pulumi:"app"`
	// ID of volume
	Id pulumi.StringInput `pulumi:"id"`
}

func (LookupVolumeOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupVolumeArgs)(nil)).Elem()
}

// A collection of values returned by getVolume.
type LookupVolumeResultOutput struct{ *pulumi.OutputState }

func (LookupVolumeResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupVolumeResult)(nil)).Elem()
}

func (o LookupVolumeResultOutput) ToLookupVolumeResultOutput() LookupVolumeResultOutput {
	return o
}

func (o LookupVolumeResultOutput) ToLookupVolumeResultOutputWithContext(ctx context.Context) LookupVolumeResultOutput {
	return o
}

// Name of app attached to
func (o LookupVolumeResultOutput) App() pulumi.StringOutput {
	return o.ApplyT(func(v LookupVolumeResult) string { return v.App }).(pulumi.StringOutput)
}

// ID of volume
func (o LookupVolumeResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupVolumeResult) string { return v.Id }).(pulumi.StringOutput)
}

// name
func (o LookupVolumeResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v LookupVolumeResult) string { return v.Name }).(pulumi.StringOutput)
}

// region
func (o LookupVolumeResultOutput) Region() pulumi.StringOutput {
	return o.ApplyT(func(v LookupVolumeResult) string { return v.Region }).(pulumi.StringOutput)
}

// Size of volume in GB
func (o LookupVolumeResultOutput) Size() pulumi.IntOutput {
	return o.ApplyT(func(v LookupVolumeResult) int { return v.Size }).(pulumi.IntOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupVolumeResultOutput{})
}
