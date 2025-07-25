// Code generated by pulumi-language-go DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package fly

import (
	"context"
	"reflect"

	"errors"
	"github.com/dirien/pulumi-fly/sdk/go/fly/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type Ip struct {
	pulumi.CustomResourceState

	// Empty if using `sharedV4`
	Address pulumi.StringOutput `pulumi:"address"`
	// The App this resource will be created in
	App pulumi.StringOutput `pulumi:"app"`
	// Fly region, ex `ord`, `sin`, `mad`
	Region pulumi.StringOutput `pulumi:"region"`
	// One of the following values (by regex): `^(v4|v6|private_v6)$`
	Type pulumi.StringOutput `pulumi:"type"`
}

// NewIp registers a new resource with the given unique name, arguments, and options.
func NewIp(ctx *pulumi.Context,
	name string, args *IpArgs, opts ...pulumi.ResourceOption) (*Ip, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.App == nil {
		return nil, errors.New("invalid value for required argument 'App'")
	}
	if args.Type == nil {
		return nil, errors.New("invalid value for required argument 'Type'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Ip
	err := ctx.RegisterResource("fly:index/ip:Ip", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetIp gets an existing Ip resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetIp(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *IpState, opts ...pulumi.ResourceOption) (*Ip, error) {
	var resource Ip
	err := ctx.ReadResource("fly:index/ip:Ip", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Ip resources.
type ipState struct {
	// Empty if using `sharedV4`
	Address *string `pulumi:"address"`
	// The App this resource will be created in
	App *string `pulumi:"app"`
	// Fly region, ex `ord`, `sin`, `mad`
	Region *string `pulumi:"region"`
	// One of the following values (by regex): `^(v4|v6|private_v6)$`
	Type *string `pulumi:"type"`
}

type IpState struct {
	// Empty if using `sharedV4`
	Address pulumi.StringPtrInput
	// The App this resource will be created in
	App pulumi.StringPtrInput
	// Fly region, ex `ord`, `sin`, `mad`
	Region pulumi.StringPtrInput
	// One of the following values (by regex): `^(v4|v6|private_v6)$`
	Type pulumi.StringPtrInput
}

func (IpState) ElementType() reflect.Type {
	return reflect.TypeOf((*ipState)(nil)).Elem()
}

type ipArgs struct {
	// The App this resource will be created in
	App string `pulumi:"app"`
	// Fly region, ex `ord`, `sin`, `mad`
	Region *string `pulumi:"region"`
	// One of the following values (by regex): `^(v4|v6|private_v6)$`
	Type string `pulumi:"type"`
}

// The set of arguments for constructing a Ip resource.
type IpArgs struct {
	// The App this resource will be created in
	App pulumi.StringInput
	// Fly region, ex `ord`, `sin`, `mad`
	Region pulumi.StringPtrInput
	// One of the following values (by regex): `^(v4|v6|private_v6)$`
	Type pulumi.StringInput
}

func (IpArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*ipArgs)(nil)).Elem()
}

type IpInput interface {
	pulumi.Input

	ToIpOutput() IpOutput
	ToIpOutputWithContext(ctx context.Context) IpOutput
}

func (*Ip) ElementType() reflect.Type {
	return reflect.TypeOf((**Ip)(nil)).Elem()
}

func (i *Ip) ToIpOutput() IpOutput {
	return i.ToIpOutputWithContext(context.Background())
}

func (i *Ip) ToIpOutputWithContext(ctx context.Context) IpOutput {
	return pulumi.ToOutputWithContext(ctx, i).(IpOutput)
}

// IpArrayInput is an input type that accepts IpArray and IpArrayOutput values.
// You can construct a concrete instance of `IpArrayInput` via:
//
//	IpArray{ IpArgs{...} }
type IpArrayInput interface {
	pulumi.Input

	ToIpArrayOutput() IpArrayOutput
	ToIpArrayOutputWithContext(context.Context) IpArrayOutput
}

type IpArray []IpInput

func (IpArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Ip)(nil)).Elem()
}

func (i IpArray) ToIpArrayOutput() IpArrayOutput {
	return i.ToIpArrayOutputWithContext(context.Background())
}

func (i IpArray) ToIpArrayOutputWithContext(ctx context.Context) IpArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(IpArrayOutput)
}

// IpMapInput is an input type that accepts IpMap and IpMapOutput values.
// You can construct a concrete instance of `IpMapInput` via:
//
//	IpMap{ "key": IpArgs{...} }
type IpMapInput interface {
	pulumi.Input

	ToIpMapOutput() IpMapOutput
	ToIpMapOutputWithContext(context.Context) IpMapOutput
}

type IpMap map[string]IpInput

func (IpMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Ip)(nil)).Elem()
}

func (i IpMap) ToIpMapOutput() IpMapOutput {
	return i.ToIpMapOutputWithContext(context.Background())
}

func (i IpMap) ToIpMapOutputWithContext(ctx context.Context) IpMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(IpMapOutput)
}

type IpOutput struct{ *pulumi.OutputState }

func (IpOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Ip)(nil)).Elem()
}

func (o IpOutput) ToIpOutput() IpOutput {
	return o
}

func (o IpOutput) ToIpOutputWithContext(ctx context.Context) IpOutput {
	return o
}

// Empty if using `sharedV4`
func (o IpOutput) Address() pulumi.StringOutput {
	return o.ApplyT(func(v *Ip) pulumi.StringOutput { return v.Address }).(pulumi.StringOutput)
}

// The App this resource will be created in
func (o IpOutput) App() pulumi.StringOutput {
	return o.ApplyT(func(v *Ip) pulumi.StringOutput { return v.App }).(pulumi.StringOutput)
}

// Fly region, ex `ord`, `sin`, `mad`
func (o IpOutput) Region() pulumi.StringOutput {
	return o.ApplyT(func(v *Ip) pulumi.StringOutput { return v.Region }).(pulumi.StringOutput)
}

// One of the following values (by regex): `^(v4|v6|private_v6)$`
func (o IpOutput) Type() pulumi.StringOutput {
	return o.ApplyT(func(v *Ip) pulumi.StringOutput { return v.Type }).(pulumi.StringOutput)
}

type IpArrayOutput struct{ *pulumi.OutputState }

func (IpArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Ip)(nil)).Elem()
}

func (o IpArrayOutput) ToIpArrayOutput() IpArrayOutput {
	return o
}

func (o IpArrayOutput) ToIpArrayOutputWithContext(ctx context.Context) IpArrayOutput {
	return o
}

func (o IpArrayOutput) Index(i pulumi.IntInput) IpOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *Ip {
		return vs[0].([]*Ip)[vs[1].(int)]
	}).(IpOutput)
}

type IpMapOutput struct{ *pulumi.OutputState }

func (IpMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Ip)(nil)).Elem()
}

func (o IpMapOutput) ToIpMapOutput() IpMapOutput {
	return o
}

func (o IpMapOutput) ToIpMapOutputWithContext(ctx context.Context) IpMapOutput {
	return o
}

func (o IpMapOutput) MapIndex(k pulumi.StringInput) IpOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *Ip {
		return vs[0].(map[string]*Ip)[vs[1].(string)]
	}).(IpOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*IpInput)(nil)).Elem(), &Ip{})
	pulumi.RegisterInputType(reflect.TypeOf((*IpArrayInput)(nil)).Elem(), IpArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*IpMapInput)(nil)).Elem(), IpMap{})
	pulumi.RegisterOutputType(IpOutput{})
	pulumi.RegisterOutputType(IpArrayOutput{})
	pulumi.RegisterOutputType(IpMapOutput{})
}
