{{ header }}

package {{ package_name }};

public interface SdkInfo {

   double API_VERSION      = {{ version }};
   String API_PREFIX       = "{{ api_prefix }}";
   String PRODUCT_ACCRONYM = "{{ product_accronym }}";
   String PRODUCT_NAME     = "{{ product_name }}";
   String CLASS_PREFIX     = "{{ class_prefix }}";
   String NAME             = "{{ name }}";
   String ROOT_API         = "{{ root_api }}";
   Class<?> ROOT_OBJECT_CLASS  = {{ class_prefix }}{{ root_api|capitalize }}.class;
   Class<?> SESSION_CLASS      = {{ class_prefix }}{{ product_accronym }}Session.class;
}
