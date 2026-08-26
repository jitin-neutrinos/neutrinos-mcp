# Adding an Environment

<https://documentation.neutrinos.com/articles/#!studio-guide-9/what-is-an-environment>

To manage environment-specific properties and values, access the **Environments** editor within your application. Select **Environments** on the side menu of the [Studio Application page](/smart/project-concepts/studio-application-page).

Environment properties are properties that are used to define the [environment](/smart/project-concepts/environment) the application is running on. These properties can be used to configure:

- The HTTP Port and address which the project is being served through
- The location of static files
- Endpoints of other external services
- storage connection information such as Database name.

Every application can have two types of environment properties:

- The **client-side **environment properties - The properties that can be accessed on the Front-end of the application.
- The **server-side **environment properties- The properties that can be accessed on the back-end server that you create for the app using [Server Services](/smart/project-concepts/server-services-designer).

By default, Neutrinos Studio provides Development **(****Dev)** and Production **(****Prod)** environments with pre-configured properties.You can also add additional environment properties or choose to create a new environment.

- **Development environment:** This is where you configure properties of your development environment.For example, when the application is in development, your server is hosted on localhost 8081.
- **Production environment:** This is where you configure environment properties for the production environment. That is, when you are ready to make your applications available to your end-users. For example, in the production environment, you will replace localhost 8081 with the URL where your server is hosted.

![Environments editor](/resources/Storage/studio-guide-9/Envi7.png)

### Adding an Environment

Apart from Dev and Prod environments, you can also create other non-production environment configurations according to your requirements. These environments' main purpose is to provide a real scenario (similar to Production) where developers can test your applications and mitigate the risk of deploying them to Production while keeping features that can assist developers with debugging. For example, a **UAT** environment to test the production build.

To create an [environment](/smart/project-concepts/environment):

- Click ![the Clone icon](/resources/Storage/studio-guide-9/clone_icon.png) next to the environment that you want to clone.
- Enter a name for the new environment and click **Clone**.
- Click each property value field to update its pre-configured value.

### Adding a Property

See [environment properties](/smart/project-concepts/environment/a/h3_709278163) to learn about the default properties on Neutrinos Studio.

To add a new property to your environment:

- Enter the property name and value for the environment.
- Select the property type. You can select **Client**, **Server,** or both **Client and Server** checkboxes.
- Click the **Add** button. The property gets added to all the environments. Edit the values as required.

You can change the type of property at any time using the **Type** column. Click the field to access the drop-down list and select the environment type.
