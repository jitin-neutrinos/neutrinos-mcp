# Binding the locales property to a component

<https://documentation.neutrinos.com/articles/#!studio-guide-9/translate-the-app-ui-to-multiple-languages>

You can access properties defined on the Locales editor on the Page UI by:

- **Method 1: **Binding it directly to a component's attribute. This is a preferred method if you do not want to run any logic on the properties.
- **Method 2: **Creating a page flow to bind the locale properties to page or flow variables and then binding that page flow to a component. prefer using this method if you want to run some logic on the locale properties before displaying them on the UI.

### Binding the locales property to a component

When you create a page on Neutrinos Studio, along with the page variable, a namespace called page.locales is also gets created. This namespace can be used to access the keys and languages that you have added to the **Locales **editor, and bind them to the page UI by either interpolating the key path in a component or binding the locales group keys with the page flow. To access a key, use page.locales.keys.<key_name>, and to get the current language code, use page.locales.language Also, to set another language, you can assign a valid language code to page.locales.language = '<LanguageCode>'.

See [Properties in Page Designer](/smart/project-page-services-designer-guide/properties-page-designer) to learn about the page properties in more detail.

Example


 Let us look at an example of how to convert a keyword to multiple languages, and bind it to the page UI.


 **Step 1: Define the key and languages on the Locales editor**

Open the **Locales **Editor.


 Add **company** as the **key** and **Neutrinos** as the **value** that is to be translated. Click the **Add** button to add them to the editor.


 From the **Add Language** drop-down, select **Africaans**, **Kannada**, and **Chinese (simplified)** as languages.


 Click the **Add **button to add the languages to the editor. Any key and value you add to this editor will get translated to these languages.


 ![](/resources/Storage/studio-guide-9/translate-the-app-ui-to-multiple-languages-2021-11-25-3.png)

**Step 2: Bind the keyword defined on the Locales editor to the Page UI**



  On the HTML editor of the page, drag and drop a **Toolbar** component to a page. Bind the key that you added on the **Locales** editor to this toolbar by entering {{page.locales.keys.company}} (here, As we are interpolating the key path in a component, we are incorporating curly parentheses.) in the content property of the toolbar.
 Note that you can copy the path of any key directly by using the ![](/resources/Storage/studio-guide-9/apply-internationalization-2021-11-24.png) icon next to the respective key.
 ![toolbar properties](/resources/Storage/studio-guide-9/toolbar_content.png)




 Drag and drop a **Row **component below the toolbar.


 Add two buttons inside the row.


 Set the following attributes on **button 1**.


 button name: **Switch to English**


 (click): Click the **edit** icon next to the field and enter page.locales.language = 'en'. Here, we are setting one of the languages from the **Locales** editor to the page UI asking the page to show the key on the toolbar in English.




 Set the following attributes on Button 2:


 button name: **Switch to Afrikaans**


 (click): Click the **edit** icon and enter page.locales.language = 'af'. On click of this button, the page will show the key on the toolbar in Africaans.





 On deployment, this is how the page looks:

 ![switch the key to Africaans](/resources/Storage/studio-guide-9/africaans.png)![Switch to English](/resources/Storage/studio-guide-9/english.png)


 Accessing the locales property from a page flow


 In the above example, you mapped the locales property directly to a component's property. Alternatively, you can design page flows on the [flow designer](/smart/project-concepts/page-designer/a/h3_520216706), and then bind that flow to a component's property. Let us extend the above example to create a page flow that toggles the keyword between two languages.


 Example




 Navigate to the flow designer of the page.


 Drag and drop a **Start** node to the flow designer. Name the node as **switch bn kan and chinese**.


 Add a Script node to the flow and name it as **check language**.


 Select the property as page.locales.language


 Set the conditions as displayed on the screenshot.

 ![switch case](/resources/Storage/studio-guide-9/switch_lang.png)






 Add a page variable node to the flow and map the first condition of the switch node to this node.

 ![mapping the first condition of the switch node](/resources/Storage/studio-guide-9/switch_flow.png)




 Set the following page variables node properties:


 Name: **Switch to kannada**


 Operation Type: **Set page variables**


 Under **page variables list**, enter the page variable as locales.language, select the type as string, and enter the value as kn.


 Save the node.




 Add another page variable node to the other condition of the Switch node.


 Set the following properties:


 Name: **Switch to kannada**


 Operation Type: **Set page variables**


 Under **page variables list**, enter the page variable as locales.language, select the type as string, and enter the value as kn.




 Save the flow.


 On the Page UI, add a button to switch the languages at the click of the button. Drag and drop a button and set the following properties:


 button name: Switch between Kannada & Chinese

 (click): Select the Flow Picker icon and select the flow on the page designer.

 ![Flow picker](/resources/Storage/studio-guide-9/flow_picker_lang.png)






 Initialize and preview the app.


 On click of the button, the keyword switches between languages - Kannada and Chinese.


 ![keyword in kannada](/resources/Storage/studio-guide-9/kannada.png)![keyword in Chinese](/resources/Storage/studio-guide-9/chinese.png)

### Binding the locales group property to a component

**Example**

Let us look at an example of how to bind Locales group with a component.

**Step 1: Create a ****Locales Group in the Locales ****Editor**

1. Open** Locales** Editor.
2. Add three keys as India, England, China and add the corresponding values as India, Australia, and China. Click the **Add** button to add them to the editor.
3. From the **Add Language** drop-down, select **English**, **Hindi **and **Chinese (simplified)** as languages.

![](/resources/Storage/studio-guide-9/apply-internationalization-2021-11-24-9.png)

**To add the keys to a group,**

1. Select the keys by checking the boxes adjoining the key name. To add the selected keys to a group, click **Group**.
2. Enter Add Key: Countries. To create the group, click **Group****.**

3. Locales group will be created with the selected keys.

**Step 3: ****Bind the keyword defined on the Locales editor to the Page UI **

1. Open the Locales Editor. click ![](/resources/Storage/studio-guide-9/apply-internationalization-2021-11-24.png) icon next to the **India** under the **Countries **to copy the path of the key.
2. On the HTML editor of the page, drag and drop a **Toolbar** component to a page. Bind the key ** India** that you added on the **Locales** **Group** to this toolbar by entering the copied path {{page.locales.keys.countries.india}} in the content property of the toolbar.

![](/resources/Storage/studio-guide-9/apply-internationalization-2021-11-24-11.png)

3. Similarly copy the path of the locales group **Countries**.

4. drag and drop a Select component. Bind the Locales Group path to the select element by entering page.locales.keys.Countries | keyvalue (here, "page.locales.keys.Countries" is the path of key **Countries**) in the datasource property of the select component.

5. Set the following properties:

1. **optionValue**: option.value
2. **optionView:** {{option.value}}.

![](/resources/Storage/studio-guide-9/translate-the-app-ui-to-multiple-languages-2021-11-30.png)

On Deployment this is how the app will look:

![](/resources/Storage/studio-guide-9/apply-internationalization-2021-11-24-6.png) ![](/resources/Storage/studio-guide-9/apply-internationalization-2021-11-24-8.png)

### Accessing the locales Group property from a page flow

In the above example, you mapped the locales group property directly to a component's property. Alternatively, you can design page flows on the [flow designer](/smart/project-concepts/page-designer/a/h3_520216706), and then bind that flow to a component's property. Let us look at example given below to create a page flow that uses all the keys from a group using the locales group path.

**Example**

**Step 1: Create two ****Locales Groups in the Locales ****Editor**

1. Open** Locales** Editor.
2. Add four keys as age, height, agebetween1, agebetween2 and add the corresponding values as Age, Height, Between 25-40 and Between 40-65. Click the **Add** button to add them to the editor.
3. From the **Add Language** drop-down, select **English**, **Hindi **and **Chinese (simplified)** as languages.
4. Select the Keys age and height by checking the boxes adjoining the key name. Select group and Enter Add Key: Eligibilty. To create the group, click **Group.**
5. Similarly select the keys agebetween1, agebetween2. Select group and Enter Add Key: ageGroup. To create the group, click **Group.**

**Step2: Bind the Locales Groups property to the page flow**

1. Navigate to the flow designer of the page.
2. Drag and drop a **Variable** to the flow designer. Open the **Variable Properties** and add two variables as **eligibility** and** ageGroup. **Click** ![](/resources/Storage/studio-guide-9/apply-internationalization-2021-11-26-6.png) **to save**. **

![](/resources/Storage/studio-guide-9/apply-internationalization-2021-11-26-1.png)

3. Add two **Script** node to the page flow. Open the **Script Properties**, add the following scripts in the in the script box.

- page.eligibility= Object.values(page.locales.keys.Eligibility);
- page.ageGroup= Object.values(page.locales.keys.ageGroup);

Note that the page.locales.keys.Eligibility and page.locales.keys.ageGroup  are the locales group key path for the group **Eligibility** and **ageGroup** respectively.

4. Click ![](/resources/Storage/studio-guide-9/apply-internationalization-2021-11-26-6.png) to save.

![](/resources/Storage/studio-guide-9/translate-the-app-ui-to-multiple-languages-2021-11-25-2.png)

![](/resources/Storage/studio-guide-9/apply-internationalization-2021-11-26-2.png)

4. Go to the Page UI, Drag and drop a Column component.

- To display the components defined under the Column in the center of the App page, set** Perpendicular Direction: ****Center **(you can also select the other options, for example. Start, End etc.)

![](/resources/Storage/studio-guide-9/translate-the-app-ui-to-multiple-languages-2021-11-30-3.png)

5. Drag and drop two **Select **components inside the column component.

6. Set the following attributes on the first** Select **component**:**

- placeholder: enter **Eligibility Criteria**
- datasource: enter **page.Eligibility. **Here we are binding the page variable to the component.
- optionValue:enter **option**
- optionView**:** enter **{{option}}**

![](/resources/Storage/studio-guide-9/apply-internationalization-2021-11-26-4.png)

7. Set the following attributes on **the Second Select component**

- placeholder: enter **Age Group**
- datasource: enter **page.ageGroup. **Here we are binding the page variable to the component.
- optionValue:enter **option**
- optionView**:** enter **{{option}}**

![](/resources/Storage/studio-guide-9/apply-internationalization-2021-11-26-5.png)

8. Drag and drop a HTML 5 component to the page UI.

![](/resources/Storage/studio-guide-9/translate-the-app-ui-to-multiple-languages-2021-11-30-4.png)

9. Click **Save.**

On Deployment this is how the app will look:

| ![Information](/resources/Storage/studio-guide-9/info.png) | If you are migrating an app from lower versions to 8.X.X, refer [Locales properties](/articles/studio-guide-7/apply-internationalization) to learn how to access the locale variable in the TS (deprecated) file. |
| --- | --- |

{"mode":"full","isActive":false}
