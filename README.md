# Kazakh Open Source -- Development of a module for information and analytical data analysis of text resources and documents of the Kazakh language based on machine learning
* **System Requirements** 
  * OS: Linux
  * Database: mysql > 5.0
  * Apertium: version > 3.6
  * CPU: core >4; RAM > 8GB; 
  * GPU: intel hd graphics or minimal or minimal graphics accelerator
  * Interpreter: Python > 3.6.8 
* **Installation**
  * mysql: https://dev.mysql.com/downloads/mysql/ or using terminal command
    * sudo apt-get install mysql-server mysql-client
    * sudo mysql_secure_installation
     * Enter current password for root (enter for none): Press Enter
     * Set root password? [Y/n] y Enter Y to set root password
     * New password: enter your password but it will not be visible
     * Re-enter new password: enter your password but it will not be visible
     * Next, you can press Enter to answer all remaining questions
    * creating database searchengine and importing database
     * Global database for backup link:  https://yadi.sk/d/XHNCEjSadhCaJg downloading and paste to $HOME or /home/\<username\> directory and
     * use terminal
      * cd $HOME
      * sed -i backup22102020.sql -e 's/utf8mb4_unicode_ci/utf8mb4_general_ci/g'
      * sed -i backup22102020.sql -e 's/utf8mb4_0900_ai_ci/utf8mb4_general_ci/g'
     * mysql -u root -p
     * enter your password
     * > CREATE DATABASE searchengine CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci
     * > exit;
     * mysql -u root -p searchengine < backup22102020.sql
     * Enter your root password from mysql and wait to finish
  * apertium: use terminal:
      * mkdir $HOME/sources
      * cd $HOME/sources
      * wget http://apertium.projectjj.com/apt/install-nightly.sh
      * sudo bash install-nightly.sh
      * sudo apt-get -f install locales build-essential automake subversion pkg-config gawk libtool apertium-all-dev
      * Then execute all the commands on the link: https://wiki.apertium.org/wiki/Kazakh_and_Russian
  * Cloning project: use terminal:
      * cd $HOME
      * git clone https://github.com/Abilay99/KazOpenCorpora.git
  * python packages: use terminal:
      * cd $HOME/KazOpenCorpora 
      * pip install -r requirements.txt 
* **Test**
  * Inserting *.txt files to directory **testbasictexts**
  * use terminal: python3 zzgotokeywordsplaintext.py
  * see directory testKeywords
  * use terminal: python3 interface0.0.1.py
