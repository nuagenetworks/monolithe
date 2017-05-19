{{ header }}

package {{ package_name }};

import net.nuagenetworks.bambou.RestException;
import net.nuagenetworks.bambou.spring.SpringConfig;
import net.nuagenetworks.vro.model.BaseSession;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import com.vmware.o11n.plugin.sdk.annotation.VsoConstructor;
import com.vmware.o11n.plugin.sdk.annotation.VsoFinder;
import com.vmware.o11n.plugin.sdk.annotation.VsoMethod;
import com.vmware.o11n.plugin.sdk.annotation.VsoObject;
import com.vmware.o11n.plugin.sdk.annotation.VsoProperty;
import com.vmware.o11n.plugin.sdk.annotation.VsoRelation;

@VsoFinder(name = Constants.SESSION, datasource = Constants.DATASOURCE, image = Constants.SESSION_IMAGE_FILENAME, idAccessor = Constants.ID_ACCESSOR, relations = {
               @VsoRelation(inventoryChildren = true, name = Constants.{{ root_entity.entity_name_plural | upper }}, type = Constants.{{ root_entity.entity_name | upper }}) })
@VsoObject(create = false, strict = true)
public class Session extends BaseSession<{{ root_entity.entity_name }}> {
    public final static double VERSION = {{ version }};

    @VsoConstructor
    public Session() {
        super({{ root_entity.entity_name }}.class);

        ClassLoader classLoader = getClass().getClassLoader();

        try (final AnnotationConfigApplicationContext applicationContext = new AnnotationConfigApplicationContext()) {
            applicationContext.setClassLoader(classLoader);
            applicationContext.register(SpringConfig.class);
            applicationContext.refresh();
            applicationContext.getAutowireCapableBeanFactory().autowireBean(this);
        }
    }

    @VsoConstructor
    public Session(String username, String password, String enterprise, String apiUrl) {
        this();
 
        setUsername(username);
        setPassword(password);
        setEnterprise(enterprise);
        setApiUrl(apiUrl);
        setApiPrefix("nuage/api");
        setVersion(VERSION);
        setCertificate(null);
        setPrivateKey(null);
    }

    @VsoConstructor
    public Session(String username, String enterprise, String apiUrl, String certificateContent, String privateKeyContent) {
        this();
 
        setUsername(username);
        setEnterprise(enterprise);
        setApiUrl(apiUrl);
        setApiPrefix("nuage/api");
        setVersion(VERSION);
        setCertificate(certificateContent);
        setPrivateKey(privateKeyContent);
    }

    @VsoProperty(displayName = "notificationsEnabled")
    public boolean getNotificationsEnabled() {
        return super.getNotificationsEnabled();
    }
    public void setNotificationsEnabled(boolean notificationsEnabled) {
        super.setNotificationsEnabled(notificationsEnabled);
    }

    @VsoProperty(displayName = "useJmsForNotifications")
    public boolean getUseJmsForNotifications() {
        return super.getUseJmsForNotifications();
    }
    public void setUseJmsForNotifications(boolean useJmsForNotifications) {
        super.setUseJmsForNotifications(useJmsForNotifications);
    }

    @VsoProperty(displayName = "Id", readOnly = true)
    public String getId() {
        return super.getId();
    }

    @VsoProperty(displayName = "Name", readOnly = true)
    public String getName() {
        return getApiUrl();
    }

    @VsoProperty(displayName = "Version", readOnly = true)
    public double getVersion() {
        return VERSION;
    }

    @VsoMethod
    public {{ root_api|capitalize }} get{{ root_api|capitalize }}() {
        return super.getRootObject();
    }

    @VsoProperty(displayName = "Username", readOnly = false)
    public String getUsername() {
        return super.getUsername();
    }

    public String getPassword() {
        return super.getPassword();
    }

    @VsoProperty(displayName = "Enterprise", readOnly = false)
    public String getEnterprise() {
        return super.getEnterprise();
    }

    @VsoProperty(displayName = "ApiUrl", readOnly = false)
    public String getApiUrl() {
        return super.getApiUrl();
    }

    @VsoProperty(displayName = "ApiPrefix", readOnly = false)
    public String getApiPrefix() {
        return super.getApiPrefix();
    }

    @VsoProperty(displayName = "Certificate", readOnly = false)
    public String getCertificate() {
        return super.getCertificate();
    }

    @VsoProperty(displayName = "PrivateKey", readOnly = false)
    public String getPrivateKey() {
        return super.getPrivateKey();
    }

    @VsoMethod
    public void start() throws RestException {
        super.start();
    }

    @VsoMethod
    public void stop() {
        super.stop();
    }

    @Override
    protected void onEntityCreated(String entityType, String entityId, String entityParentType, String entityParentId) {
        SessionManager sessionManager = SessionManager.getInstance();

        {%- for specification in specifications | sort(attribute='rest_name', case_sensitive=True) %}
        if (entityType.equals(Constants.{{ specification.entity_name | upper }}_ENTITY_TYPE)) {
            notifyElementInvalidate(sessionManager, Constants.{{ specification.entity_name_plural | upper }}_FETCHER, entityParentId);
            return;
        }
        {% endfor -%}
    }

    @Override
    protected void onEntityUpdated(String entityType, String entityId, String entityParentType, String entityParentId) {
        SessionManager sessionManager = SessionManager.getInstance();

        {%- for specification in specifications | sort(attribute='rest_name', case_sensitive=True) %}
        if (entityType.equals(Constants.{{ specification.entity_name | upper }}_ENTITY_TYPE)) {
            sessionManager.notifyElementUpdated(Constants.{{ specification.entity_name | upper }}, entityId);
            return;
        }
        {% endfor -%}
    }

    @Override
    protected void onEntityDeleted(String entityType, String entityId, String entityParentType, String entityParentId) {
        SessionManager sessionManager = SessionManager.getInstance();

        {%- for specification in specifications | sort(attribute='rest_name', case_sensitive=True) %}
        if (entityType.equals(Constants.{{ specification.entity_name | upper }}_ENTITY_TYPE)) {
            sessionManager.notifyElementDeleted(Constants.{{ specification.entity_name | upper }}, entityId);
            return;
        }
        {% endfor -%}
    }
}
