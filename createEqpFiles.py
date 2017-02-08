import os
import os.path

# this folder is custom
rootdir = "D:\\新建文件夹 (2)\\SSData04\\"
savedir = "D:\\新建文件夹 (2)\\Saves\\"

#print(

#print(os.path.abspath(os.path.join(rootdir, os.pardir, os.pardir)))

#print(os.path.relpath(rootdir))


#aa = os.path.dirname(rootdir)
#Months=os.listdir(aa)   #年月
#for dir1 in Months:
 #   print(dir1)

def text_create(name):

    full_path = savedir + name + '.txt'
    if os.path.isfile(full_path) == False:
        file = open(full_path,'w')
        file.close()

def writetimes(name,text):
    full_path = savedir + name + '.txt'
    file_object = open(full_path, 'a')
    file_object.write(text)
    file_object.write('\n')
    file_object.close()


'''
Dates = os.listdir(rootdir)
for path in Months: #年月
    print(rootdir+path)

'''
for parent, dirnames, filenames in os.walk(rootdir):
    for filename in filenames:
        if  os.path.splitext(filename)[1] != '.EC1':
            continue
        eqpid = parent.split('\\')[-1]
        Date = parent.split('\\')[-2]
        months = parent.split('\\')[-3]
        print(parent)
        text_create(eqpid)  #创建text文件
        time = '{0}-{1}-{2} {3}:{4}:{5}'.format(months[0:4],months[4:6],Date,filename[0:2],filename[2:4],filename[4:6])
        writetimes(eqpid, time)

