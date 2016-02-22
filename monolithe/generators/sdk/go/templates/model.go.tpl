{{ header }}

package {{ sdk_name }}

import "github.com/nuagenetworks/go-bambou/bambou"

// Represents the Identity of the object
var {{specification.entity_name}}Identity = bambou.Identity {
    RESTName:     "{{specification.rest_name}}",
    ResourceName: "{{specification.resource_name}}",
}

{% if not specification.is_root -%}
// Represents a list of {{specification.entity_name_plural}}
type {{specification.entity_name_plural}}List []*{{specification.entity_name}}

// Interface of an ancestor of a {{specification.entity_name}}
type {{specification.entity_name_plural}}Ancestor interface {
    {{specification.entity_name_plural}}(*bambou.FetchingInfo) ({{specification.entity_name_plural}}List, *bambou.Error)
    Create{{specification.entity_name_plural}}(*{{ specification.entity_name }}) (*bambou.Error)
}
{%- endif %}

// Represents a {{specification.entity_name}}
type {{specification.entity_name}} struct {
    bambou.ExposedObject

    {% for attribute in specification.attributes -%}
    {% set field_name = attribute.local_name[0:1].upper() + attribute.local_name[1:] -%}
    {% set can_ommit = attribute.type != "boolean" -%}
    {{ field_name }} {{ attribute.local_type }} `json:"{{attribute.local_name}}{% if can_ommit -%},omitempty{% endif -%}"`
    {% endfor -%}

    {%- if specification.is_root %}
    APIKey string `json:"APIKey,omitempty"`
    Organization string `json:"enterprise,omitempty"`
    {%- endif %}
}

// Returns a new *{{specification.entity_name}}
func New{{specification.entity_name}}() *{{specification.entity_name}} {

    return &{{specification.entity_name}}{
        ExposedObject: bambou.ExposedObject{
            Identity: {{specification.entity_name}}Identity,
        },
        {% for attribute, value in attribute_defaults.iteritems() -%}
        {{attribute}}: {{value}},
        {% endfor %}
    }
}

{% if specification.is_root -%}
// Returns a the API Key
func (o *{{specification.entity_name}}) GetAPIKey() string {

    return o.APIKey
}

// Sets a the API Key
func (o *{{specification.entity_name}}) SetAPIKey(key string) {

    o.APIKey = key
}

// Returns the special Rootable object URL
func (o *{{specification.entity_name}}) GetPersonalURL() string {

    return bambou.CurrentSession().URL + "/" + o.Identity.ResourceName
}

func (o *{{specification.entity_name}}) GetGeneralURL() string {

    return o.GetPersonalURL()
}

// Returns the special Rootable object children URL
func (o *{{specification.entity_name}}) GetURLForChildrenIdentity(identity bambou.Identity) string {

    return o.GetPersonalURL()
}

{% endif -%}

// Retrieves the {{specification.entity_name}} from the server
func (o *{{specification.entity_name}}) Fetch() *bambou.Error {

    return bambou.FetchEntity(o)
}

// Saves the {{specification.entity_name}} into the server
func (o *{{specification.entity_name}}) Save() *bambou.Error {

    return bambou.SaveEntity(o)
}

// Deletes the {{specification.entity_name}} from the server
func (o *{{specification.entity_name}}) Delete() *bambou.Error {

    return bambou.DeleteEntity(o)
}

{% for api in specification.child_apis -%}
{% set child_specification = specification_set[api.remote_specification_name] -%}
// Retrieves the list of child {{ child_specification.entity_name_plural }} of the {{specification.entity_name}}
func (o *{{ specification.entity_name }}) {{ child_specification.entity_name_plural }}(info *bambou.FetchingInfo) ({{ child_specification.entity_name_plural }}List, *bambou.Error) {

    var list {{ child_specification.entity_name_plural }}List
    err := bambou.FetchChildren(o, {{ child_specification.entity_name }}Identity, &list, info)
    return list, err
}
{% if  api.relationship == "child" or api.relationship == "root" or api.relationship == "alias" %}
// Creates a new child {{ child_specification.entity_name }} under the {{specification.entity_name}}
func (o *{{ specification.entity_name }}) Create{{ child_specification.entity_name }}(child *{{ child_specification.entity_name }}) *bambou.Error {

    return bambou.CreateChild(o, child)
}
{% else %}
// Assigns the list of {{ child_specification.entity_name_plural }} to the {{specification.entity_name}}
func (o *{{ specification.entity_name }}) Assign{{ child_specification.entity_name_plural }}(children interface{}) *bambou.Error {

    return bambou.AssignChildren(o, children, {{ child_specification.entity_name }}Identity)
}
{% endif %}
{% endfor -%}