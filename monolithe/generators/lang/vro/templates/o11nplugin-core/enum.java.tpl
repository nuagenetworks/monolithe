{{ header }}

package {{ package_name }}.enums;

import {{ package_name }}.Constants;

import com.vmware.o11n.plugin.sdk.annotation.VsoFinder;
import com.vmware.o11n.plugin.sdk.annotation.VsoObject;
import com.vmware.o11n.plugin.sdk.annotation.VsoProperty;

@VsoFinder(name = Constants.{{ specification.entity_name | upper }}_{{ attribute.local_name | upper }}_ENUM, datasource = Constants.DATASOURCE, idAccessor = Constants.ID_ACCESSOR)
@VsoObject(strict = true)
public enum {{ enum_name }} {

    {% for choice in attribute.allowed_choices %}{{ choice }}("{{ choice }}", "{{ choice }}"){% if not loop.last %}, {% endif %}{% endfor %};

    private final String id;
    private final String name;
   
    {{ enum_name }}(String id, String name) {
        this.id = id;
        this.name = name;
    }
   
    @VsoProperty(displayName = "Id", readOnly = true)
    public String getId() {
        return id;
    }
   
    @VsoProperty(displayName = "Name", readOnly = true)
    public String getName() {
        return name;
    }

    {% for choice in attribute.allowed_choices %}
    @VsoProperty(displayName = "{{ choice }}", readOnly = true)
    public {{ enum_name }} get{{ choice }}() {
        return {{ choice }};
    }
    {% endfor %}

    public static {{ enum_name }} getEnumById(String id) {
        for ({{ enum_name }} item : values()) {
            if (item.getId().equals(id)) {
                return item;
            }
        }
        return null;
    }
};
