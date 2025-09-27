import numpy as np 

#Generate synthetic data: a numerical matrix of at least 1000×5 dimensions
rng = np.random.default_rng(42) #the same matrix comes out 
r = rng.normal(0,1,(1000,5))
print (r)

#Normalization
#normalized_dataset = np.array(r)

max_value = r.max()
min_value = r.min()
normalized_dataset = (r-min_value)/(max_value-min_value)
print(normalized_dataset.min(), normalized_dataset.max())

#Thresholding
boolean_mask = r.mean()
thresholding_dataset = r>boolean_mask
# print(boolean_mask)
print(thresholding_dataset)

#Categorical Encoding
bins = [-np.inf, 0, 1, np.inf]  # -∞ - 0, 0-1, 1 +  constraints.
labels = [0, 1, 2]

categorical_dataset = np.digitize(r,bins) -1
print(categorical_dataset)

# categ_dataset = np.digitize(r,bins) # bu sekilde aralik 1,2,3 döndürüyor ancak -1 ekleyince 0,1,2 oluyor.
# print(categ_dataset)

#---Arrays---

s = np.array([1,2,3,4,5])
k = np.array([[[5,10,15],[3,6,9],[2,4,6]]])

print("s", s, "ndim:", s.ndim, "shape:", s.shape, "dtype:", s.dtype) #shape: (5,): 1 boyutlu
print("k",k, "ndim:", k.ndim, "shape:" , k.shape, "dtype:" , k.dtype) #shape: (1, 3, 3): 1 tane 3x3 matris

a = np.arange(0,5,2) #independet part arange only depends on its (start, stop, step) values, it doesn’t use other arrays such as s,k.
b = np.linspace(0,2,6)
z = np.zeros((3,3))
o = np.ones((4,3))
i = np.eye(2,2)
print(a,"\n", b, "\n",z, "\n", o, "\n", i)

###----TRANSACTIONS----
#Boolen Indexleme
#1.
zd = np.array([[3,4],[2,3]])#2D
dd = np.array([[[3,2],[1,4],[2,5]]])#3D
print(zd[zd%2 == 0])
print(dd[dd%3 == 0])
#2.
rng_a = np.random.default_rng(42) #the same matrix comes out 
e = rng_a.uniform(0,30,(2,3)) #0-30 random numbers.  rng.integers: integer 2 Ndim
print(e)
print(e[e%2 != 0])

rng_b = np.random.default_rng(42) #the same matrix comes out 
g = rng_b.uniform(0,30,(2,1,3)) #3D
print(g)
print(g[g%2 != 0])
##As Ahmet Hoca did
bi = np.arange(1,13).reshape(3,4) #2D
print(bi[bi%2 == 0])

di = np.arange(1,13).reshape(3,1,4) #3D
print(di)
print(di[di%3==0])

#Slicing
sz = np.arange(1,21).reshape(4,5)  #2D
print(sz)
print(sz[0,0]) #first element
print(sz[:,1]) #all rows 2. columns 
print(sz[1,:2]) #2. row 0 and 1.,2. columns
print(sz.T) # transpoz
print(sz[1:3, 3:6]) #1.,2. rows and 4.,5. columns 

sd = np.arange(1,21).reshape(2,2,5) #3D
print(sd)
print(sd[0]) #the entire first block
print(sd[:,:,2]) #all rows 3. columns index olarak
print(sd[1,1,:]) #2. block, 2. rows


# Fency Indexleme


# arr = np.array([10,20,30,40,50])
# idx = [0,2,4]
# print(zd[idx])

#Brodcasting
# A = np.ones((3,4))
# b = np.array([1,2,3,4])
# print(A+b)