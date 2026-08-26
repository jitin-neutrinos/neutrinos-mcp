# Test your Progressive Web App

<https://documentation.neutrinos.com/articles/#!studio-guide-9/test-your-progressive-web-app>

To test a [Progressive Web App](/smart/project-concepts/progressive-web-app) on Neutrinos Studio, you should take a build of the app. In the default terminal of Neutrinos Studio, navigate to the app folder and run the command to create a build:

```markdown
 cd app npm run build-web
```

![pwa build command](/resources/Storage/studio-guide-9/pwa%20build.png)

A dist folder is generated within the app folder. This folder will contain all the build files.

To test the app with a server, you can build a local server or[run any HTTP server](https://www.npmjs.com/package/http-server) in the dist folder. For example, To install and run the HTTP server locally on port 8083, execute the following commands:

```markdown
cd distnpm install --global http-serverhttp-server --port 8083
```

You can then launch the PWA on the given port using the URL [http://localhost:8083](http://localhost:8083/).
