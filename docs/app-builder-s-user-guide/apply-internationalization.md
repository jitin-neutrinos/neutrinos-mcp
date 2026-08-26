# Translate the App UI

<https://documentation.neutrinos.com/articles/#!app-builder-s-user-guide/apply-internationalization>

Add multi-lingual support for your application by using the **Locales** Editor. Access the **Locales** editor from the side pane.

![locales editor](/resources/Storage/app-builder-s-user-guide/locales.png)

 Set the locale-specific information by using keys and languages. Enter a **value** to be translated, along with the **key** that can be used to remember the value. Next, select the language in which the value is to be translated and click the **Add **button.


 The Neutrino Studio translator will convert the keyword to the language of your choice and displays it on the screen.





 ![Information](/resources/Storage/app-builder-s-user-guide/info.png)


 Some languages are case-sensitive. Therefore, while converting a keyword to a language of your preference, make sure you use the right casing.





 Note that if you choose this feature, you have to set a default language for the app. All the keys in the end app will be, by default, displayed in the language that you set in this editor.


 The default locale of the end app is '**en**' (English). To change the locale, you can use localesService.getLocalesInstance().language = '<preferred_language_code>'  and replace <preferred_language_code> with the language code of your preference.





 ![Information](/resources/Storage/app-builder-s-user-guide/info.png)


 See [Language codes](https://www.labnol.org/code/19899-google-translate-languages#google-translate-languages) to view ISO language codes that are supported by our translator.





 ExampleIn this example, you will toggle a button name between the two languages.

 **Step 1: Adding a locale-specific key**




 To add a locale-specific key to your app, perform the following steps:



 In the **Add Key** field, add a key that is to be associated with the value that you want to translate.


 In the **Add Value** field, add the value that is to be translated to a different language, other than English, and click the **+Add** button.
 ![Key and value in the Locales editor](/resources/Storage/app-builder-s-user-guide/i18n_key.png)



 Click the **Add language** drop-down list and select the languages to which the word has to be translated. Click the **+Add** button. You will see the translated text under the languages that you selected.
 ![The languages drop-down list](/resources/Storage/app-builder-s-user-guide/i18n_lang_selected.png)



 Select the default language, other than English to which all your keys should be translated, by default, by selecting the radio button next to the language.
 ![Default language selection](/resources/Storage/app-builder-s-user-guide/i18_def_lang.png)




 **Step 2: Bind the key to a component**

 Navigate to the HTML editor of the page and bind the key to a page component's display name. For example, if you want the button name to be displayed in the default app language that you selected in the **Locales** editor, then double-click the button to open its attributes window and enter {{locales.company}}  in the** button name** field.
 ![Attributes window of a button](/resources/Storage/app-builder-s-user-guide/btn_setting.png)

 On deployment, the button name looks like this:

 ![Translated button](/resources/Storage/app-builder-s-user-guide/translated_btn.png)

 You can bind the translated language to a component in multiple ways. For example, If you want to toggle the button name between two languages, you can:



 Add a **Toggle **button to the page


 Define a class named **toggle()** to be triggered on click of the **Toggle** button
 ![Toggle button setting](/resources/Storage/app-builder-s-user-guide/toggle_setting.png)


 Import localesService service to the page. Copy CodeJavaScriptimport { localesService } from '../../../../baseClasses/localesService';
Add the following code to the TS editor of the page. This code toggles the button name between Arabic and English.



 Copy CodeJavaScripttoggle() {
 if (localesService.getLocalesInstance().defaultLcid !== 'en') {
 localesService.getLocalesInstance().language = 'en';
 } else {
 localesService.getLocalesInstance().language = 'ar';
 }
}




 On deployment, the button name can be toggled between the two languages.

 ![Toggle between two languages](/resources/Storage/app-builder-s-user-guide/toggle_1.png)
