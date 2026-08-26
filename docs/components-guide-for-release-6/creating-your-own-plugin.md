# Before you Create a Plugin

<https://documentation.neutrinos.com/articles/#!components-guide-for-release-6/creating-your-own-plugin>

## Before you Create a Plugin

Before you start building a plugin, consider asking yourself the following questions:

- Are there existing plugins that I can reuse instead of creating a plugin?
- What do I want from your plugin?
- What options will my plugin have?
- What are the most important use cases, and how will my plugin help solve these use-cases?
- If my plugin will have UI elements, How should my plugin appear on Neutrinos Studio?

Answering these questions will help you gain clarity on the functionality of the plugin and how the plugin should look when downloaded by other users.

**Names and Descriptions**

Once your plugin is uploaded to Neutrinos Store, names and descriptions help users understand what is the goal of your plugin and how to use it. Names should be clear and clarify the functionality of the plugin. Therefore, make sure you give a clear name for your plugin and enter a proper description that describes the purpose of the plugin.

**Keep in mind these naming conventions:**

- Provide meaningful names for your plugin and for the attributes of the plugin. For example, use "Rich Text Editor", instead of "RTE").
- Use PascalCase (for example, use "FirebaseNotification", instead of "Firebasenotification").
- Use event names that start with "On" (for example, "OnSubmit", instead of "Submit").

### Concepts

Familiarize yourself with the following:

- Neutrinos Store
- bhive-toolkits package

**What is Neutrinos Store?**

[Neutrinos Store](https://store.neutrinos.co/web/catalog/featured) is the marketplace of Neutrinos. It is the center of all pre-built plugins that are created by in-house developers and other Neutrinos end users. It empowers you with reusable and standardized plugins that you can download and use in Neutrinos Studio to rapidly deliver new digital experiences.

You can contribute to the Neutrinos Store by developing new plugins that can be consumed by other end users, and further enrich the assets of Neutrinos Store.

**What is a bhive-toolkits Package?**

**@jathworx/bhive-toolkits** is an npm package that contains various classes to make a complete palette component for Neutrinos Studio. The **core** folder within this package contains the definition of the following classes. To create a component, you should inherit these classes and extend their functionality.

- **Component:** The **Component.js** class contains the definition of all the palette components.
- **Attribute: **The **Attributes.js** class contains the definition of all the attributes and configuration to be displayed when you click a palette component.
- **AdvancedComponent:** The **AdvancedComponent.js** file contains the definition of complex palette components.
- **View:** The **View.js **file contains the definition of views as a page template.
