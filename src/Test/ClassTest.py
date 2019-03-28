from newFolder import testImport as ti


class Text:

    def __init__(self, inData):
        self.value = inData

    def join(self, _list):
        data = ""
        for e in _list:
          data += e + self.value  
        
        return data


t = Text(",")
ret = t.join(["1","2"])
print(ret)


here = ti.test()
here.printThis()

