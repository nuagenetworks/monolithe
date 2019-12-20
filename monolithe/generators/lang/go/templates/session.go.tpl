{{ header }}

package {{ name }}

import (
    "github.com/nuagenetworks/go-bambou/bambou"
    "fmt"
    "strings"
    "crypto/tls"
)

var (
    urlpostfix string
)

// Returns a new Session -- authentication using username + password
func NewSession(username, password, organization, url string) (*bambou.Session, *{{root_api|capitalize}}) {

    root := New{{root_api|capitalize}}()
    url += urlpostfix

    session := bambou.NewSession(username, password, organization, url, root)

    return session, root
}

// Returns a new Session -- authentication using X509 certificate.
func NewX509Session(cert *tls.Certificate, url string) (*bambou.Session, *{{root_api|capitalize}}) {

    root := New{{root_api|capitalize}}()
    url += urlpostfix

    session := bambou.NewX509Session(cert, url, root)

    return session, root
}

func init() {

    urlpostfix = "/" + SDKAPIPrefix + "/v" + strings.Replace(fmt.Sprintf("%.1v", SDKAPIVersion), ".", "_", 100)
}
