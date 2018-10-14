Fuente: http://tipsonubuntu.com/2016/07/31/install-oracle-java-8-9-ubuntu-16-04-linux-mint-18/

1. Add the PPA
sudo add-apt-repository ppa:webupd8team/java

2. Update and install the installer script:
sudo apt update; sudo apt install oracle-java8-installer

3. Check the Java version
javac -version

4. Set Java environment variables
sudo apt install oracle-java8-set-default
