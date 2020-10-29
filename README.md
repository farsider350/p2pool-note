**P2pool installation with pypy -- Windows**


On Windows, pypy is only supported via the Windows Subsystem for Linux (WSL). P2pool on pypy on WSL is much faster than P2pool on
CPython on native Windows. To install WSL, first follow the steps outlined here:


https://msdn.microsoft.com/en-us/commandline/wsl/install_guide


Once you've done that, run bash and follow the rest of the steps below.


**P2pool installation with pypy -- Linux and Windows**


Copy and paste the following commands into a bash shell in order to install p2pool on Windows or Linux.

>sudo apt-get update

>sudo apt-get install pypy pypy-dev pypy-setuptools gcc build-essential git


>wget https://bootstrap.pypa.io/ez_setup.py -O - | sudo pypy
>sudo rm setuptools-*.zip


>wget https://pypi.python.org/packages/source/z/zope.interface/zope.interface-4.1.3.tar.gz#md5=9ae3d24c0c7415deb249dd1a132f0f79
tar zxf zope.interface-4.1.3.tar.gz

>cd zope.interface-4.1.3/

>sudo pypy setup.py install

>cd ..

>sudo rm -r zope.interface-4.1.3*


>wget https://pypi.python.org/packages/source/T/Twisted/Twisted-15.4.0.tar.bz2

>tar jxf Twisted-15.4.0.tar.bz2

>cd Twisted-15.4.0

>sudo pypy setup.py install

>cd ..

>sudo rm -r Twisted-15.4.0*


>git clone https://github.com/farsider350/p2pool-note.git

>cd p2pool-note


You'll also need to install and run your noted and edit ~/.note/note.conf) with your RPC username and password. Once it's finished downloading blocks and syncing, go to your p2pool directory and run


>pypy run_p2pool.py --net note


**Merged Mining**

>pypy p2pool.py --net note --merged http://dogerpcuser:rpcpass@127.0.0.1:7332

POW coins can be added on top of each other so run as many as your cpu and ram will handle.

>pypy p2pool.py --net note --merged http://doge:pass@127.0.0.1:7332 --merged http://via:pass@127.0.0.1:5222 --merged http://artiqox:pass@127.0.0.1:19421 --merged http://myriad:pass@127.0.0.1:10889 --merged http://argentum:pass@127.0.0.1:13581


**Miner setup**


P2pool communicates with miners via the stratum protocol. For BTC, configure your miners with the following information:


>URL: stratum+tcp://(Your node's IP address or hostname):4545

>Worker: (Your note address)

>Password: x


If you wish to modify the mining difficulty, you may add something like "address+4096" after your mining address to set the pseudoshare difficulty to 4096, or "address/65536" to set the actual share difficulty to 65536 or the p2pool minimum share difficulty, whichever is higher. Pseudoshares only affect hashrate statistics, whereas actual shares affect revenue variance and efficiency.


**Firewall considerations**


If your node is behind a firewall or behind NAT (i.e. on a private IP address), you may want to forward ports to your p2pool server. P2pool uses two ports: one for p2p communication with the p2pool network, and another for both the web UI and for stratum communication with workers. For Note Blockchain, they are 4544 (p2p) and 4545 (stratum/web).
