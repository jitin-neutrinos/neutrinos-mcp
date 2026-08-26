# Security FAQs

<https://documentation.neutrinos.com/articles/#!development-faqs/security-faqs>

Security FAQs

[Basics](/articles/development-faqs/security-faqs/a/basics)


 [Pen Test for Mobile App](/articles/development-faqs/security-faqs/a/mobile)








 Basics



 [What
 is Penetration Testing?](/articles/development-faqs/security-faqs/a/0)


 Penetration testing is a practice of testing a system to find security vulnerabilities that an attacker could exploit.





 [What are the best tools for pen test for efficient testing?](/articles/development-faqs/security-faqs/a/0)


 Some of the best tools used to perform pen test are Micro Focus, Android Debug Bridge, Mobile Security Framework. See [Mobile APP Security Testing Tools](https://www.softwaretestinghelp.com/mobile-app-security-testing-tools/) to know more about the tools used for efficient pen test results.









 Pen Test for Mobile Applications



 [How to detect mobile Rooting /Jailbreak?](/articles/development-faqs/security-faqs/a/0)


 Use [cordova-plugin-iroot](https://www.npmjs.com/package/cordova-plugin-iroot) to detect Rooting or Jailbreak. If you are using Googles safetynet plugin, then use [cordova-plugin-android-safetynet](https://www.npmjs.com/package/cordova-plugin-android-safetynet)(This links works only on android).





 [How to deal with Lack of Obfuscation?](/articles/development-faqs/security-faqs/a/0)


 Obfuscation is a programming technique in which code is intentionally obscured to prevent reverse engineering and deliver unclear code to anyone other than the programmer.

 To deal with Lack of Obfuscation and make decompiling the code difficult, use [cordova-plugin-proguard.](https://www.npmjs.com/package/cordova-plugin-proguard)





 [How to implement Dynamic Instrumentation Protection?](/articles/development-faqs/security-faqs/a/0)



 Step 1: Use [cordova-plugin-is-debug](https://www.npmjs.com/package/cordova-plugin-is-debug) to check if the application is in the debug mode or release mode.

 Step 2: If the application is in the release mode use, [cordova-plugin-check-debugger](https://www.npmjs.com/package/cordova-plugin-check-debugger) to check if the debugger is attached to the release version of your application or not.

 Step 3: If the debugger is attached to the application, then do something drastic like closing the app or delete the local app data.
.






 [How
 to disable Background Screenshoting?](/articles/development-faqs/security-faqs/a/0)


 You can use [third party plugins](https://stackoverflow.com/questions/44588610/prevent-ios-app-from-keeping-screen-snapshot-using-cordova) to prevent taking screenshot or blur the application UI when it moves to the background when switching between applications.





 [How to enable Certificate Pinning?](/articles/development-faqs/security-faqs/a/0)


 You can use [Cordova Advanced HTTP](https://www.npmjs.com/package/cordova-plugin-advanced-http)or any third party plugins to natively enable Certificate Pinning.

 **NOTE:** Angular HTTP currently does not support Certificate Pinning.






 [How
 to test for an insecure Direct Object Reference?](/articles/development-faqs/security-faqs/a/0)


 Use Globally Unique Identifier(GUIDs) instead of increamenting ID's to reduce Direct Object Reference. GUID is a 128-bit number used to identify information in computer systems.





 [How to enable or disable TLS for iOS?](/articles/development-faqs/security-faqs/a/0)


 You can enable or disable the TLS for iOS by adding the following code in the end of **config** file before the widget closing tag **(/widget)** of the application.




 To enable TLS for iOS





 <config-file target="*-Info.plist"

 parent="NSAppTransportSecurity">

 <dict>

 <key>NSAllowsArbitraryLoads <key>

 <true />

 </dict>

 </config-file>




 To disable TLS for ios





 <config-file target="*-Info.plist"

 parent="NSAppTransportSecurity">

 <dict>

 <key>NSAllowsArbitraryLoads <key>

 <false />

 </dict>

 </config-file>












  [Close](/articles/development-faqs/security-faqs/a/0)
