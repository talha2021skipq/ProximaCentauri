

# Sprint5: Docker Image for API Testing with AWS ECS Deployment from Image Repository at AWS ECR 
## Table of Contents

1. [Project Summary](#Project-Summary)
2. [Services Covered](#Services-Covered)
3. [Installation Guide](#Installation-Guide)
4. [Docker Commands](#Docker-Commands)
5. [Project Status](#Project-Status)
6. [Author](#Author)

## Project Summary 

In the sprint, I will use docker-compose to build API test clients using pyresttest and Syntribos. These tests will exercise the web crawler's CRUD endpoint built in the previous sprint. I will publish the built images to AWS ECR and deploy API test clients an EC2 instance using ECS. In the end, I will have to push API test results into CloudWatch and setup alarming and notification on API test metrics. 
## Services Covered

1. AWS API Gateway
2. Dynamodb
3. S3 buckets
5. AWS lambda
6. AWS Pipelines
7. AWS Codepipeline Actions
8. AWS ECR
9. AWS ECS
10. AWS EC2

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
5. Go to the console and open code pipelines to see the pipeline fully working. Search the pipeline by name 'TalhaPipelineStack'. 
6. Go to the console and open AWS ECS to see Task Definition and Cluster which are created to deploy the docker image in them. 

## Docker Commands

To start with Docker image, you have to go to the directory in which the Docker file is located and then follow these easy steps:

1. Go to terminal and run this command to build the Docker image,

        `docker build -t talhanew .`

2. Then run this command to check the newly built image,

        `docker images`

3. Configure the aws for ECR authentication (You will have to give access token and the ID),

        `aws configure`

4. Push the image to AWS ECR,


        `docker push image-name:tag`

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
