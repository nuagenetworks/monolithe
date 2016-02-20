{{ header }}

package {{ sdk_name }}

import (
    "github.com/nuagenetworks/go-bambou/bambou"
    "fmt"
    "strings"
)

var (
    _URLPostfix string
)

func NewSession(username, password, organization, url string) (*bambou.Session, *{{sdk_root_api|capitalize}}) {

    root := New{{sdk_root_api|capitalize}}()
    url += _URLPostfix

    session := bambou.NewSession(username, password, organization, url, root)

    return session, root
}

func init() {

    _URLPostfix = "/" + SDKAPIPrefix + "/v" + strings.Replace(fmt.Sprintf("%.1f", SDKAPIVersion), ".", "_", 100)
}