# **Deploying to DigitalOcean on App Platform**

This README will guide you through deploying a Django app to DigitalOcean using the App Platform.

Please note that other cloud services are available to deploy a Django app, but we have chosen to use DigitalOcean and provided the steps on how to do this.

It is important to note that DigitalOcean is a PAID service and there are costs associated with deploying your app using this service. At the time of writing, DigitalOcean is offering $200 free credit for a student account and $100 free credit for a standard account. We are NOT responsible for any charges incurred by deploying the app on this service. Please ensure that you review the pricing and billing information carefully before using DigitalOcean or any other cloud service.

**Prerequisites**

1. A GitHub account [https://github.com/](https://github.com/)
2. A fork of our apps code from GitHub to your account
3. A digitalocean account [https://www.digitalocean.com/](https://www.digitalocean.com/)

**Deploying**

**Step 1: Create an App**

1. Visit [https://cloud.digitalocean.com/apps](https://cloud.digitalocean.com/apps) and click Create App.
2. Connect your GitHub account and allow DigitalOcean to access your repositories.
3. Under the Repository section, select 'your\_account/appforkname' repository from the dropdown menu.
4. Select the main branch and set source directory to 'ekozumi'.
5. Choose whether to enable autoscaling. Then, click Next.

**Step 2: Configure Run Command**

1. Click the Edit pencil icon next to the app.
2. Click Edit to the right of the Run Command section.
3. Edit your run command to reference your project's WSGI file. Your completed run command should be 'gunicorn --worker-tmp-dir /dev/shm django\_ekozumi.wsgi'.
4. Click Save to confirm the change, then click Back at the bottom of the page to return to the Resources page.

**Step 3: Select Plan**

1. Click Edit Plan to select the appropriate plan to fit your needs, whether in Basic App or Professional App.
2. Click Next to proceed.

**Step 4: Deploy the App**

1. Once the build process completes, add your app's domain created by Digitalocean 'example-app-name.ondigitalocean.app' to the ALLOWED\_HOSTS array within /ekozumi/ekozumi/settings.py in your GitHub fork.
2. Click Actions and Deploy again to deploy the app if auto deploy was not selected.

**Step 5: Deploy Static Files**

1. Once your app is deployed, click the Create button and choose Create Resources From Source Code to add a static site component.
2. Select the same GitHub repository as your deployed Django service and select 'ekozumi' as the source directory. Click Next to continue.
3. Ensure that the main branch and Autodeploy are selected. Click Next to continue.
4. Click the Edit pencil icon next to the app. Click Edit to the right of the Resource Type section.
5. Select Static Site from the dropdown menu, then click Save to confirm your change.
6. Click Edit to the right of the Output Directory section and set it to 'staticfiles'. Click Save to confirm your change.
7. Click Edit to the right of the HTTP Request Routes section, then enter '/static' in the Routes field. Click Save to confirm your change.
8. Click Back at the bottom of the page to return to the Resources page, then click Next until you finalize creation.

That's it! Your Django app is now deployed to DigitalOcean using the App Platform. More detailed documentation can be found here [https://docs.digitalocean.com/](https://docs.digitalocean.com/).
