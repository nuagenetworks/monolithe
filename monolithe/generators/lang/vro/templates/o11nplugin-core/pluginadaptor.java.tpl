{{ header }}

package {{ package_name }};

import {{ package_name }}.model.SessionManager;
import net.nuagenetworks.vro.BasePluginAdaptor;
import net.nuagenetworks.vro.BasePluginFactory;
import ch.dunes.vso.sdk.api.IPluginNotificationHandler;

public final class PluginAdaptor extends BasePluginAdaptor {
    public PluginAdaptor() {
        super(SessionManager.getInstance());
    }

    @Override
    protected BasePluginFactory createPluginFactory(IPluginNotificationHandler pluginNotificationHandler) {
        return new PluginFactory(pluginNotificationHandler);
    }
}