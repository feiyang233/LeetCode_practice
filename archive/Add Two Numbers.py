'''
def lengthOfLongestSubstring(s):
	L=len(s)
	dic={}
	l=[]
	count=0
	for i in range(L-1):
		if s[i]==s[i+1]:
			l.append(i)
			count=0
		else:
			count+=1
	l.append(L-1)
	l.insert(0,0)
	index=0
	for i in l:
		dic[i]=l[index+1]-l[index]
		index+=1
		if index==len(l)-1:
			break
	print(dic)
	L1=[]
	L2=[]
	for i,j in dic.items():
		L1.append(i)
		L2.append(j)
	M=max(L2)
	#b=L1[L2.index(M)]
	#return s[b+1:b+M+1]
	return M
a='abcabcbb'
k=lengthOfLongestSubstring(a)
print(k)
'''
def lengthOfLongestSubstring(s):
    max_length = 0
    start = 0   # Start index of the substring without repeating characters
    end = 0     # End index of the substring without repeating characters
    char_dict = {}

    for index in range(len(s)):
        char = s[index]
        # Find out a repeating character. So reset start and end.
        if char in char_dict and start <= char_dict[char] <= end:
            start = char_dict[char] + 1
            end = index
        # char is not in the substring already, add it to the substring.
        else:
            end = index
            if end - start + 1 > max_length:
                max_length = end - start + 1
        char_dict[char] = index
        #print(char_dict)
        #print(start,end)
    return max_length
a='abcabcbb'
k=lengthOfLongestSubstring(a)
print(k)