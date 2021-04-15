def standard_arg(arg):
    print(arg)

def pos_only_arg(arg,/):
    print(arg)

def kwd_only_arg(*,arg):
    print(arg)

def combined_example(pos_only,/,standard,*,kwd_only):
    print(pos_only,standard,kwd_only)

standard_arg(10)
standard_arg(arg=11)

pos_only_arg(20)
#pos_only_arg(arg=21) parameter sesudah pemberian tanda / tidak boleh memberikan nama parameter

#kwd_only_arg(30) paramatere sesudah tanda * artinya harus memberikan nama parameter
kwd_only_arg(arg=31) 

combined_example(40,50,kwd_only=60) #pos_only tidak boleh memberikan nama parameter, standard boleh memberikan nama parameter 
combined_example(70,standard=80,kwd_only=100)
#combined_example(70,20,50)
#combined_example(pos_only= 70,standard=80,kwd_only=100)