// Copyright 2016-2023, Pulumi Corporation.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package fly

import (
	"fmt"
	// embed is used to store bridge-metadata.json in the compiled binary
	_ "embed"
	"path/filepath"
	"unicode"

	pf "github.com/pulumi/pulumi-terraform-bridge/pf/tfbridge"
	"github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfbridge"
	"github.com/pulumi/pulumi/sdk/v3/go/common/tokens"

	"github.com/dirien/pulumi-fly/provider/pkg/version"
	"github.com/fly-apps/terraform-provider-fly/shim"
)

// all of the random token components used below.
const (
	flyPkg = "fly"
	flyMod = "index"
)

// flyMember manufactures a type token for the random package and the given module and type.
func flyMember(mod string, mem string) tokens.ModuleMember {
	return tokens.ModuleMember(flyPkg + ":" + mod + ":" + mem)
}

// flyType manufactures a type token for the random package and the given module and type.
func flyType(mod string, typ string) tokens.Type {
	return tokens.Type(flyMember(mod, typ))
}

// flyResource manufactures a standard resource token given a module and resource name.  It automatically uses the
// fly package and names the file by simply lower casing the resource's first character.
func flyResource(mod string, res string) tokens.Type {
	fn := string(unicode.ToLower(rune(res[0]))) + res[1:]
	return flyType(mod+"/"+fn, res)
}

// flyDataSource manufactures a standard resource token given a module and resource name.  It automatically uses the
// fly package and names the file by simply lower casing the resource's first character.
func flyDataSource(mod string, res string) tokens.ModuleMember {
	fn := string(unicode.ToLower(rune(res[0]))) + res[1:]
	return flyMember(mod+"/"+fn, res)
}

//go:embed cmd/pulumi-resource-fly/bridge-metadata.json
var metadata []byte

// Provider returns additional overlaid schema and metadata associated with the random package.
func Provider() tfbridge.ProviderInfo {
	info := tfbridge.ProviderInfo{
		P:           pf.ShimProvider(shim.NewProvider()),
		Name:        "fly",
		Description: "A Pulumi package for creating and managing Fly.io resources.",
		Keywords: []string{
			"pulumi",
			"fly",
			"category/cloud",
		},
		DisplayName:       "Fly.io",
		LogoURL:           "",
		Publisher:         "dirien",
		License:           "Apache-2.0",
		Homepage:          "https://github.com/dirien/pulumi-fly",
		Repository:        "https://github.com/dirien/pulumi-fly",
		GitHubOrg:         "fly-apps",
		PluginDownloadURL: "github://api.github.com/dirien/pulumi-fly",
		Version:           version.Version,
		MetadataInfo:      tfbridge.NewProviderMetadata(metadata),
		Resources: map[string]*tfbridge.ResourceInfo{
			"fly_app":     {Tok: flyResource(flyMod, "App")},
			"fly_cert":    {Tok: flyResource(flyMod, "Cert")},
			"fly_ip":      {Tok: flyResource(flyMod, "Ip")},
			"fly_machine": {Tok: flyResource(flyMod, "Machine")},
			"fly_volume":  {Tok: flyResource(flyMod, "Volume")},
		},
		DataSources: map[string]*tfbridge.DataSourceInfo{
			"fly_app":    {Tok: flyDataSource(flyMod, "getApp")},
			"fly_cert":   {Tok: flyDataSource(flyMod, "getCert")},
			"fly_ip":     {Tok: flyDataSource(flyMod, "getIp")},
			"fly_volume": {Tok: flyDataSource(flyMod, "getVolume")},
		},
		JavaScript: &tfbridge.JavaScriptInfo{
			PackageName: "@ediri/pulumi-fly",
			Dependencies: map[string]string{
				"@pulumi/pulumi": "^3.0.0",
			},
			DevDependencies: map[string]string{
				"@types/node": "^10.0.0", // so we can access strongly typed node definitions.
			},
		},
		Python: &tfbridge.PythonInfo{
			PackageName: "ediri_fly",
			Requires: map[string]string{
				"pulumi": ">=3.0.0,<4.0.0",
			},
		},
		Golang: &tfbridge.GolangInfo{
			ImportBasePath: filepath.Join(
				fmt.Sprintf("github.com/pulumi/pulumi-%[1]s/sdk/", flyPkg),
				tfbridge.GetModuleMajorVersion(version.Version),
				"go",
				flyPkg,
			),
			GenerateResourceContainerTypes: true,
		},
		CSharp: &tfbridge.CSharpInfo{
			RootNamespace: "ediri",
			PackageReferences: map[string]string{
				"Pulumi": "3.*",
			},
		},
	}
	info.SetAutonaming(255, "-")
	return info
}
