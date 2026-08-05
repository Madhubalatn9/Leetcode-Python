from typing import List
class list:
    def update_list(self,arr:List[int]):
        arr[1]=55
        print("updated_list",arr)
    def append(self,arr:List[int],value:int):
         last_insert=arr+[value]
         print("last_insert:",last_insert)
    def insert(self,arr:List[int],value:int,insert_pos:int):
          n=len(arr)
          new_list=[None]*(n+1)
          j=0
          for i in range(n+1):
            if(i==insert_pos):
                new_list[i]=value
            else:
                new_list[i]=arr[j]
                j=j+1
          print("insertion:",new_list)
        

    def search(self, arr: List[int], search_value: int):
        n = len(arr)

        for i in range(n):
            if arr[i] == search_value:
                return i

        return -1
                
    def sort(self,arr:List[int]):
          n=len(arr)
          for i in range(n-1):
            for j in range(0,n-i-1):
               if(arr[j]>arr[j+1]):
                   arr[j],arr[j+1]=arr[j+1],arr[j]
                  
              
          return arr               
l1=list()
l1.update_list([56,9,76,89])
l1.append([5,67,89,65],7)
l1.insert([5,6,7,8,9],10,3)
l1.search([3,4,5,6],5)
print(l1.search([3,4,5,6],5))
print(l1.sort([4,1,3,9,7]))