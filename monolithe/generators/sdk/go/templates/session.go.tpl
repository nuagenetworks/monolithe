{{ header }}

package {{ sdk_name }}

import (
    "github.com/primalmotion/bambou"
    "fmt"
    "strings"
)

var (
    _URLPostfix string
)

func NewSession(username, password, organization, url string) *bambou.Session {

    root := New{{sdk_root_api|capitalize}}()
    url += _URLPostfix

    return bambou.NewSession(username, password, organization, url, root)
}

func init() {

    _URLPostfix = "/" + SDKAPIPrefix + "/v" + strings.Replace(fmt.Sprintf("%.1f", SDKAPIVersion), ".", "_", 100)
}