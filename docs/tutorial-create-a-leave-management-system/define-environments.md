# Define Environments

<https://documentation.neutrinos.com/articles/#!tutorial-create-a-leave-management-system/define-environments>

An environment is a system or server where an application is hosted. By default, Neutrinos provides with **Dev** and **Prod** environment variable configurations. You can create and maintain environment-specific properties and values for an individual environment which can be accessed within the application.

| ![Information](/resources/Storage/tutorial-create-a-leave-management-system/info.png) | For the LMS app, you will not be creating environments. You will be using the default **Dev** and **Prod **environments that are pre-configured when you created an app. |
| --- | --- |

If you want to edit the default environment settings, perform the following tasks.

**Create an Environment**

To create an environment:

1. Open the Environments editor
2. Click the **Dev** or **Prod **Environment, and click the **Clone **icon.
3. Enter a name for the new environment and click **Clone**.
4. Click each property value field to update its pre-configured value or enter a new property name and value and click **Add** to add the new property across all environments.

![To add a environment](/resources/Storage/tutorial-create-a-leave-management-system/addenviLMS.png)

**Configuring an environment**

For every environment, you need to configure a set of properties. Each environment comes with a set of predefined properties. In addition, you can also add and update properties in the **Environments** editor by using the following options:

- **Add a new property: **Enter the name and value for the property and click the** Add** button.
- **Update an existing property: ** Click the property value that you want to update and start typing the new value. For predefined properties, the property name is greyed out and you can only update values. For user-defined properties, you can update both name and value.

![update environment](/resources/Storage/tutorial-create-a-leave-management-system/updateenviLMS.png)

**Access Configuration**

Regardless of the environment in which the app runs, you can access the configured environment variables by using the [system service getVal(key) method](/articles/service-designer-user-s-guide/system-deviceservice/a/getVal) on the front-end.
