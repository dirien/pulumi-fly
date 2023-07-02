---
title: Fly.io
meta_desc: Provides an overview of the Fly.io Provider for Pulumi.
layout: package
---

The Fly.io Resource Provider lets you manage [Fly.io](https://fly.io/) resources.


## Example

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}
 TO DO
{{% /choosable %}}

{{% choosable language typescript %}}
```typescript
import * as pulumi from "@pulumi/pulumi";
import * as fly from "@ediri/pulumi-fly";


const app = new fly.App("fly-ts", {
    name: "my-dirien-app",
    org: "personal",
})

const ip4 = new fly.Ip("fly-ts-ip", {
    app: app.name,
    type: "v4",
})

const ip6 = new fly.Ip("fly-ts-ip-v6", {
    app: app.name,
    type: "v6",
})

for (const region of ["ams", "cdg", "fra"]) {
    new fly.Machine("fly-ts-machine-" + region, {
        app: app.name,
        region: region,
        name: "fly-ts-machine-" + region,
        image: "dirien/hello-server:latest",
        services: [
            {
                ports: [
                    {
                        port: 80,
                        handlers: [
                            "http",
                        ],
                    },
                    {
                        port: 443,
                        handlers: [
                            "tls",
                            "http",
                        ],
                    }
                ],
                internalPort: 8080,
                protocol: "tcp",
            }
        ],
        cpus: 1,
        memorymb: 256,
    }, {
        dependsOn: [
            app,
            ip4,
            ip6,
        ],
    })
}

export const appUrl = pulumi.interpolate`https://${app.name}.fly.dev`
```
{{% /choosable %}}

{{% choosable language python %}}
TO DO
{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
	"fmt"
	"github.com/dirien/pulumi-fly/go/fly"
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

```

{{% /choosable %}}

{{% choosable language csharp %}}
TO DO
{{% /choosable %}}

{{< /chooser >}}
