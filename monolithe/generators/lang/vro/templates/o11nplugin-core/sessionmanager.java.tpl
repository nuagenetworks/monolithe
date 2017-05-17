{{ header }}

package {{ package_name }};

import net.nuagenetworks.bambou.RestException;
import net.nuagenetworks.vro.model.BaseSessionManager;
import com.vmware.o11n.plugin.sdk.annotation.VsoMethod;
import com.vmware.o11n.plugin.sdk.annotation.VsoObject;
import ch.dunes.vso.sdk.api.IPluginFactory;
import java.util.List;

@VsoObject(create = false, strict = true, singleton = true)
public class SessionManager extends BaseSessionManager<Session> {
    private static SessionManager instance;

    public SessionManager() {
        super(Constants.PLUGIN_ROOT, Constants.PLUGIN_CONFIG_FILENAME);
    }

    public static SessionManager getInstance() {
        if (instance == null) {
            instance = new SessionManager();
        }

        return instance; 
    }

    public static SessionManager createScriptingSingleton(IPluginFactory factory) {
        return getInstance();
    }

    @Override
    protected Session createSession(String username, String password, String enterprise, String apiUrl) {
        return new Session(username, password, enterprise, apiUrl);
    }

    @Override
    protected Session createSession(String username, String enterprise, String apiUrl, String certificateContent, String privateKeyContent) {
        return new Session(username, enterprise, apiUrl, certificateContent, privateKeyContent);
    }

    @VsoMethod
    public void addSession(Session session) throws RestException {
        super.addSession(session);
    }

    @VsoMethod
    public void removeSession(Session session) throws RestException {
        super.removeSession(session);
    }

    @VsoMethod
    public Session getSessionById(String sessionId) {
        return super.getSessionById(sessionId);
    }

    @VsoMethod
    public List<Session> getSessions() {
        return super.getSessions();
    }
}
