# Views

<https://documentation.neutrinos.com/articles/#!best-practices-8/reusability-of-plugins>

# 

As developers, we are always interested in making the app development lifecycle easy and more effective. To achieve this, all development frameworks and languages provide some form of **sub-module/sub-component** support to create unit blocks of functional reusability.

Neutrinos Platform also provides ways to create unit blocks of functional reusability by:

1. Using views
2. Using existing plugins from Neutrinos Store
3. Create reusable plugins

### Views

You can create pages and use them on another page. The page inside a page is considered as a view. You can also pass data from the page to the view. A view can also emit events to make the parent page aware of user interactions.

Refer to [Views documentation](/articles/app-builder-s-user-guide/views).

### Store Plugins

Neutrinos Store is the marketplace of Neutrinos where all [plugins](/smart/project-concepts/plugin) (including components, nodes, app templates, and directives) are hosted. Navigate to [Neutrinos Store](https://store.neutrinos.co/web/catalog/featured) to [download and use the existing plugins](/smart/project-sample-how-to-guide/import-plugin) while building your application.

### Create Reusable Plugins

You can create reusable plugins and publish them to Neutrinos Store that will help developers reduce application development efforts.

- To create components, angular packages, and app templates, see [Create a widget](/articles/create-a-widget-on-studio-7/create-component-preface) documentation.
- To create nodes, see [Plugins Builder](/articles/project-plugins-builder-guide/node-builder-preface) documentation.
