# Lifecycle Events nodes

<https://documentation.neutrinos.com/articles/#!flow-designer-guide/lifecycle-events>

This is the default topic template.

When we create a page on Neutrinos Studio, a **page** component is created by default. This component instance has a lifecycle that starts when Neutrinos Studio instantiates the component class and renders the component view along with its child views.

To handle the lifecycle of the page component, use these nodes on the [Page Designer](/smart/project-concepts/page-designer):

- [On Init](/articles/flow-designer-guide/on-init-node)
- [On Changes](/articles/flow-designer-guide/on-changes-node)
- [Do Check](/articles/flow-designer-guide/do-check-node)
- [After Content Init](/articles/flow-designer-guide/after-content-init-node)
- [After Content Checked](/articles/flow-designer-guide/after-content-checked-node)
- [After View Init](/articles/flow-designer-guide/after-view-init-node)
- [After View Checked](/articles/flow-designer-guide/after-view-checked-node)
- [On Destroy](/articles/flow-designer-guide/on-destroy-node)

You can use these lifecycle event nodes to tap into key events in the lifecycle of the **page** component in order to initialize new instances, initiate change detection when needed, respond to updates during change detection, and clean up before the deletion of instances.
