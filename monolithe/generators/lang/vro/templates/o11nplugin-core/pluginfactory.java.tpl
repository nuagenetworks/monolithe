{{ header }}

package {{ package_name }};

import {{ package_name }}.model.*;
import {{ package_name }}.model.fetchers.*;
import {{ package_name }}.model.enums.*;
import net.nuagenetworks.bambou.RestException;
import net.nuagenetworks.vro.BasePluginFactory;
import ch.dunes.vso.sdk.api.IPluginNotificationHandler;
import ch.dunes.vso.sdk.api.QueryResult;
import java.util.Arrays;

public final class PluginFactory extends BasePluginFactory {
    public PluginFactory(IPluginNotificationHandler pluginNotificationHandler) {
        super(pluginNotificationHandler);
    }

    @Override
    public final Object findImpl(String type, String id) throws RestException {
        if (type.equals(Constants.SESSION)) {
            return ModelHelper.getSessionById(id);
        }
        {%- for specification in specifications | sort(attribute='rest_name', case_sensitive=True) %}
        if (type.equals(Constants.{{ specification.entity_name | upper }})) {
            return ModelHelper.get{{ specification.entity_name }}ById(id);
        }
        if (type.equals(Constants.{{ specification.entity_name_plural | upper }}_FETCHER)) {
            return ModelHelper.get{{ specification.entity_name_plural }}FetcherById(id);
        }
        {%- for attribute in specification.attributes | sort(attribute='local_name', case_sensitive=True) %}
        {%- if attribute.type == "enum" or attribute.subtype == "enum" %}
        {%- set field_name = attribute.local_name[0:1].upper() + attribute.local_name[1:] %}
        {%- set enum_name = specification.entity_name + attribute.local_name[0:1].upper() + attribute.local_name[1:] %}
        if (type.equals(Constants.{{ specification.entity_name | upper }}_{{ field_name | upper }}_ENUM)) {
            return {{ enum_name }}.getEnumById(id);
        }
        {% endif -%}
        {% endfor -%}
        {% endfor -%}
        throw new UnsupportedOperationException("implement findImpl(String type, String id) - type: " + type + ", " + id);
    }

    @Override
    public final java.util.List<?> findRelationImpl(String type, String id, String relationName) throws RestException {
        if (type.equals(Constants.PLUGIN_ROOT) && relationName.equals(Constants.SESSIONS)) {
            return ModelHelper.getAllSessions();
        }
        {%- set child_api_dict = {} %}
        {%- for specification in specifications | sort(attribute='rest_name', case_sensitive=True) %}
        {%- if specification.is_root %}
        if (type.equals(Constants.SESSION) && relationName.equals(Constants.{{ specification.entity_name_plural | upper }})) {
            return toList(ModelHelper.get{{ specification.entity_name }}ById(id));
        }
        {%- endif %}
        {%- for child_api in specification.child_apis | sort(attribute='rest_name', case_sensitive=True) %}
        {%- set child_spec = specification_set[child_api.rest_name] %}
        if (type.equals(Constants.{{ specification.entity_name | upper }}) && relationName.equals(Constants.{{ child_spec.entity_name_plural | upper }}_FETCHER)) {
            return toList(ModelHelper.get{{ child_spec.entity_name_plural }}FetcherFor{{ specification.entity_name }}Id(id));
        }
        {%- if child_api.rest_name not in child_api_dict.keys() %}
        if (type.equals(Constants.{{ child_spec.entity_name_plural | upper }}_FETCHER) && relationName.equals(Constants.{{ child_spec.entity_name_plural | upper }})) {
            return ModelHelper.get{{ child_spec.entity_name_plural }}ForFetcherId(id);
        }
        {%- do child_api_dict.update({child_api.rest_name: child_api.rest_name}) %}
        {%- endif %}
        {% endfor -%}
        {% endfor -%}
        throw new UnsupportedOperationException("implement findRelationImpl(String type, String id, String relationName) - type: " + type + ", id: " + id + ", relationName: " + relationName);
    }

    @Override
    public QueryResult findAllImpl(String type, String query) throws RestException {
        if (type.equals(Constants.SESSION)) {
            java.util.List<Session> allSessions = ModelHelper.getAllSessions();
            return new QueryResult(allSessions);
        }
        {%- for specification in specifications | sort(attribute='rest_name', case_sensitive=True) %}
        if (type.equals(Constants.{{ specification.entity_name | upper }})) {
            java.util.List<{{ specification.entity_name }}> allObjs = ModelHelper.getAll{{ specification.entity_name_plural }}();
            return new QueryResult(allObjs);
        }
        if (type.equals(Constants.{{ specification.entity_name_plural | upper }}_FETCHER)) {
            java.util.List<{{ specification.entity_name_plural }}Fetcher> allObjs = ModelHelper.getAll{{ specification.entity_name_plural }}Fetchers();
            return new QueryResult(allObjs);
        }
        {%- for attribute in specification.attributes | sort(attribute='local_name', case_sensitive=True) %}
        {%- if attribute.type == "enum" or attribute.subtype == "enum" %}
        {%- set field_name = attribute.local_name[0:1].upper() + attribute.local_name[1:] %}
        {%- set enum_name = specification.entity_name + attribute.local_name[0:1].upper() + attribute.local_name[1:] %}
        if (type.equals(Constants.{{ specification.entity_name | upper }}_{{ field_name | upper }}_ENUM)) {
            return new QueryResult(Arrays.asList({{ enum_name }}.values()));
        }
        {% endif -%}
        {% endfor -%}
        {% endfor -%}
        throw new UnsupportedOperationException("implement findAll(String type, String query) - type: " + type + ", query: " + query);
    }
}

