# Fly.io Resource Provider

![Fly.io](./img/fly.png)

The Fly.io Resource Provider lets you manage [Fly.io](https://fly.io/) resources.

## Installing

This package is available for several languages/platforms:

### Node.js (JavaScript/TypeScript)

To use from JavaScript or TypeScript in Node.js, install using either `npm`:

```bash
npm install @ediri/pulumi-fly
```

or `yarn`:

```bash
yarn add @ediri/pulumi-fly
```

### Python

To use from Python, install using `pip`:

```bash
pip install ediri_fly
```

### Go

To use from Go, use `go get` to grab the latest version of the library:

```bash
go get github.com/dirien/pulumi-fly/sdk
```

### .NET

To use from .NET, install using `dotnet add package`:

```bash
dotnet add package ediri.Fly
```

## Configuration

The following configuration options are supported for the `fly` provider:

* `fly_api_token` (String) fly.io api token. If not set checks env for `FLY_API_TOKEN`
* `fly_http_endpoint` (String) Where the provider should look to find the fly http endpoint

## Reference

For detailed reference documentation, please visit [the Pulumi registry](https://www.pulumi.com/registry/packages/fly/api-docs/).
