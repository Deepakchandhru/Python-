def most_frequent(a):
      f={}
      for i in range(len(a)):
      	f[a[i]]=f.get(a[i],0)+1
      for j in range(len(f)):
      	l=max(f,key=f.get)
      	print(l,":",f[l])
      	f.pop(l,f[l])   	
most_frequent(input("Enter word:"))  
