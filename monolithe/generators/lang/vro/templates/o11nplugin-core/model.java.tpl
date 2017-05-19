{{ header }}

package {{ package_name }};

{%- for child_api in specification.child_apis | sort(attribute='rest_name', case_sensitive=True) %}
{%- set child_spec = specification_set[child_api.rest_name] %}
import {{ package_name }}.fetchers.{{ child_spec.entity_name_plural }}Fetcher;
{% endfor -%}
{% for attribute in specification.attributes | sort(attribute='local_name', case_sensitive=True) %}
{%- if attribute.type == "enum" or attribute.subtype == "enum" %}
{%- set enum_name = specification.entity_name + attribute.local_name[0:1].upper() + attribute.local_name[1:] %}
import {{ package_name }}.enums.{{ enum_name }};
{% endif -%}
{% endfor -%}
import net.nuagenetworks.bambou.RestException;
import net.nuagenetworks.bambou.annotation.RestEntity;
import net.nuagenetworks.vro.model.{{ superclass_name }};
import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
{%- if specification.attributes|length > 0 %} 
import com.fasterxml.jackson.annotation.JsonProperty;
{% endif -%}
import com.fasterxml.jackson.annotation.JsonIgnore;
import com.vmware.o11n.plugin.sdk.annotation.VsoConstructor;
import com.vmware.o11n.plugin.sdk.annotation.VsoFinder;
import com.vmware.o11n.plugin.sdk.annotation.VsoMethod;
import com.vmware.o11n.plugin.sdk.annotation.VsoObject;
import com.vmware.o11n.plugin.sdk.annotation.VsoProperty;
import com.vmware.o11n.plugin.sdk.annotation.VsoRelation;

@VsoFinder(name = Constants.{{ specification.entity_name | upper }}, datasource = Constants.DATASOURCE, image = Constants.{{ specification.entity_name | upper }}_IMAGE_FILENAME, idAccessor = Constants.ID_ACCESSOR, relations = {
{%- for child_api in specification.child_apis | sort(attribute='rest_name', case_sensitive=True) %}
{%- set child_spec = specification_set[child_api.rest_name] %}
{%- if ((child_api.allows_get and child_api.allows_create) and not child_spec.entity_name in entity_excludes) or (child_spec.entity_name in entity_includes) %}
        @VsoRelation(inventoryChildren = true, name = Constants.{{ child_spec.entity_name_plural | upper }}_FETCHER, type = Constants.{{ child_spec.entity_name_plural | upper }}_FETCHER){% if not loop.last %}, {% endif %}
{% endif -%}
{% endfor -%}
})
@VsoObject(create = false, strict = true)
@JsonIgnoreProperties(ignoreUnknown = true)
@RestEntity(restName = "{{ specification.rest_name }}", resourceName = "{{ specification.resource_name }}")
public class {{ specification.entity_name }} extends {{ superclass_name }} {

    private static final long serialVersionUID = 1L;

    {% for attribute in specification.attributes | sort(attribute='local_name', case_sensitive=True) %}
    @JsonProperty(value = "{{ attribute.name }}")
    protected {{ attribute.local_type }} {{ attribute.local_name }};
    {% endfor %}

    {%- for child_api in specification.child_apis | sort(attribute='rest_name', case_sensitive=True)%}
    {%- set child_spec = specification_set[child_api.rest_name] %}
    @JsonIgnore
    private {{ child_spec.instance_name_plural }}Fetcher {{ child_spec.instance_name_plural[0:1].lower() + child_spec.instance_name_plural[1:] }};
    {% endfor -%}

{%- set add_warning = {} %}
{%- for attribute, value in attribute_defaults.iteritems() %}{% if value.startswith(attribute + '.') %}{% set _ = add_warning.update({'enabled' : True}) %}{% endif %}{% endfor %}
{%- if add_warning %}   @SuppressWarnings("static-access"){% endif %}
    @VsoConstructor
    public {{ specification.entity_name }}() {
        {%- for attribute, value in attribute_defaults.iteritems() %}
        {{attribute}} = {{value}};
        {% endfor -%}

        {%- for child_api in specification.child_apis | sort(attribute='rest_name', case_sensitive=True) %}
        {%- set child_spec = specification_set[child_api.rest_name] %}
        {{ child_spec.instance_name_plural[0:1].lower() + child_spec.instance_name_plural[1:] }} = new {{ child_spec.entity_name_plural }}Fetcher(this);
        {% endfor -%}
    }

    @VsoProperty(displayName = "Session", readOnly = true)
    public Session getSession() {
        return (Session) super.getSession();
    }

    {%- set name_attribute_already_defined = {} %}{% for attribute in specification.attributes | sort(attribute='local_name', case_sensitive=True) %}{% if attribute.local_name == "name" %}{% set _ = name_attribute_already_defined.update({'enabled' : True}) %}{% endif %}{% endfor %}
    {%- if not name_attribute_already_defined %}
    @VsoProperty(displayName = "Name", readOnly = false)
    public String getName() {
        return {% if specification.is_root %}"{{ specification.entity_name }}"{% else %}get{{ entity_name_attr[0:1].upper() + entity_name_attr[1:] }}(){% endif %};
    }
    {% endif -%}

    @VsoProperty(displayName = "RestName", readOnly = true)
    public String getRestName() {
        return super.getRestName();
    }

    {%- set id_attribute_already_defined = {} %}{% for attribute in specification.attributes | sort(attribute='local_name', case_sensitive=True) %}{% if attribute.local_name == "id" %}{% set _ = id_attribute_already_defined.update({'enabled' : True}) %}{% endif %}{% endfor %}
    {%- if not id_attribute_already_defined %}
    @VsoProperty(displayName = "Id", readOnly = false)
    public String getId() {
        return super.getId();
    }
    {% endif -%}

    @VsoProperty(displayName = "ParentId", readOnly = false)
    public String getParentId() {
        return super.getParentId();
    }

    @VsoProperty(displayName = "ParentType", readOnly = false)
    public String getParentType() {
        return super.getParentType();
    }

    @VsoProperty(displayName = "CreationDate", readOnly = false)
    public String getCreationDate() {
        return super.getCreationDate();
    }

    @VsoProperty(displayName = "UpdatedDate", readOnly = false)
    public String getLastUpdatedDate() {
        return super.getLastUpdatedDate();
    }

    @VsoProperty(displayName = "Owner", readOnly = false)
    public String getOwner() {
        return super.getOwner();
    }

    {%- if specification.is_root %}
    @VsoProperty(displayName = "ApiKey", readOnly = false)
    public String getApiKey() {
        return super.getApiKey();
    }
    {% endif -%}
    {%- for attribute in specification.attributes | sort(attribute='local_name', case_sensitive=True) %}
    {%- set field_name = attribute.local_name[0:1].upper() + attribute.local_name[1:] %}
    @JsonIgnore
    @VsoProperty(displayName = "{{ field_name }}", readOnly = false)   
    public {{ attribute.local_type }} get{{ field_name }}() {
       return {{ attribute.local_name }};
    }

    @JsonIgnore
    public void set{{ field_name }}({{ attribute.local_type }} value) { 
        this.{{ attribute.local_name }} = value;
    }
    {% endfor -%}

    {%- for child_api in specification.child_apis | sort(attribute='rest_name', case_sensitive=True) %}
    {%- set child_spec = specification_set[child_api.rest_name] %}
    @JsonIgnore
    @VsoProperty(displayName = "{{ child_spec.instance_name_plural }}", readOnly = true)   
    public {{ child_spec.instance_name_plural }}Fetcher get{{ child_spec.entity_name_plural }}() {
        return {{ child_spec.entity_name_plural[0:1].lower() + child_spec.entity_name_plural[1:] }};
    }
    {% endfor -%}

    @VsoMethod
    public void fetch(Session session) throws RestException {
        super.fetch(session);
    }

    @VsoMethod
    public void save(Session session, Integer responseChoice) throws RestException {
        super.save(session, responseChoice);
        if (!session.getNotificationsEnabled()) {
           SessionManager.getInstance().notifyElementUpdated(Constants.{{ specification.entity_name | upper }}, getId());
        }
    }

    @VsoMethod
    public void delete(Session session, Integer responseChoiceObj) throws RestException {
        int responseChoice = (responseChoiceObj != null) ? responseChoiceObj.intValue() : 1;
        super.delete(session, responseChoice);
        if (!session.getNotificationsEnabled()) {
           SessionManager.getInstance().notifyElementDeleted(Constants.{{ specification.entity_name | upper }}, getId());
        }
    }

    {%- for child_api in specification.child_apis | sort(attribute='rest_name', case_sensitive=True) %}
    {%- if child_api.allows_update %}
    {%- set child_spec = specification_set[child_api.rest_name] %}
    @VsoMethod
    public void assign{{ child_spec.entity_name_plural }}(Session session, {{ child_spec.entity_name }}[] childRestObjs, Boolean commitObj) throws RestException {
        boolean commit = (commitObj != null) ? commitObj.booleanValue() : true;
        super.assign(session, java.util.Arrays.asList(childRestObjs), commit);
        if (!session.getNotificationsEnabled()) { 
           SessionManager.getInstance().notifyElementUpdated(Constants.{{ specification.entity_name | upper }}, getId());
        }
    }
    {% endif -%}
    {% endfor -%}

    {%- for child_api in specification.child_apis | sort(attribute='rest_name', case_sensitive=True) %}
    {%- if child_api.allows_create %}
    {%- set child_spec = specification_set[child_api.rest_name] %}
    @VsoMethod
    public void create{{ child_spec.entity_name }}(Session session, {{ child_spec.entity_name }} childRestObj, Integer responseChoice, Boolean commitObj) throws RestException {
        boolean commit = (commitObj != null) ? commitObj.booleanValue() : true;
        super.createChild(session, childRestObj, responseChoice, commit);
        if (!session.getNotificationsEnabled()) {
           SessionManager.getInstance().notifyElementInvalidate(Constants.{{ child_spec.entity_name_plural | upper }}_FETCHER, getId());
        }
    }

    {%- for attribute in child_spec.attributes | sort(attribute='local_name', case_sensitive=True) %}
    {%- if attribute.local_name == "templateID" %}
    @VsoMethod
    public void instantiate{{ child_spec.entity_name }}(Session session, {{ child_spec.entity_name }} childRestObj, {{ child_spec.entity_name }}Template fromTemplate, Integer responseChoice, Boolean commitObj) throws RestException {
        boolean commit = (commitObj != null) ? commitObj.booleanValue() : true;
        super.instantiateChild(session, childRestObj, fromTemplate, responseChoice, commit);
        if (!session.getNotificationsEnabled()) {
           SessionManager.getInstance().notifyElementInvalidate(Constants.{{ child_spec.entity_name_plural | upper }}_FETCHER, getId());
        }
    }
    {% endif -%}
    {% endfor -%}

    {% endif -%}
    {% endfor -%}

    public String toString() {
        return "{{ specification.entity_name }} ["{% for attribute in specification.attributes | sort(attribute='local_name', case_sensitive=True) %} + "{% if not loop.first %}, {% endif %}{{ attribute.local_name }}=" + {{ attribute.local_name }}{% endfor %} + ", id=" + id + ", parentId=" + parentId + ", parentType=" + parentType + ", creationDate=" + creationDate + ", lastUpdatedDate="
                 + lastUpdatedDate + ", owner=" + owner {% if specification.is_root %} + ", apiKey=" + apiKey {% endif %} + "]";
    }
}
