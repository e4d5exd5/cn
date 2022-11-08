import time, socket, sys

s = socket.socket()

port = 1234
s.bind(("", port))


def add(arr):
  arr = arr[2::]
  sol = 0;
  for i in range(len(arr)):
    sol = sol + int(arr[i])
  
  return sol
def mul(arr):
  arr = arr[2::]
  sol = 1;
  for i in range(len(arr)):
    sol = sol * int(arr[i])
  
  return sol
  

def div(arr):
  arr = arr[2::]
  sol = int(arr[0])
  
  if(arr[0] == '0'):
    return 0
  
  if(arr[1] == '0'):
    return "Error"
  arr = arr[1::]
  for i in range(len(arr)):
    sol = sol / int(arr[i])
  
  return sol

def sub(arr):
  arr = arr[2::]
  sol = int(arr[0])
  arr = arr[1::]
  for i in range(len(arr)):
    sol = sol - int(arr[i])
  
  return sol


s.listen(1)
print("\nWaiting for incoming connections...\n")
conn, addr = s.accept()
print("Received connection from ", addr[0], "(", addr[1], ")\n")



while True:
    inp = conn.recv(1024)
    inp = inp.decode()
    arr = inp.split(' ')
    if(arr[0] == 'calc'):

        if(arr[1] == 'add'):
            sol = str(add(arr))
        elif(arr[1] == 'sub'):
            sol = str(sub(arr))
        elif(arr[1] == 'mul'):
            sol = str(mul(arr))
        elif(arr[1] == 'div'):
            sol = str(div(arr))
        else:
            sol = "Invalid Inputs"
            
        print(inp, " ", sol)
        conn.send(sol.encode())
    else:
      print(inp)
      conn.send(inp.encode())