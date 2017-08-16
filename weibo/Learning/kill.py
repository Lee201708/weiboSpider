import json

r = open('../../json/mweibocom.json',encoding='utf-8')
# line = r.read()
# line= line.strip(',\n')
# line ='[' +line + ']'

# print(line)
# print(type(line))

dic = json.load(r)
print(dic)






# line= json.load(line)
# print(line[0]['ID'])
#
#
# line = '['+line+']'
# print(type(line))
# line =dict(line)
# print(line)
# di = eval(line)
# print(type(di))
# di = dict(line)
# print(id)
# print(line)

# print(line)
# print(len(line))
# print(line[3]["ID"])



