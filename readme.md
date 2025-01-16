activate environment:
source task_env/bin/activate

runserver: python3 manage.py runserver

sudo -u postgres psql

Step 1: Remove the Faulty Repository
Open the repository file:


sudo nano /etc/apt/sources.list.d/pgadmin4.list
Replace any reference to victoria with jammy:

deb [signed-by=/usr/share/keyrings/packages-pgadmin-org.gpg] https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/jammy pgadmin4 main
Save and exit the editor:

Press Ctrl+O to save.
Press Ctrl+X to exit.
Step 2: Update and Install pgAdmin
Update the package list:

sudo apt update
Install pgAdmin 4 Desktop:

sudo apt install pgadmin4-desktop -y
Step 3: Launch pgAdmin
Once installed, you can launch pgAdmin from:

The application menu.
By typing the following command in the terminal:

pgadmin4