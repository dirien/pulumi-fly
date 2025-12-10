package main

import (
	"fmt"

	"github.com/dirien/pulumi-fly/sdk/go/fly"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi/config"
)

func main() {

	pulumi.Run(func(ctx *pulumi.Context) error {

		cfg := config.New(ctx, "fly")
		flyToken := cfg.RequireSecret("fly_api_token")

		// Create explicit provider
		flyProvider, err := fly.NewProvider(ctx, "fly-provider", &fly.ProviderArgs{
			FlyApiToken: flyToken,
		})
		if err != nil {
			return err
		}

		exampleApp, err := fly.NewApp(ctx, "example-app", &fly.AppArgs{
			Name: pulumi.String("my-dirien-app"),
			Org:  pulumi.String("personal"),
		}, pulumi.Provider(flyProvider))
		if err != nil {
			return err
		}

		exampleIpV4, err := fly.NewIp(ctx, "example-ip", &fly.IpArgs{
			App:  exampleApp.Name,
			Type: pulumi.String("v4"),
		}, pulumi.Provider(flyProvider))
		if err != nil {
			return err
		}

		exampleIpV6, err := fly.NewIp(ctx, "example-ip-v6", &fly.IpArgs{
			App:  exampleApp.Name,
			Type: pulumi.String("v6"),
		}, pulumi.Provider(flyProvider))
		if err != nil {
			return err
		}

		for _, region := range []string{"ams", "cdg", "fra"} {

			_, err = fly.NewMachine(ctx, fmt.Sprintf("example-machine-%s", region), &fly.MachineArgs{
				App:    exampleApp.Name,
				Region: pulumi.String(region),
				Name:   pulumi.Sprintf("my-dirien-app-%s", region),
				Image:  pulumi.String("dirien/hello-server:latest"),
				Env: pulumi.StringMap{
					"FLY_PROCESS_GROUP": pulumi.String("app"),
					"PRIMARY_REGION":    pulumi.String(region),
				},
				Services: fly.MachineServiceArray{
					&fly.MachineServiceArgs{
						Ports: fly.MachineServicePortArray{
							&fly.MachineServicePortArgs{
								Port: pulumi.Int(80),
								Handlers: pulumi.StringArray{
									pulumi.String("http"),
								},
							},
							&fly.MachineServicePortArgs{
								Port: pulumi.Int(443),
								Handlers: pulumi.StringArray{
									pulumi.String("tls"),
									pulumi.String("http"),
								},
							},
						},
						Protocol:     pulumi.String("tcp"),
						InternalPort: pulumi.Int(8080),
					},
				},
				Cpus:   pulumi.Int(1),
				Memory: pulumi.Int(256),
			}, pulumi.DependsOn([]pulumi.Resource{exampleApp, exampleIpV4, exampleIpV6}),
				pulumi.Provider(flyProvider))

			if err != nil {
				return err
			}
		}

		ctx.Export("app-url", pulumi.Sprintf("https://%s.fly.dev", exampleApp.Name))

		return nil
	})
}
