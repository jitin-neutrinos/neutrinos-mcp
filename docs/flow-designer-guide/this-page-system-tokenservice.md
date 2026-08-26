# this.page.system.tokenService

<https://documentation.neutrinos.com/articles/#!flow-designer-guide/this-page-system-tokenservice>

| ![Information](/resources/Storage/flow-designer-guide/info.png) | Token service is disabled starting from Studio version 8. |
| --- | --- |

bh.system.tokenService provides methods for authentication token management on the application frontend.

**Methods:**[updateTokens()](/smart/project-service-designer-user-s-guide/system-tokenservice/a/updateTokens)[isTokenExpired()](/smart/project-service-designer-user-s-guide/system-tokenservice/a/isTokenExpired)[decodeToken()](/smart/project-service-designer-user-s-guide/system-tokenservice/a/decodeToken)[updateSessionStorage()](/smart/project-service-designer-user-s-guide/system-tokenservice/a/updateSessionStorage)**Variable:**SessionStorage:This variable stores data on a temporary basis, for a single-window (or tab). The data disappears when the session ends i.e. when the user closes that window (or tab).**Syntax:**Copy CodeJavaScripttokenservice.SessionStorage → any;
updateTokens(tokensObj: any, isRemember?: Boolean)This method updates the user token into the device storage.PropertiesDescriptiontokensobjan object which contains the refresh token and access token propertiesisremember?A Boolean value which indicates if the logged-in user should be remembered across tabs.**Return type: **void**Syntax:**Copy CodeJavaScriptupdateTokens(tokensObj: any, isRemember?: Boolean) → {}
isTokenExpired(token: string, offsetSeconds?: number)This method checks if the token expiration based on the token and offsetseconds value.PropertiesDescriptiontoken is a JSON Web Token(JWT) that represents a set of information between two parties. It is composed of a header, a payload, and a signature. offsetSeconds?Optional. The number of extra seconds added to the token expiration time to consider its validity. **Return type: **Boolean**Syntax:**Copy CodeJavaScriptisTokenExpired(token: string, offsetSeconds?: number) → {boolean}**Returns:**Returns true if the token has expired. updateSessionStorage()
This method takes token information from local storage and updates the session storage.**Return type:** void**Syntax:**Copy CodeJavaScriptupdateSessionStorage() → {}
decodeToken(token: string)This method decodes the token and returns the decoded token.PropertiesDescriptiontoken is a JSON Web Token(JWT) that represents a set of information between two parties. It is composed of a header, a payload, and a signature. **Return type: **Any**Syntax:**Copy CodeJavaScriptdecodeToken(token: string) → {any}**Returns:**Returns the decoded token.
