# Get IDS Client Instance

<https://documentation.neutrinos.com/articles/#!server-services-designer-8/ids-utility-sequence>

The **idsutil **service contains reusable flows that are used by the **ids **service. It contains the following flows:

### Get IDS Client Instance

This flow gets the IDS client instance. The client instance exposes various methods such as login, logout, etc. to the ids service.

### Get Authorization Scopes

This flow returns the scopes values to the IDS service. Scopes define what information the Server Services wants IDS to return. It include:

- openid
- profile
- email
- address
- phone
- offline_access
- user

### Handle Token Expiry

This flow is used to handle the token expiry. It uses the refresh token to create a new set of token when the access token is invalid.
