package main

import (
	"fmt"
	"github.com/dirien/pulumi-fly/sdk/go/fly"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {

		exampleApp, err := fly.NewApp(ctx, "example-app", &fly.AppArgs{
			Name: pulumi.String("my-dirien-app"),
			Org:  pulumi.String("personal"),
		})
		if err != nil {
			return err
		}

		_, err = fly.NewIp(ctx, "example-ip", &fly.IpArgs{
			App:  exampleApp.Name,
			Type: pulumi.String("v4"),
		})
		if err != nil {
			return err
		}
		_, err = fly.NewIp(ctx, "example-ip-v6", &fly.IpArgs{
			App:  exampleApp.Name,
			Type: pulumi.String("v6"),
		})

		for _, region := range []string{"ams", "cdg", "fra"} {

			_, err = fly.NewMachine(ctx, fmt.Sprintf("example-machine-%s", region), &fly.MachineArgs{
				App:    exampleApp.Name,
				Region: pulumi.String(region),
				Name:   pulumi.Sprintf("my-dirien-app-%s", region),
				Image:  pulumi.String("dirien/hello-server:latest"),
				Services: fly.MachineServiceArray{
					fly.MachineServiceArgs{
						Ports: fly.MachineServicePortArray{
							fly.MachineServicePortArgs{
								Port: pulumi.Int(80),
								Handlers: pulumi.StringArray{
									pulumi.String("http"),
								},
							},
							fly.MachineServicePortArgs{
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
				Cpus:     pulumi.Int(1),
				Memorymb: pulumi.Int(256),
			}, pulumi.DependsOn([]pulumi.Resource{exampleApp}))
			if err != nil {
				return err
			}
		}

		ctx.Export("app-url", pulumi.Sprintf("https://%s.fly.dev", exampleApp.Name))

		return nil
	})
}
