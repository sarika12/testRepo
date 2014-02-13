'''it will print total charrecher in every line'''
import sys
def write_line_no(fname):
       
    with open(fname, 'r') as f:
        data=f.readlines()
        for index,line in enumerate(data):
            l1=line           
            p=l1.index('\n')
            l1=l1[:p]+' '+str(p)+l1[p+2:]
            if(index+1==len(data)):
                data[index]=l1
            else:
                data[index]=l1+'\n'
   
    with open(fname, 'w') as f:
        f.writelines(data)

if __name__=='__main__':
    write_line_no(sys.argv[1])
