{{ header }}

using net.nuagenetworks.bambou.RestSession;
using net.nuagenetworks.bambou.RestException;
using net.nuagenetworks.bambou.ssl.DynamicKeystoreGenerator;
using net.nuagenetworks.bambou.service.RestClientTemplate;
using net.nuagenetworks.bambou.spring.SpringConfig;

namespace {{ package_name }}
{

public class {{ class_prefix }}{{ product_accronym }}Session: RestSession<{{ class_prefix }}{{ root_api|capitalize }}> {
    
   public static double VERSION = {{ version }};
   
   private RestClientTemplate restClientTemplate;

   public {{ class_prefix }}{{ product_accronym }}Session() {
      base({{ class_prefix }}{{ root_api|capitalize }}.class);
   
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
      return base.getRootObject();
   }

   {% if override_content -%}
   {{ override_content.replace('\n', '\n   ') }}
   {% endif %}
}
}
