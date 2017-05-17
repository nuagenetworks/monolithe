{{ header }}

package {{ package_name }};

import java.security.KeyManagementException;
import java.io.File;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;

import net.nuagenetworks.bambou.RestSession;
import net.nuagenetworks.bambou.RestException;
import net.nuagenetworks.bambou.ssl.DynamicKeystoreGenerator;
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
      this();
 
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
      this();
 
      setUsername(username);
      setEnterprise(enterprise);
      setApiUrl(apiUrl);
      setApiPrefix("nuage/api");
      setVersion(VERSION);
      setCertificate(certificateContent);
      setPrivateKey(privateKeyContent);
   }

   public {{ class_prefix }}{{ product_accronym }}Session(String username, String enterprise, String apiUrl, File pathToCertificatePEMFile, File pathToPrivateKeyPEMFile) throws RestException {
      this();
        
      try {
         String certificateContent = DynamicKeystoreGenerator.getContentsOfPEMFile(pathToCertificatePEMFile);
         String privateKeyContent = DynamicKeystoreGenerator.getContentsOfPEMFile(pathToPrivateKeyPEMFile);
                       
         setUsername(username);
         setEnterprise(enterprise);
         setApiUrl(apiUrl);
         setApiPrefix("nuage/api");
         setVersion(VERSION);
         setCertificate(certificateContent);
         setPrivateKey(privateKeyContent);        
      } catch (KeyManagementException ex) {
         throw new RestException(ex);
      }
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
