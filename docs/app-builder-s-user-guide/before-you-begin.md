# Hardware Requirements

<https://documentation.neutrinos.com/articles/#!app-builder-s-user-guide/before-you-begin>

Before you start creating your app in Neutrinos Studio, make sure you meet the following requirements:

### 

## Hardware Requirements

### 

- 8GB RAM or above
- Dual-Core Processor or above
- 200 GB Hard disk space or above

### Operating System Requirements

- Ubuntu (v.16.04 or above)
- Windows 10
- macOS High Sierra

---

## Software Requirements

**Install the supported versions of the following software. **

### Node.Js

Required for installing dependencies for Neutrinos Studio and additional software. NPM is bundled with Nodejs.

#### Supported Versions: 10.13.0 to 12.X.X

**Installation**

- For windows, download node.js [here](https://nodejs.org/en/#home-downloadhead).
- For mac, download node.js [here](https://nodejs.org/en/#home-downloadhead).
- For Linux, download node.js here.

Refer [node.js documentation](https://nodejs.org/en/download/package-manager/#macos) to learn more!

### 2. Angular CLI

| ![Information](/resources/Storage/app-builder-s-user-guide/info.png) | Starting from Neutrinos Studio 7.6.0, Angular CLI is not a prerequisite to run the front-end. |
| --- | --- |

Required for running the designed app locally.

**Supported Versions: 9.X.X**

**Installation**

Angular CLI is a command-based interface tool used to initialize**, **develop, scaffold, and maintain Angular applications.

Refer to the [Angular documentation](https://cli.angular.io/) to learn more.

### 3. Cordova

Required for generating hybrid mobile apps locally.

**Supported versions: 10.x.x**

**Installation**

- Use npm install -g cordova@10.x.x  command in the terminal of the Neutrinos Studio to install Cordova.
- Refer to the [Cordova documentation](https://cordova.apache.org/#getstarted) to learn more.

### 4. Android Studio

Required for generating and emulating android specific hybrid applications locally.

**Supported versions: 3.1.x or later **

**Installation**

- Download Android Studio from [here](https://developer.android.com/studio#downloads).
- Refer to the [Android Studio](https://developer.android.com/studio/install) Documentation to learn more.

### 5. Java

Required to run Andriod builds.

**Supported versions: 1.8 **

**Installation**

- Download Java from [here](https://www.oracle.com/java/technologies/javase/javase-jdk8-downloads.html).

### 6. Gradle

Required to run Andriod builds.

**Supported versions: 6.1 or later **

**Installation**

Download Gradel from [here](https://gradle.org/releases/). Select the version supported and click the **binary-only** link to download Gradle.

### 7. Git

Required for collaboration

**Supported versions: 2.17.x or later **

**Installation **

Download git from [here](https://git-scm.com/downloads).

Refer [Git Documentation](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) to learn how to install.

---

### 

If you want to run the Neutrinos Studio in a corporate proxy, make sure you:

### Setup Proxy Server

See [Setup Proxy on Neutrinos Studio](/articles/app-builder-s-user-guide/setup-proxy-on-neutrinos-studio) to learn more.

### Allow Access on Firewall

If you want to run the designed app on the local machine, provide access to the following URLs:

- [https://console.neutrinos.co/](https://console.neutrinos.co/): This site is used to build and deploy your apps.
- [https://store.neutrinos.co/](https://store.neutrinos.co/): This is the Marketplace of Neutrinos. You can download existing plugins such as templates, components, and themes from this site and reuse them in your apps.
- [https://ids.neutrinos.co/](https://ids.neutrinos.co/): This is the Neutrinos Identity Server (IDS) which provides user authentication and single sign-on (SSO) functionality by maintaining all user’s information.

![Information](/resources/Storage/app-builder-s-user-guide/info.png)


 If Neutrinos Studio is open and if you are adding new software to the path variable, then make sure you restart Neutrinos Studio.
