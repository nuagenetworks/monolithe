{{ header }}
using System;

namespace {{ package_name }}
{
    public class SdkInfo 
    {
       public double API_VERSION      = {{ version }};
       public String API_PREFIX       = "{{ api_prefix }}";
       public String PRODUCT_ACCRONYM = "{{ product_accronym }}";
       public String PRODUCT_NAME     = "{{ product_name }}";
       public String CLASS_PREFIX     = "{{ class_prefix }}";
       public String NAME             = "{{ name }}";
       public String ROOT_API         = "{{ root_api }}";
       public Type ROOT_OBJECT_CLASS  = typeof({{ class_prefix }}{{ root_api|capitalize }});
       public Type SESSION_CLASS      = typeof({{ class_prefix }}{{ product_accronym }}Session);
    }
}
