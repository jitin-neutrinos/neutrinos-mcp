# Migration Steps

<https://documentation.neutrinos.com/articles/#!neutrinos-studio-migration-guide/migration-from-8-x-x-to-8-1-0>

### Migration Steps

Make sure you [Migrate the App](/articles/neutrinos-studio-migration-guide/migrate-your-application) to Studio version 8.1.0 and perform the following steps:

**Add Content Security Policy header in IDS flow**

- Open [ids service](/articles/server-side-service-designer-publication/ids-sequence)in the [Server Services Designer](/articles/concepts-publication/server-services-designer).
- To add the Content-Security-Policy header in Login Callback Api,

1. Open Html response to close in app browser node's (HTTP Out) properties.
2. In the header attribute, enter key as Content-Security-Policy and Value as script-src 'sha256-wcX+PzUovy0uNFqMGCbbbzuT5v4aAxU9obFNyt6BHAQ='.

- To add the Content-Security-Policy header in Logout Callback Api,

1. Open Html response to close in app browser node's (Send html Response) properties.
2. In the header attribute, enter key as Content-Security-Policy and value as script 'sha256-j4HHWBMKh2PoLEAu017BWktgUmmL7VVMjnHuNWUHGOg='
