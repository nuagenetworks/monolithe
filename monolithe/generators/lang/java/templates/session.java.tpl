{{ header }}

package {{ package_name }};

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;

import net.nuagenetworks.bambou.RestSession;
import net.nuagenetworks.bambou.service.RestClientTemplate;
import net.nuagenetworks.bambou.spring.SpringConfig;

public class {{ class_prefix }}{{ product_accronym }}Session extends RestSession<{{ class_prefix }}{{ root_api|capitalize }}> {
    
   public final static double VERSION = {{ version }};
   
   @Autowired
   private RestClientTemplate restClientTemplate;

   public {{ class_prefix }}{{ product_accronym }}Session() {
      super({{ class_prefix }}{{ root_api|capitalize }}.class);
   
      try (AnnotationConfigApplicationContext applicationContext = new AnnotationConfigApplicationContext(SpringConfig.class)) {
         applicationContext.getAutowireCapableBeanFactory().autowireBean(this);
      }
   }

   public {{ class_prefix }}{{ product_accronym }}Session(String username, String password, String enterprise, String apiUrl) {
      this(username, password, enterprise, apiUrl, null);
   }

   public {{ class_prefix }}{{ product_accronym }}Session(String username, String password, String enterprise, String apiUrl, String certificate) {
      this();

      setUsername(username);
      setPassword(password);
      setEnterprise(enterprise);
      setApiUrl(apiUrl);
      setApiPrefix("{{ api_prefix }}");
      setVersion(VERSION);
      setCertificate(certificate);
   }

   public double getVersion() {
      return VERSION;
   }
   
   public RestClientTemplate getClientTemplate() {
      return restClientTemplate;
   }

   public {{ class_prefix }}{{ root_api|capitalize }} get{{ root_api|capitalize }}() {
      return super.getRootObject();
   }

   {% if override_content -%}
   {{ override_content.replace('\n', '\n   ') }}
   {% endif %}
}
