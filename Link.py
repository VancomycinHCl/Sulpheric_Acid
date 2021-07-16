import ctypes


class link():
    def __init__(self):
        self.prev = None#上一跳地址
        self.data = None#数据
        self.next = None#下一跳地址

    def add_node(self,p_node):#添加节点
        if p_node.next == None:#从最后一条节点开始续写
            self.prev = id(p_node)#本节点上一跳地址=上一节点指针
            p_node.next = id(self)#上一节点的下一跳地址=本节点指针
        else:#插入
            temperVar = p_node.next#临时存数的一个变量，存放上一个节点的原下一跳地址
            p_node.next = id(self)#规定上一节点的下一跳地址为本节点地址
            self.prev = id(p_node)#规定上一跳的地址
            n_node = ctypes.cast(temperVar, ctypes.py_object).value#从临时变量里恢复原先的下一跳
            n_node.prev = id(self)#修改原先下一个节点上一跳地址
            self.next =id(n_node)
            del temperVar
            del n_node
            del p_node

    def kill_node(self):
        if (self.prev==None) & (self.next==None) == True:
            n_node = ctypes.cast(self.next, ctypes.py_object).value
            p_node = ctypes.cast(self.prev, ctypes.py_object).value
            n_node.prev = id(p_node)
            p_node.next = id(n_node)
            del n_node
            del p_node
        elif self.prev == None:
            n_node = ctypes.cast(self.next, ctypes.py_object).value
            n_node.prev = None
            del n_node
        else:
            p_node = ctypes.cast(self.prev, ctypes.py_object).value
            p_node.next = None
            del p_node

    def count_element(self):
        self.count = 1
        if (self.prev != None) & (self.next != None) == True:
            self.count += 2
            n_node = ctypes.cast(self.next, ctypes.py_object).value
            p_node = ctypes.cast(self.prev, ctypes.py_object).value
            while (n_node.next != None):
                self.count += 1
                n_node = ctypes.cast(n_node.next, ctypes.py_object).value
            while (p_node.prev != None):
                self.count += 1
                n_node = ctypes.cast(n_node.prev, ctypes.py_object).value
        elif self.prev == None:
            self.count += 1
            n_node = ctypes.cast(self.next, ctypes.py_object).value
            while (n_node.next != None):
                self.count += 1
                n_node = ctypes.cast(n_node.next, ctypes.py_object).value
        elif self.next == None:
            self.count += 1
            p_node = ctypes.cast(self.prev, ctypes.py_object).value
            while (p_node.prev != None):
                self.count += 1
                p_node = ctypes.cast(p_node.prev, ctypes.py_object).value

        print(self.count)



    #def __del__(self):
        #del self
        #print("killed!")

if __name__ == "__main__":
    a = link()
    a.data = 0

    b = link()
    b.data = 0
    b.add_node(a)

    d = link()
    d.data = 0
    d.add_node(b)
    #d.kill_node()

    c = link()
    c.data = 0
    c.add_node(b)
    e = link()
    e.data = 0
    e.add_node(d)
    #d.kill_node()

    print("pre_a ",a.prev)
    print("next_a",a.next)
    print(id(a))
    print("pre_b ",b.prev)
    print("next_b",b.next)
    print(id(b))
    print("pre_c ",c.prev)
    print("next_c",c.next)
    print(id(c))
    print("pre_d ",d.prev)
    print("next_d",d.next)
    print(id(d))
    b.count_element()