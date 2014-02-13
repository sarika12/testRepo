'''it will print line no before every line'''

import sys
def write_line_no(fname):
       
    with open(fname, 'r') as f:
        data=f.readlines()
        for index,line in enumerate(data):
            i=index+1
            data[i-1]=str(i)+". " + data[i-1]
   
    with open(fname, 'w') as f:
        f.writelines(data)

if __name__=='__main__':
    write_line_no(sys.argv[1])





