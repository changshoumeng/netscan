
import sys
import site
import platform


LOCAL_IP="192.168.18.29"



def get_python_envinfo():
    s = "sitepackages:" + str(site.getsitepackages())
    s += "\nsys.version:" + sys.version
    s += "\nplatform:" + platform.platform()
    s += "\nsys.platform:" + sys.platform
    if sys.platform != 'win32':
        s += "\n" + get_host_info()
    return s


def is_win32():
    return sys.platform == 'win32'


def get_host_info():
    import socket
    myname = socket.getfqdn(socket.gethostname())
    myaddr = socket.gethostbyname(myname)
    s = "hostname:{0} ip:{1}".format(myname, myaddr)
    return s


if __name__ == '__main__':
    print(get_python_envinfo())
