{{ header }}

@import <Foundation/Foundation.j>
@import <Bambou/NURESTFetcher.j>

@class {{ class_prefix }}{{ specification.entity_name }}


@implementation {{ class_prefix }}{{ specification.entity_name_plural }}Fetcher : NURESTFetcher

+ (Class)managedObjectClass
{
    return {{ class_prefix }}{{ specification.entity_name }};
}

@end
