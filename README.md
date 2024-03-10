# automatic-email-in-case-of-inactivity-for-bitcoin-inheritance
This is a python script that send e-mails to someone if you do not access a script for a certain time

What do you need?
1) A computer or cloud based machine that will continue running, at lest 1 year, after you died
2) A gmail with inactive desativation at least 1 year ( or access an e-mail from someone that you believes stay alive after you go )
3) Previously send 3 files (will, seeds e passphrase) that only opens with the password that script will send due your inactivity

How to use (Windows 10 64bits - Feel free to update the scripts for Linux version):
1) Download this repository, go to venv folder and extract "here" venv.zip file then go back to previous folder
2) Configure the email_sender.py file with your login to gmail (you will need enable 2FA autentication and create a new pass to a new app in gmail configuration)
   Read this article https://support.google.com/accounts/answer/185833?visit_id=638455376385662495-127977219&p=InvalidSecondFactor&rd=1
3) Configure IsManAlive.py file with your e-mail, the e-mail to someone you want the deliver the messages and the messages itself
4) Create a cron job with Task Scheduler to run run_me.bat file every day
5) Run hit_me.bat script every day ou closest you can. You can create a shortcut to your desktop
   
