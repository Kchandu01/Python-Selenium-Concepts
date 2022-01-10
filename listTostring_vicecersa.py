#########################  string To list ########################################
strr = "this is very good testing"
# need output = ['this', 'is', 'very', 'good', 'testing']

strr2 = []
for i in strr:
    strr2 = strr.split(' ')

print(strr2)

##########################   list to string #######################################
str3 = ['this', 'is', 'very', 'good', 'testing']
# Need output = this is very good testing

str4 = ''
for word in str3:

    str4 = str4 + ' ' + word

print(str4)