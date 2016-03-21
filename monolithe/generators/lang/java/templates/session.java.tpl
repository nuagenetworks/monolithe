{{ header }}

package {{ name }}.{{ version_string }};

import bambou.RestSession;

public class {{ class_prefix }}{{ product_accronym }}Session extends RestSession {
    
   public final static double VERSION = {{ version }};
   
   public {{ class_prefix }}{{ product_accronym }}Session(String username, String password, String enterprise, String apiUrl, String certificate) {
      super(username, password, enterprise, apiUrl, "{{ api_prefix }}", VERSION, certificate);
   }
   
   public double getVersion() {
      return VERSION;
   }
   
   public {{ class_prefix }}{{ root_api|capitalize }} get{{ root_api|capitalize }}() {
      return ({{ class_prefix }}{{ root_api|capitalize }}) rootObject;
   }

   protected {{ class_prefix }}{{ root_api|capitalize }} createRootObject() {
      return new {{ class_prefix }}{{ root_api|capitalize }}();
   }
   
   {% if override_content -%}
   {{ override_content.replace('\n', '\n    ') }}
   {% endif -%}
}
