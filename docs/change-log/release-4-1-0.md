# 4.1.0

<https://documentation.neutrinos.com/articles/#!change-log/release-4-1-0>

## 4.1.0

#### Date: (2019-02-10)

| ![Information](/resources/Storage/change-log/info.png) | If your app is using flex-layout, please downgrade @angular/flex-layout to 7.0.0-beta.19. An open issue is being tracked and will be updated in future releases. |
| --- | --- |

---

### Features:

- Name components while designing pages in studio. [[BHIV-653](https://jatahworx.atlassian.net/browse/BHIV-653)]
- Copy and paste shortcut for drag and drop components. [[BHIV-653](https://jatahworx.atlassian.net/browse/BHIV-653)]
- Detect when the user has clicked the studio close button and then show 'Save all', 'Discard all' and 'Cancel' buttons in a dialog. [[BHIV-693](https://jatahworx.atlassian.net/browse/BHIV-693)]
- Detect when the user has clicked the app exit button and then show 'Save all', 'Discard all' and 'Cancel' button in a dialog. [[BHIV-692](https://jatahworx.atlassian.net/browse/BHIV-692)]
- Pages as views. [[BHIV-672](https://jatahworx.atlassian.net/browse/BHIV-672)]
- Performance optimization for views [[BHIV-918](https://jatahworx.atlassian.net/browse/BHIV-918)]
- A directive for image download and to view bhive-art using filter. [[BHIV-841](https://jatahworx.atlassian.net/browse/BHIV-841)]
- Added labels and a placeholder for the components [[BHIV-768](https://jatahworx.atlassian.net/browse/BHIV-768) , [BHIV-835](https://jatahworx.atlassian.net/browse/BHIV-835)]
- Dynamic icons in the icon, mini fab, and fab button components in the wysiwyg editor.
- Support for nodejs 10 added.

---

### 

### Bug Fixes

Component copy paste occurs when attributes value copy paste is done.[[BHIV-850](https://jatahworx.atlassian.net/browse/BHIV-850)].The text inside the HTML component is getting doubled when copy-pasted. [[BHIV-851](https://jatahworx.atlassian.net/browse/BHIV-851)]Cannot delete a copied component from a container [[BHIV-856](https://jatahworx.atlassian.net/browse/BHIV-856)]A droppable palette element is non-droppable on first drop [[BHIV-913](https://jatahworx.atlassian.net/browse/BHIV-913)]Views going into a loop [[BHIV-908](https://jatahworx.atlassian.net/browse/BHIV-908)]Newly created view not able to drag and drop [[BHIV-909](https://jatahworx.atlassian.net/browse/BHIV-909)]Log rotation when the log file reaches max size [[BHIV-916](https://jatahworx.atlassian.net/browse/BHIV-916)]Warn user if mismatch node or node is not installed [[BHIV-74](https://jatahworx.atlassian.net/browse/BHIV-744)]Studio throws an error on opening with a double click [[BHIV-902](https://jatahworx.atlassian.net/browse/BHIV-902)]Copy-Paste views cyclic loop [[BHIV-1050](https://jatahworx.atlassian.net/browse/BHIV-1050)]Android Emulator throws "no platform added to the project" error [[BHIV-822](https://jatahworx.atlassian.net/browse/BHIV-822)]Charts are not rendered correctly on Edge and Firefox browser [[BHIV-682](https://jatahworx.atlassian.net/browse/BHIV-682)]While creating .nos file platforms, www, plugins folders should be excluded [[BHIV-911](https://jatahworx.atlassian.net/browse/BHIV-911)]Migration logic for 4.1.0 and ArtImgSrcDirective import in declaration.ts.Mini fab and fab getting stuck at the top when dragging [[BHIV-812](https://jatahworx.atlassian.net/browse/BHIV-812)].Components shaking on hover.

**Enhancement**

Studio updated to Angular 7 and Electron update to 4.0.3 [BHIV-751](https://jatahworx.atlassian.net/browse/BHIV-751).All seed app dependencies updated to the latest version.
