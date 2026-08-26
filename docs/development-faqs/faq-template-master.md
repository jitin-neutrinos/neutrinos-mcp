# FAQs

<https://documentation.neutrinos.com/articles/#!development-faqs/faq-template-master>

Development FAQs

Development FAQs

[Basics](/articles/development-faqs/faq-template-master/a/basics)
 [Platform](/articles/development-faqs/faq-template-master/a/mobile)
 [Mobile](/articles/development-faqs/faq-template-master/a/account)





 Basics

  [What
 is Neutrinos Platform?](/articles/development-faqs/faq-template-master/a/0)

 To learn about Neutrinos platform and what it constitutes of,
 see [here.](/articles/sample-how-to-guide/learn-about-neutrinos-platform)


  [How
 do I sign up to Neutrinos Platform?](/articles/development-faqs/faq-template-master/a/0)

 If you are a new user and want to sign-up for a free trial,
 navigate to the [https://www.neutrinos.co/](https://www.neutrinos.co/)
 and click the **Free Trial** option on the top navigation. In the free trial
 form, enter the required details and click **Submit**.


  [What
 are the free trial terms?](/articles/development-faqs/faq-template-master/a/0)

 For free trial terms, see [here.](/articles/app-builder-s-user-guide/free-trial-terms)


  [How
 do I perform user management?](/articles/development-faqs/faq-template-master/a/0)

 To perform user management for your organization, see [here.](/articles/app-builder-s-user-guide/perform-user-management)


  [I
 forgot my Neutrinos account password?](/articles/development-faqs/faq-template-master/a/0)

 Ask your ORG_ADMIN
 to login to [Neutrinos Console](https://console.neutrinos.co/web/users) and reset your password.






 Platform

  [How
 can I upgrade to a new version of Neutrinos Studio?](/articles/development-faqs/faq-template-master/a/0)

 Neutrinos provides** Over-the-air** updates for
 Windows and Mac Operating systems.
 If you are using Ubuntu,
 navigate to [Neutrinos
 Console.](https://console.neutrinos.co/web/) and manually update your Studio version.


  [If
 I upgrade to the latest version, what happens to the apps created
 in the old version?](/articles/development-faqs/faq-template-master/a/0)

 The apps in the previous versions of Neutrinos Studio will
 remain in the user workspace. If there is any impact to an app,
 the auto-migration option will take care of it. Or, Neutrinos
 Studio will prompt you to perform a few manual steps mentioned
 in the [Migration guide](/articles/neutrinos-studio-migration-guide/get-started).After performing the manual steps mentioned in the migration guide, if you face any issues, write to support@neutrinos.co for assistance.


  [Can
 I create native apps?](/articles/development-faqs/faq-template-master/a/0)

 Neutrinos Studio creates hybrid apps. That said, the [Neutrinos Store](https://store.neutrinos.co/web/catalog/featured) hosts a variety of native
 widgets that are compatible with studio as well. This gives you access
 to native phone features.


  [How
 do I push data to a database?](/articles/development-faqs/faq-template-master/a/0)

 You can create Server flows using the Server Services Designer to perform operations
 on databases such as MongoDB, MSSQL, etc. See [Server Services Designer guide](/articles/#!server-side-service-designer-publication/) for more details.


  [Can
 the UI or Front-end code be extracted and changed from outside Neutrinos Studio?](/articles/development-faqs/faq-template-master/a/0)

 Neutrinos Platform provides no lock in. You always have the
 option to modify the code outside the platform. However, this is
 not recommended as you would loose rapidity and also changes
 made outside the platform do not reflect back.



  [How
 do I create application templates?](/articles/development-faqs/faq-template-master/a/0)

 The process is similar to creating an app. Once you create an
 app, you can submit the same to Neutrinos to be uploaded as a
 template on MarketPlace. Or, you save the template in your local file
 system and import it as and when you want to use the template in your app.


  [How
 do I create my own widgets or plugins using Neutrinos Studio?](/articles/development-faqs/faq-template-master/a/0)

 Neutrinos provides a framework to create and publish new widgets/plugins on Neutrinos Store. See [Create a Plugin](/articles/components-guide-for-release-6/release-6-0-2) for more details.



  [How
 do I authenticate and authorize my app users](/articles/development-faqs/faq-template-master/a/0)

 To authenticate and authorize application users, Neutrinos provides its own authorization strategy. Further it also allows you to use other OAuth Providers such as Google, Active Directory, and Azure.
 See [Configure IDS for your app](/articles/app-builder-s-user-guide/configure-your-ids) for more details.


  [How
 are authentication tokens created?](/articles/development-faqs/faq-template-master/a/0)

 Authentication tokens are created by the server flows that get auto-generated after you enable IDS for your application. see [IDS Services](/articles/server-side-service-designer-publication/ids-services) to learn more.


  [What
 are the prerequisites required to run the platform?](/articles/development-faqs/faq-template-master/a/0)

 For prerequisites, see [here.](/articles/#%21project-sample-how-to-guide/before-you-begin)




  [Neutrinos
 Studio is not loading on Windows machine?](/articles/development-faqs/faq-template-master/a/0)

 If you have an antivirus software installed in your Windows
 machine, Neutrinos Studio may not load as **winpty**
 (the package for running Windows console programs) starts to
 break. The resources required to start Neutrinos Studio could be
 blocked during the antivirus scan. Make sure you keep the studio
 workspace in the exclusion list for the studio to load properly.


  [Can
 an existing app be imported to Neutrinos Studio?](/articles/development-faqs/faq-template-master/a/0)

 Currently, only apps built on Neutrinos Studio can be imported. See [Importing an app](/articles/app-builder-s-user-guide/creating-an-app/a/h3__911704037)to learn how.>


  [Can
 Neutrinos platform support bootstrap with Angular instead of
 Angular Material?](/articles/development-faqs/faq-template-master/a/0)

 Although we would not recommend it, yes our platform can
 support Bootstrap over Angular Material.


  [Can
 I differentiate the code from the design?](/articles/development-faqs/faq-template-master/a/0)

 Yes, generated code and design files are saved separately.



  [Can
 I use external components like ITEXT?](/articles/development-faqs/faq-template-master/a/0)

 No, not as a default feature of studio.


  [What
 is the difference between Studio template generator and the
 default CLI template generator?](/articles/development-faqs/faq-template-master/a/0)

 The default CLI generator just generates standard templates for
 pages and routes. Any subsequent edits to these components has
 to be done manually by the developer.



  [Does
 the platform support any testing modules?](/articles/development-faqs/faq-template-master/a/0)

 Yes. With Neutrinos Studio, you can use Karma or Protracted
 test modules.


  [Do
 you have a Devops capability?](/articles/development-faqs/faq-template-master/a/0)

 Yes. We provide Devops capability with Jenkins, GIT hub, and
 Jira.


  [Can
 I manage application states in Neutrinos Studio?](/articles/development-faqs/faq-template-master/a/0)

 Neutrinos Studio allows you to configure PM2 , which is a daemon process manager that helps you in managing and keeping your application online. See [Configure PM2](/articles/app-builder-s-user-guide/configure-pm2) for more details.


  [Why
 is there no support for Internet Explorer on Neutrinos Platform?](/articles/development-faqs/faq-template-master/a/0)

 Here are the reasons for Neutrinos Platform to not support IE:



 **Security Loopholes and threats:** IE has serious browser security flaws
 with the recent one flagged as close to 18th Jan 2020, where the
 vulnerability lets attackers corrupt memory used for the scripting
 engine in IE9, IE10 and IE11 in a way that would let the intruder run
 arbitrary code with the same permissions as the user, letting them
 hijack a PC.




 Legacy by Default approach from Microsoft:IE had major technical debts
 where IE makers chose simplicity over covering the technical debt.

  When newer versions of IE were releases, Microsoft decided not only to
 update the standards but also retain the older interpretation of
 standards just to make sure not to break older applications based on the
 older standards.




 Delayed patches and updates:IE 11 will be supported till Windows 10
 reaches end of life, but that support will be minimal with security
 fixes and bug fixes.




 **Support for IE is phased out:** Microsoft stopped supporting IE older
 versions as explained in the previous paragraphs. Microsoft has
 mentioned that Internet Explorer 11 is the last major version of
 Internet Explorer.



 **Does not support Cross Platform IE based Applications:**IE 11 does not support modern JavaScript standards.
  To have your applications work on IE 11, JavaScript has to be compiled
 to ES5 instead of ES 6 which means the size of your bundle increase by
 30 % and significantly worsens performance.
 Also,it it limits the developer to use the features of the newer JavaScript
 standards such as HTML elements, and new CSS properties.









 Mobile

  [The iOS keyboard closes and opens
 immediately when shifting focus() from one input to another using
 code?](/articles/development-faqs/faq-template-master/a/0)


 Imagine a screen with multiple input fields, where the cursor
 moves from one input box to the next, based on whether or not the
 user entered a text in the previous input box. (For example, in
 the case of OTP). In this screen, the normal logic would be to
 listen for keyboard inputs in the first input box and then use focus()
 to shift focus to the next one. But on doing this in iOS, you
 might face the following issues:



 **Issue 1:** The keyboard does not show up on using focus()
 .



 **Clue: **Add the following code to config.xml
 file:

 <preference
 name="KeyboardDisplayRequiresUserAction" value="false" />



 **Issue 2:** Once issue 1 is handled, the keyboard
 bounces, that is, the keyboard opens and closes multiple times in
 a span of a few seconds.



 **Clue: **Perform the following steps to fix the
 issue:



 1. Add cordova plugin cordova-plugin-keyboard
 to your project.

 2. Use blur()
 to remove focus from the first input field, after the user has
 typed in his first letter. The blur()
 function on removing focus from the element will trigger the keyboardWillHide
 event:



 document.getElementById("input1").blur();



 3. Then, use the keyboardWillHide
 plugin and listen for the iOS only event as shown below:




 window.addEventListener('keyboardWillHide', function () {

 // Set focus onto
 next input box before the keyboard hides.


 document.getElementById("input2").focus();

 });



 4. In the keyboardWillHide
 event listener, set focus onto the second input field. This makes
 sure that the keyboard does not have the time to close.



 **Be careful while writing the logic inside this listener as
 the listener might trigger every time the keyboard is about to
 close.**

  [Push notification using .p8
 authentication does not work the same way as that of Android
 devices?](/articles/development-faqs/faq-template-master/a/0)

 **This issue does not apply if you are using a .p12
 certificates in Firebase.**



 If you are building the app using Xcode, navigate to **File**
 > **Workspace** Settings, and change Build
 System to Legacy Build system. Or, if you are building the app
 using CLI, add the following flag when you run the build:



 npm
 run build-mobile && cordova build ios
 --buildFlag="-UseModernBuildSystem=0"


  [How
 do I disable context menu in an Android device?](/articles/development-faqs/faq-template-master/a/0)

 In an Android device, if you want to disable the context menu
 that appears on long press of a palette component , perform the
 following steps:

 1. Click the palette component on which you want to disable the
 context menu. The component's attributes window opens up for
 you.

 2. Expand **Custom Properties** and select **Key
 & Value**.

 3. Enter (contextmenu)
 in the **property name** field. Enter false
 in the **property value** field to disable the
 context menu.

 4. Click **Add** to add this custom property to
 the component.


  [I
 cannot run the .ipa file directly in a new Apple device?](/articles/development-faqs/faq-template-master/a/0)

 If you have a basic Apple Developer account, and if you want to
 develop or test your .ipa file in a new Apple device, you cannot
 directly install the .ipa file into the device. This is because
 the new device ID is not provisioned in the app profile.



 **Workaround:**



 Perform the following steps to create a **.ipa**
 file for the new Apple device:



 1. Open Xcode and select the config.xml
 file from your app project folder. Make sure that the bundle id
 is correct. The bundle id should be in the format
 co.neutrinos.<app_name>.



 2. Navigate to [https://get.udid.io/](%20https://get.udid.io/) and retrieve your device's UDID.



 3. Login to your Apple Developer account, navigate to the
 Devices section, and add the UDID of the new device.



 4. Click the App IDs section, under Identifiers, create a new
 App ID.



 5. If your app has additional capabilities such as push
 notifications, In the Explicit App ID field, give the name and
 bundle id of the app. If there are no additional capabilities,
 use wildcard app id.



 6. Enable app services for all your capabilities.



 7. Create an iOS development or distribution(for app store)
 provisioning profile using the app Id created in step and
 make sure your device's UDID is included in this profile.

 Download the provisioning profile.



 8. Open the provisioning profile using a code editor of your
 choice. You will see the following lines of code which
 represents the provisioning profile number. This number will be
 used while creating the .ipa
 file.

 <key>UDID</key>


 <string>177XXXf-50db-4849-ac86-0a47axxxxe0a3</string>



 9. These lines of code represents the array of devices that will
 work with this particular provisioning profile. Make sure that
 the UDID of your device is listed here.


 <key>ProvisionedDevices</key>

 <array>


 <string>bdfbe710a917a244xxxa7daf998xx913ae788</string>


 <string>70138e67d2fcc3fcd71a4sxxxxx57xx02e4</string>


 <string>00008020-000XXXXX226DA002E</string>

 </array>



 10. Open a Command Prompt and build you app using the following
 command:


 npm run build-mobile && cordova build ios

 --device

 --codeSignIdentity="iPhone Developer"

 --developmentTeam="AUX825XVW"

 --buildFlag="-allowProvisioningUpdates"

 --buildFlag="-UseModernBuildSystem=0"


 --provisioningProfile="177XXXf-50db-4849-ac86-0a47axxxxe0a3"



 You will receive a .ipa
 file that will work on all the devices that are listed in step
 10.


  [How
 do you support new versions of IOS and Android?](/articles/development-faqs/faq-template-master/a/0)

 An upgrade of the underlying OS may require an upgrade of
 Neutrinos Studio. When Studio is upgraded, the apps in the
 studio may also required to be migrated. The migration utility
 will provide an automatic migration path.


  [How
 do I use native components from Android and IOS?](/articles/development-faqs/faq-template-master/a/0)

 [Neutrinos Store](https://store.neutrinos.co/web/catalog/featured) hosts a variety of native
 widgets that are compatible with Neutrinos Studio. This gives
 you access to a majority of native phone features. You can also
 create your own plugins and host it on the marketplace and reuse
 it across the projects.


  [I cannot publish my iOS app to Apple Store due to unsupported architectures.](/articles/development-faqs/faq-template-master/a/0)

 This is a known issue. See [the solution posted on GitHub](https://github.com/NeutrinosPlatform/cordova-plugin-document-scanner/issues/18#issuecomment-576527918) for a quick fix.






  [Close](/articles/development-faqs/faq-template-master/a/0)
