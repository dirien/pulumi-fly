// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package fly

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-fly/sdk/go/fly/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type App struct {
	pulumi.CustomResourceState

	AppUrl pulumi.StringOutput `pulumi:"appUrl"`
	// Assign a shared ipv4 address to the app. Note that depending on conditions an app may get a shared ip automatically.
	AssignSharedIpAddress pulumi.BoolOutput `pulumi:"assignSharedIpAddress"`
	// Name of application
	Name pulumi.StringOutput `pulumi:"name"`
	// The name of the organization to generate the app in, ex: `personal` (your initial org)
	Org   pulumi.StringOutput `pulumi:"org"`
	OrgId pulumi.StringOutput `pulumi:"orgId"`
	// A shared ipv4 address, automatically attached in certain conditions or if explicitly requested
	SharedIpAddress pulumi.StringOutput `pulumi:"sharedIpAddress"`
}

// NewApp registers a new resource with the given unique name, arguments, and options.
func NewApp(ctx *pulumi.Context,
	name string, args *AppArgs, opts ...pulumi.ResourceOption) (*App, error) {
	if args == nil {
		args = &AppArgs{}
	}

	opts = internal.PkgResourceDefaultOpts(opts)
	var resource App
	err := ctx.RegisterResource("fly:index/app:App", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetApp gets an existing App resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetApp(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *AppState, opts ...pulumi.ResourceOption) (*App, error) {
	var resource App
	err := ctx.ReadResource("fly:index/app:App", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering App resources.
type appState struct {
	AppUrl *string `pulumi:"appUrl"`
	// Assign a shared ipv4 address to the app. Note that depending on conditions an app may get a shared ip automatically.
	AssignSharedIpAddress *bool `pulumi:"assignSharedIpAddress"`
	// Name of application
	Name *string `pulumi:"name"`
	// The name of the organization to generate the app in, ex: `personal` (your initial org)
	Org   *string `pulumi:"org"`
	OrgId *string `pulumi:"orgId"`
	// A shared ipv4 address, automatically attached in certain conditions or if explicitly requested
	SharedIpAddress *string `pulumi:"sharedIpAddress"`
}

type AppState struct {
	AppUrl pulumi.StringPtrInput
	// Assign a shared ipv4 address to the app. Note that depending on conditions an app may get a shared ip automatically.
	AssignSharedIpAddress pulumi.BoolPtrInput
	// Name of application
	Name pulumi.StringPtrInput
	// The name of the organization to generate the app in, ex: `personal` (your initial org)
	Org   pulumi.StringPtrInput
	OrgId pulumi.StringPtrInput
	// A shared ipv4 address, automatically attached in certain conditions or if explicitly requested
	SharedIpAddress pulumi.StringPtrInput
}

func (AppState) ElementType() reflect.Type {
	return reflect.TypeOf((*appState)(nil)).Elem()
}

type appArgs struct {
	// Assign a shared ipv4 address to the app. Note that depending on conditions an app may get a shared ip automatically.
	AssignSharedIpAddress *bool `pulumi:"assignSharedIpAddress"`
	// Name of application
	Name *string `pulumi:"name"`
	// The name of the organization to generate the app in, ex: `personal` (your initial org)
	Org *string `pulumi:"org"`
}

// The set of arguments for constructing a App resource.
type AppArgs struct {
	// Assign a shared ipv4 address to the app. Note that depending on conditions an app may get a shared ip automatically.
	AssignSharedIpAddress pulumi.BoolPtrInput
	// Name of application
	Name pulumi.StringPtrInput
	// The name of the organization to generate the app in, ex: `personal` (your initial org)
	Org pulumi.StringPtrInput
}

func (AppArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*appArgs)(nil)).Elem()
}

type AppInput interface {
	pulumi.Input

	ToAppOutput() AppOutput
	ToAppOutputWithContext(ctx context.Context) AppOutput
}

func (*App) ElementType() reflect.Type {
	return reflect.TypeOf((**App)(nil)).Elem()
}

func (i *App) ToAppOutput() AppOutput {
	return i.ToAppOutputWithContext(context.Background())
}

func (i *App) ToAppOutputWithContext(ctx context.Context) AppOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AppOutput)
}

// AppArrayInput is an input type that accepts AppArray and AppArrayOutput values.
// You can construct a concrete instance of `AppArrayInput` via:
//
//	AppArray{ AppArgs{...} }
type AppArrayInput interface {
	pulumi.Input

	ToAppArrayOutput() AppArrayOutput
	ToAppArrayOutputWithContext(context.Context) AppArrayOutput
}

type AppArray []AppInput

func (AppArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*App)(nil)).Elem()
}

func (i AppArray) ToAppArrayOutput() AppArrayOutput {
	return i.ToAppArrayOutputWithContext(context.Background())
}

func (i AppArray) ToAppArrayOutputWithContext(ctx context.Context) AppArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AppArrayOutput)
}

// AppMapInput is an input type that accepts AppMap and AppMapOutput values.
// You can construct a concrete instance of `AppMapInput` via:
//
//	AppMap{ "key": AppArgs{...} }
type AppMapInput interface {
	pulumi.Input

	ToAppMapOutput() AppMapOutput
	ToAppMapOutputWithContext(context.Context) AppMapOutput
}

type AppMap map[string]AppInput

func (AppMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*App)(nil)).Elem()
}

func (i AppMap) ToAppMapOutput() AppMapOutput {
	return i.ToAppMapOutputWithContext(context.Background())
}

func (i AppMap) ToAppMapOutputWithContext(ctx context.Context) AppMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AppMapOutput)
}

type AppOutput struct{ *pulumi.OutputState }

func (AppOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**App)(nil)).Elem()
}

func (o AppOutput) ToAppOutput() AppOutput {
	return o
}

func (o AppOutput) ToAppOutputWithContext(ctx context.Context) AppOutput {
	return o
}

func (o AppOutput) AppUrl() pulumi.StringOutput {
	return o.ApplyT(func(v *App) pulumi.StringOutput { return v.AppUrl }).(pulumi.StringOutput)
}

// Assign a shared ipv4 address to the app. Note that depending on conditions an app may get a shared ip automatically.
func (o AppOutput) AssignSharedIpAddress() pulumi.BoolOutput {
	return o.ApplyT(func(v *App) pulumi.BoolOutput { return v.AssignSharedIpAddress }).(pulumi.BoolOutput)
}

// Name of application
func (o AppOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *App) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// The name of the organization to generate the app in, ex: `personal` (your initial org)
func (o AppOutput) Org() pulumi.StringOutput {
	return o.ApplyT(func(v *App) pulumi.StringOutput { return v.Org }).(pulumi.StringOutput)
}

func (o AppOutput) OrgId() pulumi.StringOutput {
	return o.ApplyT(func(v *App) pulumi.StringOutput { return v.OrgId }).(pulumi.StringOutput)
}

// A shared ipv4 address, automatically attached in certain conditions or if explicitly requested
func (o AppOutput) SharedIpAddress() pulumi.StringOutput {
	return o.ApplyT(func(v *App) pulumi.StringOutput { return v.SharedIpAddress }).(pulumi.StringOutput)
}

type AppArrayOutput struct{ *pulumi.OutputState }

func (AppArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*App)(nil)).Elem()
}

func (o AppArrayOutput) ToAppArrayOutput() AppArrayOutput {
	return o
}

func (o AppArrayOutput) ToAppArrayOutputWithContext(ctx context.Context) AppArrayOutput {
	return o
}

func (o AppArrayOutput) Index(i pulumi.IntInput) AppOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *App {
		return vs[0].([]*App)[vs[1].(int)]
	}).(AppOutput)
}

type AppMapOutput struct{ *pulumi.OutputState }

func (AppMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*App)(nil)).Elem()
}

func (o AppMapOutput) ToAppMapOutput() AppMapOutput {
	return o
}

func (o AppMapOutput) ToAppMapOutputWithContext(ctx context.Context) AppMapOutput {
	return o
}

func (o AppMapOutput) MapIndex(k pulumi.StringInput) AppOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *App {
		return vs[0].(map[string]*App)[vs[1].(string)]
	}).(AppOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*AppInput)(nil)).Elem(), &App{})
	pulumi.RegisterInputType(reflect.TypeOf((*AppArrayInput)(nil)).Elem(), AppArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*AppMapInput)(nil)).Elem(), AppMap{})
	pulumi.RegisterOutputType(AppOutput{})
	pulumi.RegisterOutputType(AppArrayOutput{})
	pulumi.RegisterOutputType(AppMapOutput{})
}
