import csv

def read_data_from_csv(filename):
    fd=open(filename)
    fdata=csv.reader(fd)
    data_list=[]
    for row in fdata:
        #print(row)
        data_list.append(row)
        #print(data_list)
        temp=0
        
        for i in range(0,len(data_list)):
            for j in range(i+1,len(data_list)):
                if(data_list[i][0]>data_list[j][0]):
                    temp=data_list[i]
                    data_list[i]=data_list[j]
                    data_list[j]=temp
    print(data_list)
                    
	
	
	
	
	
	
	
	
	
def main():
	filename="data.csv"
	read_data_from_csv(filename)
	
if __name__=='__main__':
	main()
