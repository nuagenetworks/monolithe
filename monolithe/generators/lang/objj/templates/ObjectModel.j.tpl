{{ header }}

@import <Foundation/Foundation.j>
@import <AppKit/CPArrayController.j>
@import <Bambou/NURESTObject.j>

{% for api in specification.child_apis -%}
{% set child_spec = specification_set[api.rest_name] -%}
@import "Fetchers/{{ class_prefix }}{{ child_spec.entity_name_plural }}Fetcher.j"
{% endfor %}

@implementation {{ class_prefix }}{{ specification.entity_name }} : NURESTObject
{
    {% for attribute in specification.attributes -%}
    {{ attribute.local_type }} _{{attribute.local_name }} @accessors(property={{attribute.local_name }});
    {% endfor %}
    {% for api in specification.child_apis -%}
    {% set child_spec = specification_set[api.rest_name] -%}
    {{ class_prefix }}{{ child_spec.entity_name_plural }}Fetcher _{{ child_spec.entity_name_plural }} @accessors(property={{ child_spec.entity_name_plural }});
    {% endfor %}
}


#pragma mark -
#pragma mark Class Method

+ (CPString)RESTName
{
    return @"{{ specification.rest_name }}";
}


#pragma mark -
#pragma mark Initialization

- (id)init
{
    if (self = [super init])
    {
        {% for attribute in specification.attributes -%}
        [self exposeLocalKeyPathToREST:@"{{ attribute.local_name }}"];
        {% endfor %}
        {% for api in specification.child_apis -%}
        {% set child_spec = specification_set[api.rest_name] -%}
        _{{ child_spec.entity_name_plural }} = [{{ class_prefix }}{{ child_spec.entity_name_plural }}Fetcher fetcherWithParentObject:self];
        {% endfor %}
    }

    return self;
}

@end
