package shim

import (
	p "github.com/fly-apps/terraform-provider-fly/internal/provider"
	"github.com/hashicorp/terraform-plugin-framework/provider"
)

func NewProvider() provider.Provider {
	fly := p.New("0.0.0")
	return fly()
}
