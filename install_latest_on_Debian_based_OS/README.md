# Debian Python3 , install last stable
install last stable of Python3 for Debian. Python-3.7.4 at time of writing.

## Download last stable version of Python3 to /home/<usr>/temp

* [Python3] - Python homepage where you find the latest stable version 


## unpack the file
    #tar -xf Python-3.7.4.tar.xz

## install  
    #cd Python-3.7.4
    #./configure --enable-optimizations
    #nproc    => number of kernels. 8 at my laptop.
    #make -j 8
    #sudo make install       or sudo make altinstall  if you like to keep the old one
    
## test
    #python3.7 --version
        Python 3.7.4
    
    #python3
        Python 3.7.4
    
## install pip3
    #sudo apt-get install python3-pip
    

Have fun !

created by tsterber



[Python3]:<https://www.python.org>
    
