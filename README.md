# BMI6319Question

As a Ph.D. student in SBMI, I was exposed to the predictive modeling task to detect the reoccurrence of breast cancer. After exploring the dataset, I decided to use the binary-classification algorithm for this task. In this project, I will first load the data set and prepare the dataset for the machine learning toolkit, which is 'Liblinear' in this case. To make sure all the works are reproducible, I also create a self-contained docker image to run the whole experiment.

Usage:
1.	Check out the source code:
https://github.com/jingqimelax/BMI6319Question.git
2.	Build the docker image:
Install docker if you don’t have it yet: https://docs.docker.com/docker-for-mac/install/
	Run command: ./build.sh
3.	Set the data directory: Open the ‘run_docker.sh’ file, and update the data path accordingly.
  vim run_docker.sh
  docker run -v <your_data_path>:/data/ bmi6319question /app/run.sh
 
4.	Run the package:
./run_docker.sh
 
5.	Collect the accuracy:
cd corpus/working/
ls *.eval | while read l; do echo $l; cat $l; echo; done
