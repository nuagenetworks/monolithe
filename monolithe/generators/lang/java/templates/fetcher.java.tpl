{{ header }}

package {{ package_name }}.fetchers;

import net.nuagenetworks.bambou.RestObject;
import net.nuagenetworks.bambou.RestFetcher;
import {{ package_name }}.{{ class_prefix }}{{ specification.entity_name }};

public class {{ class_prefix }}{{ specification.entity_name_plural }}Fetcher extends RestFetcher<{{ class_prefix }}{{ specification.entity_name }}> {

   private static final long serialVersionUID = 1L;
   
   public {{ class_prefix }}{{ specification.entity_name_plural }}Fetcher(RestObject parentRestObj) {
      super(parentRestObj, {{ class_prefix }}{{ specification.entity_name }}.class);
   }
   
   {% if override_content -%}
   {{ override_content.replace('\n', '\n   ') }}
   {%- endif %}
}
