# Add Language

<https://documentation.neutrinos.com/articles/#!pulse-publication/language-editor-wf-cm>

Language translation is essential for making applications accessible to a global audience. In Workflow Studio, developers can add multiple languages for a project. In the Language Editor, Workflow Studio allows you to define keys that will be dynamically replaced at runtime based on the language selected by the user.

We support both Left-to-Right (LTR) and Right-to-Left (RTL) languages. This language configuration affects the entire layout of the project view in the Workbench

## Add Language

To add language for application through Workflow Studio, follow the steps below:

1. In Config editor, navigate to **Language** editor.
2. In the Language editor, click the **Add Language** button > Enter the details below in the **Add Language** pop up screen.
    **Field**
    **Description**
    Language Name
    Accepts the name of the language.
    Language Key
    Accepts a acronym for the language. For example, if the language is Arabic, the key is Ar.
    Direction
    Choose the language orientation. For example, Arabic uses **RTL (right-to-left)**, while English follows **LTR (left-to-right).**
3. Once a language is added, the required display text values must be added for translation. Some terms are pre-listed by default. If a pre-listed term does not have a translated value, its key value will be used instead. You can also define custom keys and provide corresponding text in both the default language (English) and the translated language.
  1. To add custom keys values scroll to the bottom of the page, click **Add Key **button.
  2. Enter the Key, display text to be used in both default language and the translated language.
4. Click the **Save** button.

The GIF below demonstrates how to add a new language and define a key with its translated values in Workflow Studio .

![language-add-gif](/resources/Storage/pulse-publication/images/workflow-studio-config-language-add-gif.gif)

| ![Note](/resources/Storage/pulse-publication/project-trailproject/note.png) | If a language has an RTL (Right-to-Left) orientation, the entire application layout adapts accordingly. This means the application switches to an RTL layout to match the language. |
| --- | --- |

## Change Language

The content of form or layout components can be translated into the newly added language. For example, button labels can be translated. To apply the translated text, follow these steps:

1. Open the page in the application that needs to adapt to the language translation.
2. Select the layout component, then double-click it to open its settings.
3. Navigate to the **Basic Attributes** section.
4. Select the attribute, choose **Language** from the dropdown, and then select the appropriate key from the available list.
    ![orkflow-studio-language-direct](/resources/Storage/pulse-publication/images/workflow-studio-language-1.png)
    Alternatively, you can enter the key value directly into the dropdown using {{lang.keyname}} without changing the value type from **String** to **Language** in the first dropdown.
    ![workflow-studio-language-using-{{}}](/resources/Storage/pulse-publication/images/workflow-studio-language-2.png)
5. Click the **Save** button.

In the Workbench, change the language from the default. Observe how the layout components update their display text based on the selected language. The GIF below demonstrates how to add display text in a different language to a submit button.

![language-add-workbench-gif](/resources/Storage/pulse-publication/images/workflow-studio-config-language-add-workbench-gif.gif)
