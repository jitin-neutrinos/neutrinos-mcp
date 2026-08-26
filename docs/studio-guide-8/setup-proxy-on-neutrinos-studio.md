# Setup Proxy on Neutrinos Studio

<https://documentation.neutrinos.com/articles/#!studio-guide-8/setup-proxy-on-neutrinos-studio>

| ![Information](/resources/Storage/studio-guide-8/info.png) | If you are running the configured Neutrinos Studio environment behind the proxy server, then perform the steps that are mentioned on this page. |
| --- | --- |

You can configure Neutrinos Studio to use a proxy server to communicate with Neutrinos hosted services such as IDS, Store & Console. To do so, perform the following steps:

1. Launch Neutrinos Studio and wait for the Network error prompt.
2. Edit the **settings.json** file located in the **.neutrinos** folder in the user $HOME directory of your operating system.
  1. Windows - C:\Users\<UserName>\.neutrinos\settings.json
  2. Linux - /home/<UserName>/.neutrinos/settings.json
  3. Mac - /Users/<UserName>/.neutrinos/settings.json
3. Configure the proxyAgent with following options at root level of settings JSON object:
  1. **proxy [mandatory]** - String proxy url http://host:port. If proxy requires basic authentication, you can configure it in the proxy url http://username:password@host:port
  2. **keepAlive [optional]** - Boolean defaulted to true
  3. **keepAliveMsecs [optional]** - Integer defaulted to 1000
  4. **maxSockets [optional] **- Integer defaulted to 256
  5. **maxFreeSockets [optional]** - Integer defaulted to 256
  6. **scheduling [optional]** - String defaulted to lifo

Example:

```markdown
"proxyAgent": {       "proxy": "http://localhost:80",}
```

OR

```markdown
"proxyAgent": {       "proxy": "http://localhost:80",       "keepAlive": true,       "keepAliveMsecs": 1000,       "maxSockets": 256,       "maxFreeSockets": 256,       "scheduling": "lifo" }
```

**Make sure to save valid JSON structure only.**

1. Configure proxy server for npm. Run the below command.
    npm config set proxy http://host:port
    If the proxy requires basic authentication, you can configure it in the proxy URL.
    npm config set proxy http://username:password@host:port
2. The [Locales](/articles/studio-guide-8/apply-internationalization) editor communicates with Google cloud API using @google-cloud/translate SDK. You can configure your proxy server details in below environment variables:
  - HTTP_PROXY=http://username:password@host:port
  - http_proxy=http://username:password@host:port
  - https_proxy=http://username:password@host:port
  - HTTPS_PROXY=http://username:password@host:port
3. Restart** Neutrinos Studio.**
