{{ header }}

package {{ package_name }};

import {{ package_name }}.fetchers.*;

import net.nuagenetworks.vro.model.fetchers.BaseFetcher;
import net.nuagenetworks.vro.model.BaseObjectExtensions;
import net.nuagenetworks.vro.model.BaseModelHelper;
import net.nuagenetworks.bambou.RestException;
import org.springframework.web.client.HttpClientErrorException;
import java.util.ArrayList;

public class ModelHelper extends BaseModelHelper {

    public static java.util.List<Session> getAllSessions() {
        return SessionManager.getInstance().getSessions();
    }

    public static Session getSessionById(String id) {
        return SessionManager.getInstance().getSessionById(id);
    }
    
    {% for specification in specifications | sort(attribute='rest_name', case_sensitive=True) %}
    public static {{ specification.entity_name }} get{{ specification.entity_name }}ById(String id) {
        for (Session session : SessionManager.getInstance().getSessions()) {
            {{ specification.entity_name }} obj = null;
            {%- if specification.is_root %}
            obj = session.get{{ specification.entity_name }}();
            if (obj.getId().equals(id)) {
                return addObject(Constants.{{ specification.entity_name | upper }}, obj);
            }
            {% else %}
            obj = new {{ specification.entity_name }}();
            obj.setId(id);

            try {
                session.fetch(obj);
                return addObject(Constants.{{ specification.entity_name | upper }}, obj);
            } catch (RestException | HttpClientErrorException ex) {
                // Object not found in session
            }

            {% endif %}
        }

        return null;
    }

    {%- for child_api in specification.child_apis | sort(attribute='rest_name', case_sensitive=True) %}
    {%- set child_spec = specification_set[child_api.rest_name] %}
    public static {{ child_spec.entity_name_plural }}Fetcher get{{ child_spec.entity_name_plural }}FetcherFor{{ specification.entity_name }}Id(String id) throws RestException {
        {{ specification.entity_name }} obj = getObject(Constants.{{ specification.entity_name | upper }}, id);
        if (obj == null) {
            obj = get{{ specification.entity_name }}ById(id);
        }

        if (obj != null) {
            {{ child_spec.entity_name_plural }}Fetcher fetcher = obj.get{{ child_spec.entity_name_plural }}();
            return addFetcher(Constants.{{ child_spec.entity_name_plural | upper }}_FETCHER, fetcher);
        }

        return null;
    }
    {% endfor -%}

    public static java.util.List<{{ specification.entity_name }}> get{{ specification.entity_name_plural }}ForFetcherId(String id) throws RestException {
        {{ specification.entity_name_plural }}Fetcher fetcher = get{{ specification.entity_name_plural }}FetcherById(id);
        if (fetcher != null) {
            try {
                Session session = fetcher.getSession();
                session.fetch(fetcher);
                return addFetcherObjects(fetcher, Constants.{{ specification.entity_name | upper }});
            } catch (RestException | HttpClientErrorException ex) {
                // Error fetching objects
            }
        }

        return new ArrayList<{{ specification.entity_name }}>();
    }

    public static {{ specification.entity_name_plural }}Fetcher get{{ specification.entity_name_plural }}FetcherById(String id) throws RestException {
        BaseFetcher<? extends BaseObjectExtensions> fetcher = getFetcher(Constants.{{ specification.entity_name_plural | upper }}_FETCHER, id);
        if (fetcher != null) {
            return ({{ specification.entity_name_plural }}Fetcher) fetcher;
        }

        {%- for parent_api in specification.parent_apis | sort(attribute='rest_name', case_sensitive=True) %}
        {%- set parent_spec = specification_set[parent_api.rest_name] %}
        {%- if parent_spec is defined %}
        if ((fetcher = get{{ specification.entity_name_plural }}FetcherFor{{ parent_spec.entity_name }}Id(id)) != null) {
            return ({{ specification.entity_name_plural }}Fetcher) addFetcher(Constants.{{ specification.entity_name_plural | upper }}_FETCHER, fetcher);
        }
        {% endif -%}
        {% endfor -%}
        return null;
    }

    public static java.util.List<{{ specification.entity_name }}> getAll{{ specification.entity_name_plural }}() throws RestException {
        java.util.List<{{ specification.entity_name }}> allObjs = new ArrayList<{{ specification.entity_name }}>();

        {%- for parent_api in specification.parent_apis | sort(attribute='rest_name', case_sensitive=True) %}
        {%- set parent_spec = specification_set[parent_api.rest_name] %}
        {%- if parent_spec is defined and parent_spec.is_root %}
        for (Session session : SessionManager.getInstance().getSessions()) {
            {{ specification.entity_name_plural }}Fetcher fetcher = get{{ specification.entity_name_plural }}FetcherFor{{ parent_spec.entity_name }}Id(session.getId());
            java.util.List<{{ specification.entity_name }}> objs = session.fetch(fetcher);
            allObjs.addAll(objs);
        }
        {% endif -%}
        {% endfor %}

        return allObjs;
    }

    public static java.util.List<{{ specification.entity_name_plural }}Fetcher> getAll{{ specification.entity_name_plural }}Fetchers() throws RestException {
        java.util.List<{{ specification.entity_name_plural }}Fetcher> allObjs = new ArrayList<{{ specification.entity_name_plural }}Fetcher>();
        return allObjs;
    } 

    {%- endfor %}
}