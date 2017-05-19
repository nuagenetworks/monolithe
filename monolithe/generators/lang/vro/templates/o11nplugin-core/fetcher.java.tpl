{{ header }}

package {{ package_name }}.fetchers;

import {{ package_name }}.{{ specification.entity_name }};
import {{ package_name }}.Session;
import {{ package_name }}.Constants;
{%- for parent_api in specification.parent_apis | sort(attribute='rest_name', case_sensitive=True) %}
{%- set parent_spec = specification_set[parent_api.rest_name] %}
{%- if parent_spec is defined %}
import {{ package_name }}.{{ parent_spec.entity_name }};
{% endif -%}
{% endfor -%}
import net.nuagenetworks.vro.model.fetchers.BaseFetcher;
import net.nuagenetworks.bambou.RestException;
import net.nuagenetworks.bambou.RestObject;
import com.vmware.o11n.plugin.sdk.annotation.VsoFinder;
import com.vmware.o11n.plugin.sdk.annotation.VsoMethod;
import com.vmware.o11n.plugin.sdk.annotation.VsoObject;
import com.vmware.o11n.plugin.sdk.annotation.VsoProperty;
import com.vmware.o11n.plugin.sdk.annotation.VsoRelation;

@VsoFinder(name = Constants.{{ specification.entity_name_plural | upper }}_FETCHER, datasource = Constants.DATASOURCE, image = Constants.FOLDER_IMAGE_FILENAME, idAccessor = Constants.ID_ACCESSOR, relations = {
        @VsoRelation(inventoryChildren = true, name = Constants.{{ specification.entity_name_plural | upper }}, type = Constants.{{ specification.entity_name | upper }}) })
@VsoObject(create = false, strict = true)
public class {{ specification.entity_name_plural }}Fetcher extends BaseFetcher<{{ specification.entity_name }}> {
    private static final long serialVersionUID = 1L;

    public {{ specification.entity_name_plural }}Fetcher(RestObject parentRestObj) {
        super(parentRestObj, {{ specification.entity_name }}.class);
    }

    @VsoProperty(displayName = "Id", readOnly = true)
    public String getId() {
        return super.getParentRestObj().getId();
    }

    @VsoProperty(displayName = "Name", readOnly = true)
    public String getName() {
        return "{{ specification.entity_name_plural }}";
    }

    @VsoProperty(displayName = "Session", readOnly = true)
    public Session getSession() {
        return (Session) super.getSession();
    }

    {%- for parent_api in specification.parent_apis | sort(attribute='rest_name', case_sensitive=True) %}
    {%- set parent_spec = specification_set[parent_api.rest_name] %}
    {%- if parent_spec is defined %}
    @VsoProperty(displayName = "{{ parent_spec.entity_name }}", readOnly = true)
    public {{ parent_spec.entity_name }} get{{ parent_spec.entity_name }}() {
        RestObject obj = super.getParentRestObj();
        if (obj instanceof {{ parent_spec.entity_name }}) {
            return ({{ parent_spec.entity_name }}) obj;
        }
        
        return null;
    }
    {% endif -%}
    {% endfor -%}

    @VsoMethod
    public java.util.List<{{ specification.entity_name }}> fetch(Session session, String filter, String orderBy, String[] groupBy, Integer page, Integer pageSize, String queryParameters, Boolean commitObj) throws RestException {
        boolean commit = (commitObj != null) ? commitObj.booleanValue() : true;
        return super.fetch(session, filter, orderBy, groupBy, page, pageSize, queryParameters, commit);
    }

    @VsoMethod
    public java.util.List<{{ specification.entity_name }}> get(Session session, String filter, String orderBy, String[] groupBy, Integer page, Integer pageSize, String queryParameters, Boolean commitObj) throws RestException {
        boolean commit = (commitObj != null) ? commitObj.booleanValue() : true;
        return super.get(session, filter, orderBy, groupBy, page, pageSize, queryParameters, commit);
    }

    @VsoMethod
    public {{ specification.entity_name }} getFirst(Session session, String filter, String orderBy, String[] groupBy, Integer page, Integer pageSize, String queryParameters, Boolean commitObj) throws RestException {
        boolean commit = (commitObj != null) ? commitObj.booleanValue() : true;
        return super.getFirst(session, filter, orderBy, groupBy, page, pageSize, queryParameters, commit);
    }

    @VsoMethod
    public int count(Session session, String filter, String orderBy, String[] groupBy, Integer page, Integer pageSize, String queryParameters, Boolean commitObj) throws RestException {
        boolean commit = (commitObj != null) ? commitObj.booleanValue() : true;
        return super.count(session, filter, orderBy, groupBy, page, pageSize, queryParameters, commit);
    }
}
