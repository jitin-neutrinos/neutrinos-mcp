# Prerequisites

<https://documentation.neutrinos.com/articles/#!neutrinos-studio-migration-guide/migration-steps-from-6-0-0-to-6-0-4>

### Prerequisites

| ![Information](/resources/Storage/neutrinos-studio-migration-guide/info.png) | Before following the below steps, please make sure you have already migrated the app to the latest version using Neutrinos Studio's auto migrate feature. |
| --- | --- |

Perform these steps if you are migrating your app from Neutrinos Studio 6.0.x to 6.1.0.

If you are migrating your app from previous releases of Neutrinos Studio, perform the migration steps mentioned in the below topics (based on the version from which you are upgrading) before you proceed with this topic.

- [Migrate from 5.x to 6.0.0](/articles/neutrinos-studio-migration-guide/migrate-from-5)
- [Migrate to 4.0.2](/articles/neutrinos-studio-migration-guide/migrate-to-402)
- [Migrate to 3.3.1](/articles/neutrinos-studio-migration-guide/migrate-to-3)

For example, If you are migrating your app from Neutrinos Studio version 5.0.4 to version 6.1.0, perform migration steps mentioned in [migrate from 5.x to 6.0.0](/articles/neutrinos-studio-migration-guide/migrate-from-5) and then perform the steps mentioned below.

---

### Migration Steps

#### Handle custom dependencies

**Package.json file**: If you migrate your app to Neutrinos Studio version 6.1.0, dependencies such as npm and Angular packages will be deleted from the **package.json** file. This happens only if you have manually added these dependencies without using the [Plugins Manager](/smart/project-sample-how-to-guide/manage-app-dependencies).

Make sure that you add these dependencies to your app using the [Plugins Manager](/smart/project-sample-how-to-guide/manage-app-dependencies).

**Other files:** Also, the following files will be replaced when your app gets migrated. If you had made any changes to these files, make sure that you perform the changes again.

- package.json
- n-dataSorce.service.ts
- n-localeResources.service.ts
- n-map.component.ts
- polyfills.ts
- import-modules.ts

---

#### Angular version

Angular version is updated from 7.2.3 to 8.2.0.

To support Angular version 8.2.0 in Neutrinos Studio, perform the following updates in your app:

**http package: **Migrate the http package from **@angular/http** to **@angular/common/http**.Refer to the [deprecations guide](https://angular.io/guide/deprecations#angularhttp) to learn the migration steps.


 **Static Flag**: Add a static flag to all **@ViewChild** and **@ContentChild** queries. This is required in Angular version 8 to specify whether the query is static or dynamic.

**Earlier:**@ViewChild(‘signaturecanvas’)

**To be updated to:**@ViewChild(‘signaturecanvas’, {static: <true> or <false>})

**HTML tags: **Make sure that you place the **<tr>** and **<col>** tags inside a parent tag. This is required to follow HTML specifications.



 Wrap the **<tr>** tag in **<tbody>** or **<thead>** tags.




 Wrap the **<col>** tag in **<colgroup>** tag.

---

#### The rxjs-compat package

The rxjs-compat package was created so that developers could upgrade to **RxJS version 6** without having to modify code. It re-implements the prototype-patching operators and makes available all of the RxJS-version-5 export locations.

In this version of Neutrinos Studio, this package is not supported as Angular 8 has dropped support for this package. Therefore, there are a couple of breaking changes that may affect end apps mainly around the use of observables, map, import statements, timeout, etc. To see a complete list of breaking changes that could occur when removing this package, refer the [dropping-the-compatibility-layer](https://github.com/ReactiveX/rxjs/blob/master/docs_app/content/guide/v6/migration.md#dropping-the-compatibility-layer) section.

---

#### Flex Layout

Flex layout is upgraded from version 7.0.0-beta.19 to 8.0.0-beta.26.

- **core:** The MediaObserver service is the only supported mechanism to watch breakpoint activations outside the library as the ObservableMedia service is deprecated in anticipation of RxJS version 7.
- The filterOverlaps property now defaults to** false.**
- The stream data type for asObservable is changed from MediaChange to MediaChange[].
- The media$ API is deprecated in favor of the asObservable() function.
- ServerMatchMedia is no longer exported.
- MatchMedia is no longer exported as a public utility.

---

**Node.js version**

The node.js version is updated to support versions between 10.9.x and 12.x.x.

---

#### Mobile Builds

If your app supports mobile platforms, and if you are migrating from previous versions of Neutrinos studio, perform the following steps:

1. In your app directory, open the gulpfile.js file.
2. Add this code snippet at the end of the file:
    Copy CodeJavaScriptvar fs = require('fs');
   gulp.task('create-www', () =>
    {
    if (!fs.existsSync('/www')) {
    return gulp.src('*.*', { read: false })
    .pipe(gulp.dest('./www'));
   }
    }
    );
3. From your app directory, open the package.json file with any editor and replace "app-prepare": "cordova prepare", with "app-prepare": "gulp create-www && cordova prepare".

This migration step creates a **www **folder in your app directory when you trigger a mobile build from the Neutrinos Studio.
