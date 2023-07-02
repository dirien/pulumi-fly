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
