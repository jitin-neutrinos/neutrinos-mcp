# Placeholders to replace:

<https://documentation.neutrinos.com/articles/#!pulse-publication/identity-server-faq>

How to use this script

1. Click anywhere inside the grey code box below.
2. Press `Ctrl + A` to select all lines, then `Ctrl + C` to copy.
3. Paste into your Jenkinsfile and replace every `${YOUR_...}` placeholder with your actual value.
4. Refer to the full documentation for a description of each placeholder.

### Placeholders to replace:

| **Placeholder** | **Replace with** |
| --- | --- |
| ${YOUR_ACR_REGISTRY_URL} | Your Azure Container Registry hostname, e.g. mycompany.azurecr.io |
| ${YOUR_AKS_RESOURCE_GROUP} | Azure Resource Group containing your AKS cluster, e.g. RG-AKS-DEV-01 |
| ${YOUR_AKS_CLUSTER_NAME} | Your AKS cluster name, e.g. AKS-DEV-CLUSTER |
| ${YOUR_JENKINS_NODE_LABEL} | Jenkins agent label, e.g. linux or Trinity-XL |
| ${YOUR_NODEJS_TOOL_NAME} | Node.js tool name configured in Jenkins, e.g. nodejs_22_lts |
| ${YOUR_BITBUCKET_REPO_URL} | HTTPS URL of your identity-server repository |
| ${YOUR_BITBUCKET_CREDENTIAL_ID} | Jenkins credential ID for Bitbucket access |
| ${YOUR_GIT_USERNAME} | Git user name for automated commits, e.g. Jenkins Bot |
| ${YOUR_GIT_EMAIL} | Git email for automated commits, e.g. jenkins@yourcompany.com |
| ${YOUR_ACR_CREDENTIALS_ID} | Jenkins credential ID for ACR Docker login |
| ${YOUR_AZURE_SP_CREDENTIALS_ID} | Jenkins credential ID for Azure Service Principal (Helm deploy only) |

### Jenkinsfile

```code
def dockerRegistery = '${YOUR_ACR_REGISTRY_URL}' 

def AKS_RESOURCE_GROUP = '${YOUR_AKS_RESOURCE_GROUP}' 

def AKS_CLUSTER_NAME = '${YOUR_AKS_CLUSTER_NAME}' 

  

pipeline { 

    agent { label '${YOUR_JENKINS_NODE_LABEL}' } 

  

    tools { nodejs '${YOUR_NODEJS_TOOL_NAME}' } 

  

    parameters { 

        string(name: 'BRANCH_NAME', defaultValue: '', 

               description: 'Branch name to build') 

        string(name: 'PREID', defaultValue: '', 

               description: 'Prerelease identifier (e.g. beta, rc). Leave empty for patch release') 

        booleanParam(name: 'RELEASE', defaultValue: false, 

               description: 'Perform a release build') 

        booleanParam(name: 'SKIP_DEPS', defaultValue: true, 

               description: 'Skip bumping/publishing UMA and updating deps') 

        string(name: 'HELM_UPGRADE_NAMESPACE', defaultValue: '', 

               description: 'K8s namespace to deploy Helm chart. Leave blank to skip') 

        booleanParam(name: 'REFRESH_PIPELINE_SCRIPT_AND_EXIT', defaultValue: false, 

               description: 'Set to true to refresh the pipeline script and exit without building') 

    } 

  

    environment { 

        WORKDIR = "${env.WORKSPACE}" 

    } 

  

    stages { 

  

        stage('Refresh Pipeline Script') { 

            when { expression { params.REFRESH_PIPELINE_SCRIPT_AND_EXIT } } 

            steps { 

                script { 

                    echo 'Refreshing pipeline script and exiting...' 

                    currentBuild.result = 'ABORTED' 

                    error('Pipeline script refreshed.') 

                } 

            } 

        } 

  

        stage('Validate Parameters') { 

            steps { 

                script { 

                    if (!params.BRANCH_NAME?.trim()) { 

                        error 'BRANCH_NAME parameter is required' 

                    } 

                    if (!params.RELEASE && !params.PREID?.trim()) { 

                        error 'PREID must be specified for release builds' 

                    } 

                    dockerRegistery += params.RELEASE ? '/alpha' : '/alpha-dev' 

                    echo "Using Docker registry: ${dockerRegistery}" 

                } 

            } 

        } 

  

        stage('Clean Workspace') { 

            steps { cleanWs() } 

        } 

  

        stage('Checkout') { 

            steps { 

                dir('identity-server') { 

                    checkout ([ 

                        $class: 'GitSCM', 

                        branches: [[name: params.BRANCH_NAME]], 

                        userRemoteConfigs: [[ 

                            url: '${YOUR_BITBUCKET_REPO_URL}', 

                            credentialsId: '${YOUR_BITBUCKET_CREDENTIAL_ID}' 

                        ]], 

                    ]) 

                } 

                dir('identity-server') { 

                    sh "git checkout ${params.BRANCH_NAME}" 

                } 

            } 

        } 

  

        stage('Prepare Environment') { 

            steps { 

                dir('identity-server') { 

                    sh "git config user.name '${YOUR_GIT_USERNAME}'" 

                    sh "git config user.email '${YOUR_GIT_EMAIL}'" 

                } 

                dir('identity-server') { 

                    sh 'npm ci --legacy-peer-deps' 

                } 

            } 

        } 

  

        stage('Docker Login') { 

            steps { 

                script { 

                    withCredentials([usernamePassword( 

                        credentialsId: '${YOUR_ACR_CREDENTIALS_ID}', 

                        usernameVariable: 'DOCKER_USERNAME', 

                        passwordVariable: 'DOCKER_PASSWORD' 

                    )]) { 

                        sh "echo ${DOCKER_PASSWORD} | docker login -u ${DOCKER_USERNAME} \ 

                            --password-stdin ${dockerRegistery.split('/')[0]}" 

                    } 

                } 

            } 

        } 

  

        stage('Build and Push Image') { 

            steps { 

                script { 

                    def args = [] 

                    if (params.SKIP_DEPS) { args << '--skip-deps' } 

                    args << "--docker-registry=${dockerRegistery}" 

                    if (params.PREID?.trim()) { args << "--preid=${params.PREID.trim()}" } 

                    if (params.RELEASE) { args << '--release' } 

                    dir('identity-server') { 

                        def output = sh( 

                            script: "node scripts/build-push.mjs ${args.join(' ')}", 

                            returnStdout: true 

                        ).trim() 

                        echo output 

                        def tagMatch = output =~ /Tag: (.+)$/ 

                        if (tagMatch) { 

                            env.BUILD_TAG = tagMatch[0][1] 

                            echo "Extracted build tag: ${env.BUILD_TAG}" 

                        } else { 

                            error 'Failed to extract tag from build script output' 

                        } 

                    } 

                } 

            } 

        } 

  

        stage('Helm Deploy (optional)') { 

            when { expression { params.HELM_UPGRADE_NAMESPACE?.trim() } } 

            steps { 

                script { 

                    withCredentials([azureServicePrincipal( 

                        credentialsId: '${YOUR_AZURE_SP_CREDENTIALS_ID}', 

                        subscriptionIdVariable: 'AZURE_SP_SUBSCRIPTION_ID', 

                        clientIdVariable: 'AZURE_SP_CLIENT_ID', 

                        clientSecretVariable: 'AZURE_SP_CLIENT_SECRET', 

                        tenantIdVariable: 'AZURE_SP_TENANT_ID' 

                    )]) { 

                        sh """ 

                          az login --service-principal \ 

                              -u "$AZURE_SP_CLIENT_ID" \ 

                              -p "$AZURE_SP_CLIENT_SECRET" \ 

                              -t "$AZURE_SP_TENANT_ID" 

                          az account set --subscription "$AZURE_SP_SUBSCRIPTION_ID" 

                          az aks get-credentials \ 

                              --resource-group "${AKS_RESOURCE_GROUP}" \ 

                              --name "${AKS_CLUSTER_NAME}" \ 

                              --overwrite-existing 

                          kubectl get nodes -o wide || true 

                          helm version || true 

                        """ 

                    } 

                    dir('identity-server') { 

                        sh """ 

                        helm upgrade identity-server ./charts \ 

                            -f ./charts/values.yaml \ 

                            --namespace ${params.HELM_UPGRADE_NAMESPACE} \ 

                            --debug --atomic --timeout 10m 

                        """ 

                    } 

                } 

            } 

        } 

  

        stage('Push Version Commit and Tags') { 

            when { 

                expression { 

                    sh( 

                        script: "git -C '${env.WORKSPACE}/identity-server' diff --name-status @", 

                        returnStatus: true 

                    ) == 0 

                } 

            } 

            steps { 

                script { 

                    dir('identity-server') { 

                        sh """ 

                            echo 'Creating git tag and pushing changes' 

                            git add --all 

                            git commit -m 'ci: version bump and dependency update' 

                            git tag -a ${env.BUILD_TAG} -m 'build: ${env.BUILD_TAG}' 

                            git push --follow-tags 

                        """ 

                    } 

                } 

            } 

        } 

    } 

  

    post { 

        always { 

            sh 'az logout || true' 

            echo 'Pipeline completed.' 

        } 

    } 

}
```
