from stack import Stack
from node_nerf import Node

if __name__ == "__main__":

    #print("creating head of list")
    st = Stack()
    print("testing")
    for x in range(4):
        print("making stack block: " + str(x))
        st.push(x)
    #print(st.size)
    #print(str(st.isEmpty))
    print(st)
