from crud import *
def operation(self):
    while(True):
        print('press 1 for insert')
        print('press 2 for update')
        print('press 3 for delete')
        print('press 4 for fetch')
        try:
            ch=int(input('enter ch'))
            if ch==1:
                 db.insert()
        except Exception as e:
                print('error')
    
db=DB()
 
