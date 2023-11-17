# CS 5001 Final Project Instructions

For your final in CS 5001, we would like you to present a project related to the content learned in 5001. 
Term projects provide tangible benefits to your learning, and to your own personal goals and interests. 
It gives you as a student the opportunity to demonstrate what you learned in an applied manner. 

Your final deliverable for the project will have multiple components

1. A meeting with the instructor or TA to go over your project goals and plans.
2. A github repository that contains code, example runs, and a report that follows the structure of this [report template](../README.md)

Due dates will be listed in canvas, along with the full rubric. 

## Setting up your Repository

There are a number of resources at the bottom of this document to setup the repository on github. We have made this repository a "Template Repository", and we recommend that you use that to create your own repository. This will allow you to clone the repository to your local machine, and then push changes to your own repository. Make sure to go to the '[root](../)' of this repo, to see the "Use this template" button.

Github is a standard in the industry, and we want you to get used to using it. You will use it in future courses, and it is a great way to show off your work to potential employers.  Make sure to meet with the TA or instructor *EARLY* if you don't have it setup!

## Project Selection

When selecting your project, you will have two phases. The first involves evaluating options, doing some background
research, and then presenting your project idea to a Instructor or TA in a one-on-one meeting. The 
meeting can happen during office hours or at another arranged time. 

1. When selecting your project, think smaller! The most common mistake with projects is selecting something too large
   * The purpose of the meeting is to:
     * Make sure your ideal is more realistic in the limited time frame
     * Meets requirements to highlight topics you learned in CS 5001
  

Here are some [project ideas](ProjectIdeas.md). Look through them, but don't feel limited by them! There are many possible options for projects, and these are just a few ideas. 

## Deliverable Details

### Staff Meeting
The first part of the project is a staff (instructor or TA) to get approval for your project. We do this, because people often create projects that are often too large, and we want to make sure you are on the right track. You will setup the meeting time slot using the standard bookings options. 

For the meeting - use this [template](meeting_template.md) to prepare for the meeting!


### Github Repo
You will create a github repository to host your code, and share a link to that repo. The repo should include
a README.md explaining what the project is (and class it is for), and highlights some key aspects of the project. You will
create this under your personal github account (you can create one if you don't have one, the free version is fine). The reason
we are asking for the github hosting is (1) your project is something you should demonstrate to the world - though you are free to make it private after we grade it, and (2) you will use github in future courses, so this helps prepare you in advance. 

For your code, we will be looking at:

* Code organization: Is it well organized? Is it easy to navigate? It should not be a single giant main function!
* Code quality: Is it readable? Is it well documented? Is it well commented?
  * You should have a docstring comment for **every** function, and for standard comment for **every** line of code that is not obvious.
* Code style: Is it consistent? Does it follow the [PEP8 style guide](https://www.python.org/dev/peps/pep-0008/)?
* Test Cases: Did you test your code to ensure validity? Have you created a documented process to repeat that testing?

For your report, we will be looking at:

* Do you clearly explain your project.
* Can we duplicate running the project on our local machine
* Do you clearly highly key aspects of your project, which also include the "big ideas" of CS 5001.
* Can we understand your code from your report? Do you explain the key aspects of your code?
* Readability and clarity

Since the code report is actually the README.md file in your github repo, you will be graded on the following, make sure to look at your report in github to make sure it looks good! It should be formatted properly (see resources below), and should be easy to read.

> IMPORTANT  
> A report is not be all bullet points! We give your section headings, but you should remove the guidelines and replace them with your own content. Your own content needs to be prose paragraphs, code snippets, etc. You are building this project assuming we are an employer wanting to read what you did. 

#### Principles of Good Design, Documentation, Testing and Style:
* Top-of-File triple-double documentation string consistent with style guidelines
taught during this semester 
* Top-of-Function/Method triple-double documentation string consistent with style
guidelines taught during this semester 
* Modular design using functions, objects, and methods, with each function or
method doing one job. No “giant main()” ugly coding
* Validation of all user input. Error-handling evident throughout
* Thoughtful design choices around scope, aliasing, and mutability
* Little or no duplication of code
* Extensible: organized to allow increased functionality in the future
* Test code is provided and indicates thorough coverage
  * This can be hard for applications with graphics (GUI, webpages, etc) - your tests 
  will need to be a combination of code tests, and screenshot/videos that show interface testing! Remember to focus on keeping the code in small chunks, to make testing easier!





### Grading Rubric
Will be posted in Canvas. You will submit a link to your repo on canvas, and the course staff will grade directly off the repo.



# Resources for Github
* [Getting Started with Github](https://docs.github.com/en/get-started/onboarding/getting-started-with-your-github-account)
* [Git Handbook](https://docs.github.com/en/get-started/using-git/about-git)
* [Markdown / Writing on Github](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/quickstart-for-writing-on-github)

While the resources talk about git on your computer, and it is something you should explore - you can simply upload all your files to your repo once you create it via the web-interface.  However, using many IDEs, it may make sense to *clone* this FinalProjectTemplate repo, and then push your changes to your own repo. We have left this repo as a template repository for that reason. Follow these [instructions](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template) from github. Select "Use this template" and "Create a new repository". You can then clone your new repo to your local machine, and push changes to it.


