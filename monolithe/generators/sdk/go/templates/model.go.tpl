{{ header }}

package {{ sdk_name }}

import (
    "github.com/primalmotion/bambou"
)

/*
    Identity
*/
var (
    {{specification.entity_name}}Identity = bambou.RESTIdentity{"{{specification.rest_name}}", "{{specification.resource_name}}"}
)

{%- if not specification.is_root %}
/*
    Ancestor Interface
*/
type {{specification.entity_name_plural}}List []*{{specification.entity_name}}
type {{specification.entity_name_plural}}Ancestor interface {
    {{specification.entity_name_plural}}(*bambou.FetchingInfo) ({{specification.entity_name_plural}}List, *bambou.Error)
    Create{{specification.entity_name_plural}}(*{{ specification.entity_name }}) (*bambou.Error)
}
{%- endif %}

/*
    Object Structure
*/
type {{specification.entity_name}} struct {
    bambou.ExposedObject

    {% for attribute in specification.attributes -%}
    {% set field_name = attribute.local_name[0:1].upper() + attribute.local_name[1:] -%}
    {{ field_name }} {{ attribute.local_type }} `json:"{{attribute.local_name}},omitempty"`
    {% endfor -%}

    {%- if specification.is_root %}
    APIKey string `json:"APIKey,omitempty"`
    Organization string `json:"enterprise,omitempty"`
    {%- endif %}
}

/*
    Initializer
*/
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
/*
    Rootable interface
*/
func (o *{{specification.entity_name}}) GetAPIKey() string {

    return o.APIKey
}

func (o *{{specification.entity_name}}) SetAPIKey(key string) {

    o.APIKey = key
}

func (o *{{specification.entity_name}}) GetURL() string {

    return bambou.CurrentSession().URL + "/" + o.Identity.ResourceName
}

func (o *{{specification.entity_name}}) GetURLForChildrenIdentity(identity bambou.RESTIdentity) string {

    return bambou.CurrentSession().URL + "/" + identity.ResourceName
}

{% endif -%}

/*
    Exposable Interface
*/
func (o *{{specification.entity_name}}) Fetch() *bambou.Error {

    return bambou.FetchEntity(o)
}

func (o *{{specification.entity_name}}) Save() *bambou.Error {

    return bambou.SaveEntity(o)
}

func (o *{{specification.entity_name}}) Delete() *bambou.Error {

    return bambou.DeleteEntity(o)
}

/*
    Children Entities
*/
{% for api in specification.child_apis -%}
{% if  api.relationship == "child" or api.relationship == "root" -%}
{% set child_specification = specification_set[api.remote_specification_name] -%}


func (o *{{ specification.entity_name }}) {{ child_specification.entity_name_plural }}(info *bambou.FetchingInfo) ({{ child_specification.entity_name_plural }}List, *bambou.Error) {

    var list {{ child_specification.entity_name_plural }}List
    err := bambou.FetchChildren(o, {{ child_specification.entity_name }}Identity, &list, info)
    return list, err
}

func (o *{{ specification.entity_name }}) Create{{ child_specification.entity_name }}(child *{{ child_specification.entity_name }}) *bambou.Error {

    return bambou.CreateChild(o, child)
}

{% endif -%}
{% endfor -%}


/*
    Assignation
*/
{% for api in specification.child_apis -%}
{% if  api.relationship == "member" -%}
{% set child_specification = specification_set[api.remote_specification_name] -%}
func (o *{{ specification.entity_name }}) Assign{{ child_specification.entity_name_plural }}(children interface{}) *bambou.Error {

    return bambou.AssignChildren(o, children, {{ child_specification.entity_name }}Identity)
}
{% endif -%}
{% endfor -%}


