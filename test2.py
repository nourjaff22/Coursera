import subprocess
import json
import shlex

def main():
    arg1 = "17.9259123865229"
    arg2 = "1.64222598694351"
    arg3 = "1.43713887097528"
    arg4 = "0.0651395682880492"
    arg5 = "0.0838684197680972"
    arg6 = "0.415294101652516"
    arg7 = "-0.0611142195900331"
    arg8 = "3"
    arg9 = "1.5"
    input_list = [shlex.quote(arg) for arg in [arg1,arg2,arg3,arg4,arg5,arg6,arg7,arg8,arg9]]
    process = subprocess.Popen(["/home/ubuntu/model/test/dist/Kmeans_test2"] + input_list,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if(stdout):
        result = stdout.decode('utf-8')
        print(result.split())
    if(stderr):
        print('Error: ' + stderr.decode('utf-8'))

main()
