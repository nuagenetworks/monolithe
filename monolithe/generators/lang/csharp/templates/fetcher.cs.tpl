{{ header }}


import net.nuagenetworks.bambou.RestObject;
import net.nuagenetworks.bambou.RestFetcher;
import {{ package_name }}.{{ class_prefix }}{{ specification.entity_name }};

namespace {{ package_name }}.fetchers
{
    public class {{ class_prefix }}{{ specification.entity_name_plural }}Fetcher: RestFetcher<{{ class_prefix }}{{ specification.entity_name }}>
    {

       private const long serialVersionUID = 1L;
       
       public {{ class_prefix }}{{ specification.entity_name_plural }}Fetcher(RestObject parentRestObj) {
          base(parentRestObj, {{ class_prefix }}{{ specification.entity_name }}.class);
       }
   
       {% if override_content -%}
       {{ override_content.replace('\n', '\n   ') }}
       {%- endif %}
    }
}
