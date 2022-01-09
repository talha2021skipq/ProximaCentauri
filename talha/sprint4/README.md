

# Sprint4: Create and Deploy a Frontend for the API Gateway Using ReactJS Chakra UI 
## Table of Contents

1. [Project Summary](#Project-Summary)
2. [Services Covered](#Services-Covered)
3. [Installation Guide](#Installation-Guide)
4. [ReactJS App Creation](#ReactJS-App-Creation)
5. [Project Status](#Project-Status)
6. [Author](#Author)

## Project Summary 

In the previous work, I created a public CRUD API gateway so that user can Read, Write, Update or Delete URLs in dynamodb table through the API Gateway. To deliver this service to the user, I designed a frontend for this API gateway and I have implemented Oauth as authorization or my frontend. I have created a ReactJs app in VS code,the app folder will also be uploaded to github, but you need to setup this APP seperately in VS Code or just git clone. 
## Services Covered

1. AWS API Gateway
2. Dynamodb
3. S3 buckets
5. AWS lambda
6. AWS Amplify
7. AWS Pipelines
9. AWS Codepipeline Actions

## Installation Guide 

Follow these easy steps to set up the environment and run the project:

1. Run the following command to clone the repo:
	
	    `git clone https://github.com/talha2021skipq/ProximaCentauri.git`

2. Land in my project directory by running the command:

	   `cd ProximaCentauri/talha/sprint4`

3. Bootstrap the environment by using following command:

           `cdk bootstrap aws://315997497220/us-east-2 --qualifier talha --toolkit-stack talhastoolkit`
 	- Make sure to specify qualifier name as talha, if you change it then you will have to replace talha with your qualifier's name on line number 24 in `cdk.json` file as shown below:

 			`"@aws-cdk/core:bootstrapQualifier": "talha2"`
4. The environment is bootstrapped, now it's time to deploy the pipeline. Deploy the pipeline by using the below mentioned command but make sure you are in the same directory where the `app.py` is located.  
          
           `cdk deploy Sprint4TalhaPipelineStck`
5. Go to the console and open code pipelines to see the pipeline fully working. Search the pipeline by name 'Sprint3TalhaPipelineStck'. 
6. Go to the console and open API Gateway to test and run the API. Open TalhasAPI from APIs Dashboard. Click on 'ANY' Method to open the created API Gateway for web crawler.
7. Now click on Test to run the API and then select any method from the drop down menue to perform CRUD operations.

## ReactJS App Creation

To start with ReactJS app, you have to follow these easy steps:

1. Go to terminal and run this command to create a reactJS app,

        `npm install –g create-react-app`

2. Then run,

        `npm create-react-app talhas_rjs_ap`

3. Go to that app folder,

        `cd talhas_rjs_app`

4. Install the dependencies:

CHAKRA

        `npm i @chakra-ui/react @emotion/react@^11 @emotion/styled@^11 framer-motion@^5`
React-Paginate        

        `npm install react-paginate`
AXIOS
    
        `npm i axios`
    

5. Arrange the file in the same format as shown above and the run the app using,
    
        `npm start`
6. Now you need build of this app to deploy it in AWS_AMPLIFY, So for that run the following command:
        `npm run build`
7. Now a folder with name 'build' will be created in the same directory, now you have to zip this folder by keeping all the files directly in the zip file and then upload the zip file either directly in you amplify app, or in S3 bucket if the amplify app is sourced from the bucket.  
That's ALL
## Project Status

Completed!

## Author

 Talha Naeem 
DevOps Trainee @skipQ 
talha.naeem.s@skipq.org

Thanks! Enjoy:)













#### Helpful if you want to setup you cdk project

This is a blank project for Python development with CDK.

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization
process also creates a virtualenv within this project, stored under the `.venv`
directory.  To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.

To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!
