import os

print(os.path.join('usr', 'bin'))
print(os.path.sep)

hellofile = open('./hello.txt')
hello_content = hellofile.read()
print(type(hello_content))

sonnetfile = open('./sonnet29.txt')

sonnet_content = sonnetfile.readlines()

print(hellofile.read())
print(sonnet_content)

hellofile.close()
sonnetfile.close()
