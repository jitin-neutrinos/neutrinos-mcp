# Release 7.4.0

<https://documentation.neutrinos.com/articles/#!change-log/release-7-4-0>

#### Release 7.4.0

### Date: 10 December 2020

### Enhancements

- The following nodes are added to the Server Services Designer:
  - [Emit node](/smart/project-server-side-service-designer/emit)
  - [Listen node](/smart/project-server-side-service-designer/listen)
  - [Textract node](/smart/project-server-side-service-designer/textract-node)
  - S3 node which includes:
    - [S3 Bucket](/smart/project-server-side-service-designer/s3-bucket)
    - [S3 Upload](/smart/project-server-side-service-designer/s3-upload)
    - [S3 Object](/smart/project-server-side-service-designer/s3-object)
    - [S3 Multiport Upload](/smart/project-server-side-service-designer/s3-multiport-upload)
  - SFTP node which includes:
    - [SFTP List](/smart/project-server-side-service-designer/sftp-list)
    - [SFTP Get](/smart/project-server-side-service-designer/sftp-get)
    - [SFTP Put](/smart/project-server-side-service-designer/sftp-put)
    - [SFTP Command](/smart/project-server-side-service-designer/sftp-command)
  - [Crypto node](/smart/project-server-side-service-designer/crypto-node)
- Added a new editor for the IDS UI configuration.
- Added a Settings editor UI to skip consent and shared client info.

**Bug Fixes**

- Middleware dirty and invalid check not in place.
- Not able to save the Middleware Workspace Sequence.
- Not able to add util to a node when another node's util is open.
- While moving the attributes using a handler, data is not updated in the form.
- Plugin Builder:
  - Documentation link not added.
  - Invalid icon not shown after drag and drop of the node.
  - Version not updated in the package.json file of the package while updating the package.
  - Allow spaces and numbers in the node name.
  - Invalid icon not shown after drag and drop of the node.
- Deleted page import is not removed from the declaration.ts script.
- Add docsLink placeholder is not added in node Html.
- Neutrinos Login Template does not download by default.
- The locally published plugin should not be added to the package.json file in .neutrinos.
