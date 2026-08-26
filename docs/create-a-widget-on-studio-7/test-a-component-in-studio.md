# Delete the Component from Neutrinos Studio

<https://documentation.neutrinos.com/articles/#!create-a-widget-on-studio-7/test-a-component-in-studio>

| ![Information](/resources/Storage/create-a-widget-on-studio-7/info.png) | When you are testing the component, make sure the component is responsive and works well in the mobile. |
| --- | --- |

To test the component that you have created, and to debug issues, you should open the Neutrinos Studio in **Debug** mode, import the component to Neutrinos Studio, and install it. Perform the following steps:

1. If you have Neutrinos Studio running in your machine, close the application.
2. Open a Command Prompt, navigate to the folder or directory location which contains the Neutrinos Studio executable file. By default, the file is present in the following location:
  - ***C:\Program Files\Neutrinos Studio*** in a Windows machine.
  - ***/usr/bin/n-studio*** in a Linux machine.
  - ***/Applications*** in a MAC machine.
3. Open Neutrinos Studio in **Debug** mode.
  - To open Neutrinos Studio on Windows, navigate to the folder containing the **.exe** file and execute the following command. Copy CodeMarkdown"Neutrinos Studio.exe" --debug
  - To open Neutrinos Studio in Linux, navigate to the folder containing the Neutrinos Studio file, and execute the following command: Copy CodeMarkdownn-studio --debug
  - To open Neutrinos Studio on MAC, navigate to the folder containing the Neutrinos Studio file, and execute the following command: Copy CodeMarkdownopen Neutrinos Studio.app --args --debug
4. Once Neutrinos Studio starts, you will see the Chrome **DevTools **appear to the right. DevTools help you edit pages on-the-fly and diagnose problems.
5. On the [Neutrinos Studio Home page](/smart/project-concepts/studio-home-page), open an existing app in which you want to test your component.
6. On the [Application page](/smart/project-concepts/studio-application-page), open** Plugins Manager**, navigate to **Workspace Plugins. **If you have packaged the component correctly, it will appear in this tab.

| ![Information](/resources/Storage/create-a-widget-on-studio-7/info.png) | If your component is not displayed in the Workspace Plugins tab, navigate back to [Create and Publish a Component](/articles/create-a-widget-on-studio-7/create-component) and verify the steps. |
| --- | --- |

7. Install the component to your app.

8. Once installed, the **Workspace**** Plugins **page will list the component as an installed plugin.

9. Search for the installed component. The component will appear as a separate section under the palette list.

| ![Information](/resources/Storage/create-a-widget-on-studio-7/info.png) | **Known Issue: **Once you search for the component, you will see that the component icon flickering or broken in the palette list. This is a known issue and will be handled in the next release of the Neutrinos Studio. |
| --- | --- |

10. Drag and drop the component to your page designer. Make sure that the appearance of the component is correct.

11. Click the component to open its attributes window.

![](/resources/Storage/create-a-widget-on-studio-7/1-5-2-5-test-in-neutrinos-studio-img0002.png)

If you face any issues, inspect the CSS of the component using DevTools.

---

### Delete the Component from Neutrinos Studio

If you want to delete the component that you installed in Neutrinos Studio, perform the following steps:

- Delete the component folder from **$HOME/.neutrinos/plugins/marketplace-components/node_modules** folder.
- Remove the component metadata in the **$HOME/.neutrinos/plugins/marketplace-components/dependency.json **file.

By default, the $HOME path is:

- ***C:\Users\<user>*** in a Windows machine.
- **/home/<user>** in a Linux machine.
- ***/Users/<user>* ** in a MAC machine.
