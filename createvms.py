#1-In GCP console, on the top right toolbar, click the Open Cloud Shell button.
#2-To display a list of all the zones in the region to which Qwiklabs assigned you
gcloud compute zones list | grep *<us-central1>*
#3-To set your default zone to the one you just chose
gcloud config set compute/zone *<us-central1-b>*
#4-To create a VM instance called my-vm-2 in that zone, execute this command
gcloud compute instances create "<my-vm-2>" \
--machine-type "<n1-standard-1>" \
--image-project "<debian-cloud>" \
--image "<debian-9-stretch-v20190213>" \
--subnet "default"
#5-To close the Cloud Shell
exit
#TO CONNECT BETWEEN VM INSTANCES
#1-To open a command prompt on the my-vm-2 instance, click SSH in its row in the VM instances list.
#2-Use the ping command to confirm that my-vm-2 can reach my-vm-1 over the network
ping *<my-vm-1>*
#3-Notice that the output of the ping command reveals that the complete hostname of my-vm-1 is my-vm-1.c.PROJECT_ID.internal, where PROJECT_ID is the name of your Google Cloud Platform project. 
#4-Press Ctrl+C to abort the ping command.
#5-Use the ssh command to open a command prompt on my-vm-1
ssh my-vm-1
#6-If you are prompted about whether you want to continue connecting to a host with unknown authenticity, enter yes to confirm that you do.
#7- At the command prompt on my-vm-1, install the Nginx web server
sudo apt-get install nginx-light -y
#8- Use the nano text editor to add a custom message to the home page of the web server:
sudo nano /var/www/html/index.nginx-debian.html
#9- Use the arrow keys to move the cursor to the line just below the h1 header. Add text like this, and replace YOUR_NAME with your name
<h1> Hi from YOUR_NAME </h1>
#10- Press Ctrl+O and then press Enter to save your edited file, and then press Ctrl+X to exit the nano text editor.
#11- Confirm that the web server is serving your new page. At the command prompt on my-vm-1, execute this command:
curl http://localhost/
#12- To exit the command prompt on my-vm-1, execute this command:
exit
#13- You will return to the command prompt on my-vm-2
#To confirm that my-vm-2 can reach the web server on my-vm-1, at the command prompt on my-vm-2, execute this command:
curl http://my-vm-1/
#14- Copy the External IP address for my-vm-1 and paste it into the address bar of a new browser tab. You will see your web server's home page, including your custom text.
#If you forgot to click Allow HTTP traffic when you created the my-vm-1 VM instance, your attempt to reach your web server's home page will fail. You can add a firewall rule to allow inbound traffic to your instances
#fin.