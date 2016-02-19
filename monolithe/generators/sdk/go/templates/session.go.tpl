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

func MakeSession(username, password, organization, url string) *bambou.Session {

    root := New{{sdk_root_api|capitalize}}()

    return &bambou.Session{
        Username:     username,
        Password:     password,
        Organization: organization,
        URL:          url + _URLPostfix,
        RootObject:   root,
    }
}

func init() {

    _URLPostfix = "/" + SDKAPIPrefix + "/v" + strings.Replace(fmt.Sprintf("%.1f", SDKAPIVersion), ".", "_", 100)
}