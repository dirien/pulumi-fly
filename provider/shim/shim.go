package shim

import (
	p "github.com/andrewbaxter/terraform-provider-fly/provider"
	"github.com/hashicorp/terraform-plugin-framework/provider"
)

func NewProvider() provider.Provider {
	fly := p.New()
	return fly()
}
