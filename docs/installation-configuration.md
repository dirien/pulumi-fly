---
title: Fly.io Setup
meta_desc: Information on how to install the Fly.io provider.
layout: package
---

## Installation

The Pulumi Fly.io provider is available as a package in all Pulumi languages:

* JavaScript/TypeScript: [`@ediri/pulumi-fly`](https://www.npmjs.com/package/@ediri/pulumi-fly)
* Python: [`ediri_fly`](https://pypi.org/project/ediri_fly/)
* Go: [`github.com/dirien/pulumi-fly/sdk`](https://github.com/dirien/pulumi-fly/sdk)
* .NET: [`ediri.Fly`](https://www.nuget.org/packages/ediri.Fly)

## Configuration Options

The following configuration options are supported for the `fly` provider:

* `fly_api_token` (String) fly.io api token. If not set checks env for `FLY_API_TOKEN`
* `fly_http_endpoint` (String) Where the provider should look to find the fly http endpoint
