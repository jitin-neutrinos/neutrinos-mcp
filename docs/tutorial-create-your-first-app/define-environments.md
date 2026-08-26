# Environment Properties

<https://documentation.neutrinos.com/articles/#!tutorial-create-your-first-app/define-environments>

An [environment](/smart/project-concepts/environment) is a system or server where an application is hosted.

To access the Environments editor, click **Environments** in the left pane.

### Environment Properties

For every environment, you need to configure a set of properties. Each environment comes with a set of predefined properties. In addition, you can also add and update properties in the **Environments** editor by using the following options:

- **Add a new property: **Enter the name and value for the property and click the** Add** button.
- **Update an existing property: **Click the property value that you want to update and start typing the new value. For predefined properties, the property name is greyed out and you can only update values. For user-defined properties, you can update both name and value.

### Environment Properties for the app

For the weather app, add these server properties in the Environments editor. Make sure only the server checkbox is selected.

- **apiId**: 6076e953046196d0c851e53173393c0d
- **weatherProviderURL:** http://api.openweathermap.org/data/2.5/weather

![The environments settings for the weather app](/resources/Storage/tutorial-create-your-first-app/env_wea.png)
