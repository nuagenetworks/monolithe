{{ header }}

package {{ name }}.{{ version_string }}.fetchers;

import com.github.nuagenetworks.bambou.RestObject;
import com.github.nuagenetworks.bambou.RestFetcher;
import {{ name }}.{{ version_string }}.{{ class_prefix }}{{ specification.entity_name }};

public class {{ class_prefix }}{{ specification.entity_name_plural }}Fetcher extends RestFetcher<{{ class_prefix }}{{ specification.entity_name }}> {

   private static final long serialVersionUID = 1L;
   
   public {{ class_prefix }}{{ specification.entity_name_plural }}Fetcher(RestObject parentRestObj) {
      super(parentRestObj, {{ class_prefix }}{{ specification.entity_name }}.class);
   }
   
   {% if override_content -%}
   {{ override_content.replace('\n', '\n   ') }}
   {%- endif %}
}
