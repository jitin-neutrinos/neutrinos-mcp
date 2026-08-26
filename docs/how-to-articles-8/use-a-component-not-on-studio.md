# Use a Component that is not on Studio or Store

<https://documentation.neutrinos.com/articles/#!how-to-articles-8/use-a-component-not-on-studio>

Neutrinos Studio hosts a list of [palette components](/smart/project-concepts/palette-component) to design your applications. It also provides [additional components on Neutrinos Store](/smart/project-concepts/store-component) which you can download and use while designing your applications.

If you want to use a component that is not on Neutrinos Studio, or Store, you should import the component library to the app and then use the component in an app page. That is,

1. You should first add the component library and its modules as a dependency to the app by using the Plugins Manager. See [Manage App Dependencies](/smart/project-sample-how-to-guide/manage-app-dependencies/a/h3_1506476317) to learn more.
2. Then, use the component library and modules on the app page by using the [Use Dependency](/smart/project-page-services-designer-guide/use-dependency-node) node.

See an example of how to use the bottom sheet component that is not on Studio or Store - [Display a Bottom Sheet on a Page](/articles/how-to-articles-8/display-a-bottom-sheet-on-a-page).
