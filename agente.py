import time
import mysql.connector
from subprocess import PIPE, run

def procesador(command):
    result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
    return result.stdout

def procesos(command):
    result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
    return result.stdout

def usuarios(command):
    result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
    return result.stdout

def so(command):
    result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
    return result.stdout

def kernel(command):
    result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
    return result.stdout

def ip(command):
    result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
    return result.stdout


salida_procesador = procesador("cat /proc/cpuinfo | grep 'model name' | uniq")
salida_procesos = procesos("ps -o command")
salida_usuarios = usuarios("users")
salida_so = so("cat /etc/issue.net")
salida_kernel = kernel("uname -r")
salida_ip = ip("ip -4 a show enp2s0 | grep -Po 'inet \K[0-9.]*'")

print (salida_procesador)
print (salida_procesos)
print (salida_usuarios)
print (salida_so)
print (salida_kernel)
print (salida_ip)


print (type(salida_procesador))
print (type(salida_procesos))
print (type(salida_usuarios))
print (type(salida_so))
print (type(salida_kernel))
print (type(salida_ip))


timestr = time.strftime("%Y%m%d")
print (timestr)


archivo = open(salida_ip+"_"+timestr+".csv","w")

archivo.write(salida_procesador)
archivo.write(",")
archivo.write(salida_procesos)
archivo.write(",")
archivo.write(salida_usuarios)
archivo.write(",")
archivo.write(salida_so)
archivo.write(",")
archivo.write(salida_kernel)


archivo.close()


conexion1=mysql.connector.connect(host="192.168.100.60", 
                                  user="wpuser", 
                                  passwd="1270130", 
                                  database="compliance_server")
cursor1=conexion1.cursor()
sql="insert into tabla_servidores(ip, procesador, procesos, usuarios, so, kernel ) values (%s,%s,%s,%s,%s,%s)"
datos=(salida_ip, salida_procesador, salida_procesos, salida_usuarios, salida_so, salida_kernel )
cursor1.execute(sql, datos)
conexion1.commit()
conexion1.close() 





