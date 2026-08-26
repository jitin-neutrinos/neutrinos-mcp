# Generate the code to import node utils

<https://documentation.neutrinos.com/articles/#!plugins-builder-guide-8/node-utils>

Each node that you create will have some utility files. These files define the functionalities to be consumed by the node at the runtime of the app.

1. Click the plus icon next to **Node Utils**.
2. Enter the name of the utility module and press Enter. For example, **GenericRDBMSOperations**.

![](/resources/Storage/plugins-builder-guide-8/utils.png)

### Generate the code to import node utils

To generate the code to import the node utilities to service, perform the following:

1. Open the **Code Generation **editor.
2. Find the method by the name **[generateImports](/articles/plugins-builder-guide-8/code-generation/a/h4_1584156788). **Define this method if not found.
3. Modify the **generateImports **method to return an array of objects in this format:Copy CodeJavaScriptgenerateImports() { const nodeName = '' // name of the package (copy from the package details editor) const nodeName = '' // name of the node (copy from the node details editor); const utilName = '' // name of the util return [ { library: `./utils/${packageName}/${nodeName}/${utilName}`, modules: [ utilName ] } ] }
4. After modifying, save the code. The service will have access to the imported **util **where the node is used.

### Add the imported util to the code

1. In the **Code Generation** editor, find the method by the name **[generateSnippet](/articles/plugins-builder-guide-8/code-generation/a/h3_2122082004). **Define this method if not found.
2. Modify the **generateSnippet **method to return a string in this format:Copy CodeJavaScriptgenerateSnippet(serviceType, serviceClassTemplate) {
    const utilName = '' // name of the util;
    return `const utilInstance = new ${utilName}();
    await utilInstance.executeSQL();`;
    }
3. After modifying, save the code.
