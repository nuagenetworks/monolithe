{{ header }}


using net.nuagenetworks.bambou;
using {{ package_name }}; 

namespace {{ package_name }}.fetchers
{
    public class {{ class_prefix }}{{ specification.entity_name_plural }}Fetcher: RestFetcher<{{ class_prefix }}{{ specification.entity_name }}>
    {

       private const long serialVersionUID = 1L;
       
       public {{ class_prefix }}{{ specification.entity_name_plural }}Fetcher(RestObject parentRestObj) 
          : base(parentRestObj, typeof({{ class_prefix }}{{ specification.entity_name }}))
       {
       }
   
       {% if override_content -%}
       {{ override_content.replace('\n', '\n   ') }}
       {%- endif %}
    }
}
