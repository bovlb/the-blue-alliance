# CI/CD Setup

## Configure Secrets

Under your repository Settings > Secrets on GitHub, set the following secrets:

- `GCLOUD_PROJECT_ID`: Google Cloud Project ID

  You can find this by going to your [Google Cloud Platform Dashboard](https://console.cloud.google.com/home/dashboard).

- `GCLOUD_AUTH`: Base64-encoded string representation of your service account JSON key

  e.g. `cat my-key.json | base64`

  More info on [creating and managing service account keys](https://cloud.google.com/iam/docs/creating-managing-service-account-keys).

- `FIREBASE_API_KEY`: Firebase App API key

  You can find this key by going to your [Firebase Project](https://console.firebase.google.com/) Settings -> General -> Your project -> Web API Key.

- `FIREBASE_APP_ID`: Firebase App ID

  You can find this key by going to your [Firebase Project](https://console.firebase.google.com/) Settings -> General -> Your apps -> App ID

  If an app does not already exist, click "Add app" and setup a Web app.

- `FIREBASE_MESSAGING_SENDER_ID`: Firebase App Cloud Messaging Sender ID

  You can find this key by going to your [Firebase Project](https://console.firebase.google.com/) Settings -> Cloud Messaging -> Project credentials -> Sender ID