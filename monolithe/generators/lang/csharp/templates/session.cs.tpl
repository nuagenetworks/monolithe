{{ header }}

using net.nuagenetworks.bambou;
using System;

namespace {{ package_name }}
{

public class {{ class_prefix }}{{ product_accronym }}Session: RestSession<{{ class_prefix }}{{ root_api|capitalize }}> {
    
   public static double VERSION = {{ version }};

   public {{ class_prefix }}{{ product_accronym }}Session(String username, String password, String enterprise, String apiUrl) {
      setUsername(username);
      setPassword(password);
      setEnterprise(enterprise);
      setApiUrl(apiUrl);
      setApiPrefix("{{ api_prefix }}");
      setVersion(VERSION);
      setCertificate(null);
      setPrivateKey(null);
   }

   public {{ class_prefix }}{{ product_accronym }}Session(String username, String enterprise, String apiUrl, String certificateContent, String privateKeyContent) {
      setUsername(username);
      setEnterprise(enterprise);
      setApiUrl(apiUrl);
      setApiPrefix("nuage/api");
      setVersion(VERSION);
      setCertificate(certificateContent);
      setPrivateKey(privateKeyContent);
   }

   public double getVersion() {
      return VERSION;
   }

   public {{ class_prefix }}{{ root_api|capitalize }} get{{ root_api|capitalize }}() {
      return base.getRootObject();
   }

   {% if override_content -%}
   {{ override_content.replace('\n', '\n   ') }}
   {% endif %}
}
}
