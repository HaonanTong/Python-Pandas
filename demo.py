import os
import sys
import pandas as pd
import matlab.engine as matEng

# python demo.py ~/Desktop/ 

argIn=sys.argv[1]


def main():
	print argIn
	for file in os.listdir(argIn):
	# for subdir,dir,files in os.walk(argIn):
		# print files
			# file='~/Desktop/kat-rpkm-expression.csv'
			# fPath=os.path.join(argIn,file) 
			# print fPath
		if file.endswith('.csv'):
			print 'hello'
			# df=pd.read_csv(file,usecols=[0,1,2,3],index_col=0)
			# df['avg1']=df.mean(axis=1)
			df=pd.read_csv(file,index_col=0)
			colnames=list(df)
			# df['avg1']=df['kat_1_1','kat_2_1','kat_3_1']
			df['avg1']=df.iloc[:,[0,1,2]].mean(axis=1)

			grp1=df['avg1']
			# grp1.to_csv('avg.csv')

			avg1=grp1.tolist()
			print avg1
			# matlab function
			# sum(a,b)
			matAvg1=matEng.double(avg1)
			# sum1=matEng.sum(avg1,avg2)
			# print df
						 # fetch data
					  # matlab func
					   # savecsv

if __name__ == '__main__':
	main()
