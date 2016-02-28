{{ header }}

package {{ sdk_name }}

import "github.com/nuagenetworks/go-bambou/bambou"

// {{specification.entity_name}}Identity represents the Identity of the object
var {{specification.entity_name}}Identity = bambou.Identity {
    Name:     "{{specification.rest_name}}",
    Category: "{{specification.resource_name}}",
}

{% if not specification.is_root -%}
// {{specification.entity_name_plural}}List represents a list of {{specification.entity_name_plural}}
type {{specification.entity_name_plural}}List []*{{specification.entity_name}}

// {{specification.entity_name_plural}}Ancestor is the interface of an ancestor of a {{specification.entity_name}} must implement.
type {{specification.entity_name_plural}}Ancestor interface {
    {{specification.entity_name_plural}}(*bambou.FetchingInfo) ({{specification.entity_name_plural}}List, *bambou.Error)
    Create{{specification.entity_name_plural}}(*{{ specification.entity_name }}) (*bambou.Error)
}
{%- endif %}

// {{specification.entity_name}} represents the model of a {{specification.rest_name}}
type {{specification.entity_name}} struct {
    ID         string `json:"ID,omitempty"`
    ParentID   string `json:"parentID,omitempty"`
    ParentType string `json:"parentType,omitempty"`
    Owner      string `json:"owner,omitempty"`
    {% for attribute in specification.attributes -%}
    {% set field_name = attribute.local_name[0:1].upper() + attribute.local_name[1:] -%}
    {% set can_ommit = attribute.type != "boolean" -%}
    {{ field_name }} {{ attribute.local_type }} `json:"{{attribute.local_name}}{% if can_ommit -%},omitempty{% endif -%}"`
    {% endfor -%}

    {%- if specification.is_root %}
    Token string `json:"APIKey,omitempty"`
    Organization string `json:"enterprise,omitempty"`
    {%- endif %}
}

// New{{specification.entity_name}} returns a new *{{specification.entity_name}}
func New{{specification.entity_name}}() *{{specification.entity_name}} {

    return &{{specification.entity_name}}{
        {% for attribute, value in attribute_defaults.iteritems() -%}
        {{attribute}}: {{value}},
        {% endfor %}
    }
}

// Identity returns the Identity of the object.
func (o *{{specification.entity_name}}) Identity() bambou.Identity {

    return {{specification.entity_name}}Identity
}

// Identifier returns the value of the object's unique identifier.
func (o *{{specification.entity_name}}) Identifier() string {

    return o.ID
}

// SetIdentifier sets the value of the object's unique identifier.
func (o *{{specification.entity_name}}) SetIdentifier(ID string) {

    o.ID = ID
}

{% if specification.is_root -%}
// APIKey returns a the API Key
func (o *{{specification.entity_name}}) APIKey() string {

    return o.Token
}

// SetAPIKey sets a the API Key
func (o *{{specification.entity_name}}) SetAPIKey(key string) {

    o.Token = key
}

{% endif -%}

// Fetch retrieves the {{specification.entity_name}} from the server
func (o *{{specification.entity_name}}) Fetch() *bambou.Error {

    return bambou.CurrentSession().FetchEntity(o)
}

// Save saves the {{specification.entity_name}} into the server
func (o *{{specification.entity_name}}) Save() *bambou.Error {

    return bambou.CurrentSession().SaveEntity(o)
}

// Delete deletes the {{specification.entity_name}} from the server
func (o *{{specification.entity_name}}) Delete() *bambou.Error {

    return bambou.CurrentSession().DeleteEntity(o)
}

{% for api in specification.child_apis -%}
{% set child_specification = specification_set[api.remote_specification_name] -%}
// {{ child_specification.entity_name_plural }} retrieves the list of child {{ child_specification.entity_name_plural }} of the {{specification.entity_name}}
func (o *{{ specification.entity_name }}) {{ child_specification.entity_name_plural }}(info *bambou.FetchingInfo) ({{ child_specification.entity_name_plural }}List, *bambou.Error) {

    var list {{ child_specification.entity_name_plural }}List
    err := bambou.CurrentSession().FetchChildren(o, {{ child_specification.entity_name }}Identity, &list, info)
    return list, err
}
{% if  api.relationship == "child" or api.relationship == "root" or api.relationship == "alias" %}
// Create{{ child_specification.entity_name }} creates a new child {{ child_specification.entity_name }} under the {{specification.entity_name}}
func (o *{{ specification.entity_name }}) Create{{ child_specification.entity_name }}(child *{{ child_specification.entity_name }}) *bambou.Error {

    return bambou.CurrentSession().CreateChild(o, child)
}
{% else %}
// Assign{{ child_specification.entity_name_plural }} assigns the list of {{ child_specification.entity_name_plural }} to the {{specification.entity_name}}
func (o *{{ specification.entity_name }}) Assign{{ child_specification.entity_name_plural }}(children {{ child_specification.entity_name_plural }}List) *bambou.Error {

    list := []bambou.Identifiable{}
    for _, c := range children {
        list = append(list, c)
    }

    return bambou.CurrentSession().AssignChildren(o, list, {{ child_specification.entity_name }}Identity)
}
{% endif %}
{% endfor -%}
