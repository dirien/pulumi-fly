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

// Fly certificate resource
type Cert struct {
	pulumi.CustomResourceState

	// The App this resource will be created in
	App                       pulumi.StringOutput `pulumi:"app"`
	Check                     pulumi.BoolOutput   `pulumi:"check"`
	DnsValidationHostname     pulumi.StringOutput `pulumi:"dnsValidationHostname"`
	DnsValidationInstructions pulumi.StringOutput `pulumi:"dnsValidationInstructions"`
	DnsValidationTarget       pulumi.StringOutput `pulumi:"dnsValidationTarget"`
	Hostname                  pulumi.StringOutput `pulumi:"hostname"`
}

// NewCert registers a new resource with the given unique name, arguments, and options.
func NewCert(ctx *pulumi.Context,
	name string, args *CertArgs, opts ...pulumi.ResourceOption) (*Cert, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.App == nil {
		return nil, errors.New("invalid value for required argument 'App'")
	}
	if args.Hostname == nil {
		return nil, errors.New("invalid value for required argument 'Hostname'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Cert
	err := ctx.RegisterResource("fly:index/cert:Cert", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetCert gets an existing Cert resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetCert(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *CertState, opts ...pulumi.ResourceOption) (*Cert, error) {
	var resource Cert
	err := ctx.ReadResource("fly:index/cert:Cert", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Cert resources.
type certState struct {
	// The App this resource will be created in
	App                       *string `pulumi:"app"`
	Check                     *bool   `pulumi:"check"`
	DnsValidationHostname     *string `pulumi:"dnsValidationHostname"`
	DnsValidationInstructions *string `pulumi:"dnsValidationInstructions"`
	DnsValidationTarget       *string `pulumi:"dnsValidationTarget"`
	Hostname                  *string `pulumi:"hostname"`
}

type CertState struct {
	// The App this resource will be created in
	App                       pulumi.StringPtrInput
	Check                     pulumi.BoolPtrInput
	DnsValidationHostname     pulumi.StringPtrInput
	DnsValidationInstructions pulumi.StringPtrInput
	DnsValidationTarget       pulumi.StringPtrInput
	Hostname                  pulumi.StringPtrInput
}

func (CertState) ElementType() reflect.Type {
	return reflect.TypeOf((*certState)(nil)).Elem()
}

type certArgs struct {
	// The App this resource will be created in
	App      string `pulumi:"app"`
	Hostname string `pulumi:"hostname"`
}

// The set of arguments for constructing a Cert resource.
type CertArgs struct {
	// The App this resource will be created in
	App      pulumi.StringInput
	Hostname pulumi.StringInput
}

func (CertArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*certArgs)(nil)).Elem()
}

type CertInput interface {
	pulumi.Input

	ToCertOutput() CertOutput
	ToCertOutputWithContext(ctx context.Context) CertOutput
}

func (*Cert) ElementType() reflect.Type {
	return reflect.TypeOf((**Cert)(nil)).Elem()
}

func (i *Cert) ToCertOutput() CertOutput {
	return i.ToCertOutputWithContext(context.Background())
}

func (i *Cert) ToCertOutputWithContext(ctx context.Context) CertOutput {
	return pulumi.ToOutputWithContext(ctx, i).(CertOutput)
}

// CertArrayInput is an input type that accepts CertArray and CertArrayOutput values.
// You can construct a concrete instance of `CertArrayInput` via:
//
//	CertArray{ CertArgs{...} }
type CertArrayInput interface {
	pulumi.Input

	ToCertArrayOutput() CertArrayOutput
	ToCertArrayOutputWithContext(context.Context) CertArrayOutput
}

type CertArray []CertInput

func (CertArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Cert)(nil)).Elem()
}

func (i CertArray) ToCertArrayOutput() CertArrayOutput {
	return i.ToCertArrayOutputWithContext(context.Background())
}

func (i CertArray) ToCertArrayOutputWithContext(ctx context.Context) CertArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(CertArrayOutput)
}

// CertMapInput is an input type that accepts CertMap and CertMapOutput values.
// You can construct a concrete instance of `CertMapInput` via:
//
//	CertMap{ "key": CertArgs{...} }
type CertMapInput interface {
	pulumi.Input

	ToCertMapOutput() CertMapOutput
	ToCertMapOutputWithContext(context.Context) CertMapOutput
}

type CertMap map[string]CertInput

func (CertMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Cert)(nil)).Elem()
}

func (i CertMap) ToCertMapOutput() CertMapOutput {
	return i.ToCertMapOutputWithContext(context.Background())
}

func (i CertMap) ToCertMapOutputWithContext(ctx context.Context) CertMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(CertMapOutput)
}

type CertOutput struct{ *pulumi.OutputState }

func (CertOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Cert)(nil)).Elem()
}

func (o CertOutput) ToCertOutput() CertOutput {
	return o
}

func (o CertOutput) ToCertOutputWithContext(ctx context.Context) CertOutput {
	return o
}

// The App this resource will be created in
func (o CertOutput) App() pulumi.StringOutput {
	return o.ApplyT(func(v *Cert) pulumi.StringOutput { return v.App }).(pulumi.StringOutput)
}

func (o CertOutput) Check() pulumi.BoolOutput {
	return o.ApplyT(func(v *Cert) pulumi.BoolOutput { return v.Check }).(pulumi.BoolOutput)
}

func (o CertOutput) DnsValidationHostname() pulumi.StringOutput {
	return o.ApplyT(func(v *Cert) pulumi.StringOutput { return v.DnsValidationHostname }).(pulumi.StringOutput)
}

func (o CertOutput) DnsValidationInstructions() pulumi.StringOutput {
	return o.ApplyT(func(v *Cert) pulumi.StringOutput { return v.DnsValidationInstructions }).(pulumi.StringOutput)
}

func (o CertOutput) DnsValidationTarget() pulumi.StringOutput {
	return o.ApplyT(func(v *Cert) pulumi.StringOutput { return v.DnsValidationTarget }).(pulumi.StringOutput)
}

func (o CertOutput) Hostname() pulumi.StringOutput {
	return o.ApplyT(func(v *Cert) pulumi.StringOutput { return v.Hostname }).(pulumi.StringOutput)
}

type CertArrayOutput struct{ *pulumi.OutputState }

func (CertArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Cert)(nil)).Elem()
}

func (o CertArrayOutput) ToCertArrayOutput() CertArrayOutput {
	return o
}

func (o CertArrayOutput) ToCertArrayOutputWithContext(ctx context.Context) CertArrayOutput {
	return o
}

func (o CertArrayOutput) Index(i pulumi.IntInput) CertOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *Cert {
		return vs[0].([]*Cert)[vs[1].(int)]
	}).(CertOutput)
}

type CertMapOutput struct{ *pulumi.OutputState }

func (CertMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Cert)(nil)).Elem()
}

func (o CertMapOutput) ToCertMapOutput() CertMapOutput {
	return o
}

func (o CertMapOutput) ToCertMapOutputWithContext(ctx context.Context) CertMapOutput {
	return o
}

func (o CertMapOutput) MapIndex(k pulumi.StringInput) CertOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *Cert {
		return vs[0].(map[string]*Cert)[vs[1].(string)]
	}).(CertOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*CertInput)(nil)).Elem(), &Cert{})
	pulumi.RegisterInputType(reflect.TypeOf((*CertArrayInput)(nil)).Elem(), CertArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*CertMapInput)(nil)).Elem(), CertMap{})
	pulumi.RegisterOutputType(CertOutput{})
	pulumi.RegisterOutputType(CertArrayOutput{})
	pulumi.RegisterOutputType(CertMapOutput{})
}
