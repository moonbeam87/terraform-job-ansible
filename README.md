# Terraform Job for Nuspire

[![Terraform](https://img.shields.io/badge/Built%20With-Terraform-blueviolet?style=for-the-badge)](https://www.terraform.io/) [![Ansible](https://img.shields.io/badge/Built%20With-Ansible-red?style=for-the-badge)](https://www.ansible.com/)
[![AWS](https://img.shields.io/badge/Built%20With-AWS-orange?style=for-the-badge)](https://aws.amazon.com/)

## Part 2 and 3 - Ansible and AWS Configuration
## Prerequisites:
 - All the Prerequisites from Part 1 and:
 - Linux environment with Ansible installed
 - Access to key pairs for EC2 Instances
 - Straight SSH access

The first step is to clone and enter the github repository:

`git clone https://github.com/moonbeam87/terraform-job-ansible.git`

`cd terraform-job-ansible`

After cloning the repo, the next step you want to take is to establish ssh access to your EC2 Instance. After connecting, run:

`aws configure`

and fill in all the fields. After that you can exit the ssh session. Your next step will be to configure ansible to connect to an EC2 Instance.

Open your ansible hosts file as root so you can edit it. You can do this with this command:

`sudo nano /etc/ansible/hosts`

Then, make a new group called AWS, and add the EC2 Instance. You can add this section to the end of the hosts file:

~~~

[AWS]

ec2-instance ansible_host=[YOUR IP GOES HERE] ansible_user=[USERNAME] ansible_ssh_private_key_file=[PATH TO KEY]

~~~

After adding that, you can test your Ansible config by running the following command:

`ansbile -m ping all`

This should check all of your ansible instances, and should return ping-pong from all of the EC2 instances.

The next step you shoud take is to run the playbook:

`ansible-playbook nginx.yml`

This will run the playbook on the EC2 Instance, and you should be good to go. ***Don't forget to look through all the files to enter in the proper ARNs, file paths, variables, etc. The nginx config has an SSL part that's commented out, you will have to put in your variables there as well***
