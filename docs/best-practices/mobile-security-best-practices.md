# Mobile Security Best Practices

<https://documentation.neutrinos.com/articles/#!best-practices/mobile-security-best-practices>

# Mobile Security Best Practices

---

Follow these general best practices for securing your mobile apps:

![Mobile security](/resources/Storage/best-practices/mob_security.jpg)

- [Cordova best practices for mobile security](https://cordova.apache.org/docs/en/latest/guide/appdev/security/)
- [Platform Security using PhoneGap](https://github.com/phonegap/phonegap/wiki/Platform-Security)

Other Best PracticesWKWebViewWKWebView provides better performance and security when compared to UIWebView. If you consider using WKWebView in your iOS app, make sure you install the following plugins:[Cordova WKWebView Engine](https://www.npmjs.com/package/cordova-plugin-wkwebview-engine)[cordova-plugin-wkwebviewxhrfix](https://github.com/TheMattRay/cordova-plugin-wkwebviewxhrfix)[cordova-plugin-wkwebview-file-xhr](https://www.npmjs.com/package/cordova-plugin-wkwebview-file-xhr) Also, since WebSQL has been removed from WKWebView, consider using either local storage or a custom driver on local forage. Navigate to [Git Hub](https://github.com/localForage/localForage/wiki/Custom-Drivers) to see the available custom drivers. Screen PrivacyBoth iOS and Android have app switchers that display a screenshot of your app. This is a great feature for most apps, but if your app displays sensitive information this is a possible privacy risk.
The cordova-privacyscreen-plugin plugin flags your app so that it doesn't show your user's sensitive data in the task switcher. It sets the FLAG_SECURE flag in Android (which also prevents manual screenshots from being taken) and hides the window in iOS.On iOS, this plugin will try to show your splash screen in the app switcher. It will search for splash screens prefixed by Default or the value of the key UILaunchImageFile in your .plist file. If it fails to find a splash screen for a specific device or orientation (portrait or landscape), a black screen is shown instead.See the [Cordova documentation](https://www.npmjs.com/package/cordova-privacyscreen-plugin) for more details.Detect Jailbroken or Rooted DeviceRooting a device means the user can load software that can actively prevent root/jailbreak detection. This adds an extra layer of security for your app. If you want to detect if a device was rooted (Android) or jailbreaked (iOS), use the [cordova-plugin-iroot](https://www.npmjs.com/package/cordova-plugin-iroot) plugin in your app.Detect a DebuggerAttackers attach a debugger to the app to gain access to the internal workings of the app, even when the app is in release mode. The cordova-plugin-check-debugger plugin can be used to check if an unauthorized debugging of the app is in progress. See the [Cordova documentation](https://www.npmjs.com/package/cordova-plugin-check-debugger) for more details.
