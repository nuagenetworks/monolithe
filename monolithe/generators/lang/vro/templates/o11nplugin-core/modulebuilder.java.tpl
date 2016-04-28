{{ header }}

package {{ package_name }};

import {{ package_name }}.model.Constants;
import net.nuagenetworks.vro.BaseModuleBuilder;

public final class ModuleBuilder extends BaseModuleBuilder {
    public ModuleBuilder() {
        super(PluginAdaptor.class, ModuleBuilder.class.getPackage().getName(), Constants.PLUGIN_NAME, Constants.PLUGIN_DESCRIPTION, Constants.PLUGIN_ROOT,
                Constants.PLUGIN_IMAGE_FILENAME);
    }
}