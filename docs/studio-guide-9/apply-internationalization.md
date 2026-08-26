# Internationalize the App UI using Locales Properties

<https://documentation.neutrinos.com/articles/#!studio-guide-9/apply-internationalization>

The UI of an application is designed for a particular language. This is called the default language, and it is in this language that the application is executed by default. You may want to have your application translated and executed in other languages, making it a multilingual application with a multilingual UI.
Use the **Locales** editor to extend multi-lingual support for your application. Neutrino Studio has an in-built translator that supports these ISO language codes - [Language codes](https://www.labnol.org/code/19899-google-translate-languages#google-translate-languages).
Accessing the Locales Editor
To access the locales editor, on the [side menu](/smart/project-concepts/studio-application-page/a/h3__348108846) of your application, click the **Locales** icon.


 On this editor, you can set the locale-specific information by using the **K****ey**, **V****alue**, and **L****anguage** fields. Perform the following steps to translate a keyword to any language:

 Enter the keyword that is to be translated in the **value** field, along with the **key** that can be used to remember the keyword.
 Select the language(s) to which the keyword is to be translated from the **Add Language** drop-down list.
 Click the **Add **button.

 The Neutrinos Studio translator will convert the keyword to the language of your choice and displays it in the editor.



 ![Information](/resources/Storage/studio-guide-9/info.png)
 Some languages are case-sensitive. Therefore, while converting a keyword to a language of your preference, make sure you use the right casing.



 Note that if you choose this feature, you have to set a default language for the app. All the keys in the end app will be, by default, displayed in the language that you set in this editor.
 The default language of the end app is set to English ('**en**'). To change the default language, select the radio button next to the language.
 ![default language](/resources/Storage/studio-guide-9/default_lang.png)

Locales Groups Locales group allows you to group together multiple locales keywords and bind them to the pages to render a multilingual UI.Follow the steps mentioned below to group keys in the Locales Editor**Step 1: Define the key and languages on the Locales editor**Open** Locales** Editor.Add three keys as India, England, China and add the corresponding values as India, Australia, and China. Click the **Add** button to add them to the editor. From the **Add Language** drop-down, select **English**, **Hindi **and **Chinese (simplified)** as languages. ![](/resources/Storage/studio-guide-9/apply-internationalization-2021-11-24-9.png)**Step 2: Add the keys to a Group**Select the keys by checking the boxes adjoining the key name. To add the selected keys to a group, click **Group**. Enter  Add key: Countries. To create the group, click **Group**.![](/resources/Storage/studio-guide-9/apply-internationalization-2021-11-23-1.png) 3. Locales group **Countries **will be created with the selected keys.

![](/resources/Storage/studio-guide-9/get-started-2021-11-26.png)

Delete Keys from a groupYou can delete a key/multiple keys from a Locales Group.**Steps**Open** Locales Editor.**Expand the group where the key you wish to delete is stored. Click on the adjoining ![](/resources/Storage/studio-guide-9/apply-internationalization-2021-11-24-12.png) icon to delete a key.![Warning](/resources/Storage/studio-guide-9/warning.png)If all the keys under a group is deleted. The group will be deleted.
