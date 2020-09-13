The Blue Alliance leverages [Firebase](https://firebase.google.com/) for several services, including authentication, real-time data, crash reporting, analytics, and more. Most services provided by Firebase are not necessary for local development. However, some services like Authentication are only available by hitting an upstream Firebase instance.

## Add Firebase Project
1. Navigate to the [Firebase Console](https://console.firebase.google.com/)
2. Click `Add Project`
3. Enter a project name to work with - preferably something namespace'd to yourself (ex: `zach-tba-dev`)
4. Finish setting up your project. You should be redirected to the project's overview page. If not, you can access the project's overview by clicking on the project in the Firebase Console.
5. On the overview page, start the flow to setup a new Web app to your project. This can also be found in Gear -> Project Settings -> General -> Your apps and clicking Web.
6. Enter any required information for your app and click `Register App`

## Setup Secrets
After setting up your app, you should see a set of keys. The Blue Alliance already imports required Firebase Javascript. It's only necessary to setup the configuration keys locally. Keys are referenced from a `tba_keys.js` file. This file is not checked in to source control, but an template of the file is. You can copy the template and add your own keys to the file.

```
$ cp src/backend/web/static/javascript/tba_js/tba_keys_template.js src/backend/web/static/javascript/tba_js/tba_keys.js
```

Edit the fields specified in the file and save. If you're using the development container, make sure to sync this file to the container. Finally, [rebuild web resources](https://github.com/the-blue-alliance/the-blue-alliance/wiki/Development-Runbook#rebuilding-web-resources-javascript-css-etc) to compile the secrets file with the Javascript.

## Configure Authentication

1. Navigate to the Authentication tab on the left-hand side under Develop.
2. Under `Sign In Method`, click `Google` and toggle the `Enable` button.
3. Click the `Save` button

When navigating your local project, make sure to use the `http://localhost:8080` domain, as `localhost` is the only local domain specified in the `Authorized domains` section. Otherwise, add `0.0.0.0` in the `Authorized domains` section.

Other authentication providers can be setup, if necessary. Currently, The Blue Alliance only supports Google and Apple as authentication providers.

## (Optional) Additional Configuration

Additional steps to replicate The Blue Alliance's Firebase configuration in your own Firebase project. These steps are included for completeness and for any situational use cases, but will not be necessary for most contributors.

### Configure Authorized Domains

In Firebase, production domains should be included in the Develop -> Authentication -> Sign In Method -> Authorized domains section. Additionally if the Firebase API key has restricted permissions, the `{project_id}.firebaseapp.com` redirect domain must be included as a valid HTTP referrer for the API key. This can be configured in Google Cloud Platform Console when navigating to API & Services -> Credentials -> API Keys -> editing the API key in question and adding the `{project_id}.firebaseapp.com` domain under the `Website restrictions` section. If the Firebase API key is not restricted, this step is not required.

### Configure Sign In with Apple

The [Firebase documentation for setting up Sign In with Apple](https://firebase.google.com/docs/auth/web/apple) should be considered the master document for these steps, as they may change. All of the code-related steps have already been done inside the codebase.

### Configure Service Accounts

Existing service accounts can be configured with Firebase permissions by giving them the proper roles in IAM. This is necessary when using Firebase Admin SDK APIs like Cloud Messaging or Remote Config on a server, or when granting users access to parts of the Firebase Console. The broadest role is the `Firebase Admin SDK Administrator Service Agent`, which can be helpful when debugging against a personal instance. Production service accounts should be more mindful about which roles they are given. For more details, see a complete list of [Firebase IAM Roles](https://firebase.google.com/docs/projects/iam/permissions).