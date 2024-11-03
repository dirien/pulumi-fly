import * as fly from "@ediri/pulumi-fly";


const app = new fly.App("fly-ts", {
    name: "my-dirien-app",
    org: "personal",
    assignSharedIpAddress: false
})

const ip4 = new fly.Ip("fly-ts-ip", {
    app: app.name,
    type: "v4",
    region: 'global'
})
