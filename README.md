# Steps to connect to GCP
# I will need to create a GCP Kubernetes cluster by navigating to Kubernetes Engine > Cluster in GCP
# Then, I will need to reference a yaml file for my frontend service and backend service using nano frontend.yaml, etc. and the command kubectl apply -f frontend.yaml, etc.
# tweaking some of the IP addresses.

# The build/run commands you used to run the client-side application 
# docker build -t frontend .
# docker run -t frontend . or docker run -t frontend bash to see the files

# At this point, the frontend.py python file asks the user to input the destination path for the file they want to upload and asks them to manually execute the docker cp command
# to copy the file over, however in the future I would like to have the process be more user friendly. There is also the problem of the container stopping because no process is
# being run, which requires the user execute the command docker run -t -d frontend so that the bash waits in the background and the container does not close.
# At the same time, I was researching using an nginx image to upload the file to the Hadoop cluster directly using reverse proxy, but this process is complicated and requires that
# I find a sample Java program that allows a user to upload a file. This process would require hard coding IP addresses like the extra credit mini project does.
# I was planning on using the program found here: https://github.com/imehrdadmahdavi/map-reduce-inverted-index to create a Hadoop cluster that would create the inverted indexes
# for the files, but so far I only know how to manually upload files in the Dataproc section of GCP where the cluster is created and not how to pass the files from the first
# application to the second.
