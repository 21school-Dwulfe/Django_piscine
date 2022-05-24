from elem import Elem, Text
from elements import *

class Page():
    def __init__(self, instance:Elem) -> None:
        if not isinstance(instance, Elem):
            raise Elem.ElementIncorrect("Uknown type")
        self.instance = instance

    def __str__(self) -> str:
        result = ''
        if type(self.instance) == Html:
            result += "<!DOCTYPE html>\n"
        result += self.instance.__str__()
        return (result)

    def __check_elem(self, el:Elem) -> bool:
        if not isinstance(el, (Html, Head, Body,
            Title, Meta, Img, Table, Th, Tr, Td,
            Ul, Ol, Li, H1, H2, P, Div, Span, Hr, Br, Text)):
            raise Elem.ElementIncorrect("Unknown type")
        if type(el) == Text:
            return (True)
        if type(el) == Meta and len(el.content) == 0:
            return (True)
        if type(el) == Html and len(el.content) == 2\
            and type(el.content[0])  == Head and type(el.content[1]) == Body:
            if all(self.__check_elem(item) for item in el.content): 
                return (True)
        elif type(el) == Head and [type(item) == Title for item in el.content].count(True) == 1:
            return (True)
        elif type(el) == Div or type(el) == Body\
            and all([isinstance(item, (H1, H2, Div, Table, Ul, Ol, Span, Text)) for item in el.content]):
            return (True)
        elif isinstance(el, (Title, H1, H2, Li, Li, Th, Td)) and\
            len(el.content) == 1 and type(el.content[0]) == Text:
            return (True)
        elif type(el) == P and (el.content == 1 and type(el.content[0]) == Text):
            return (True)
        elif type(el) == Span and all([isinstance(item, (P, Text)) for item in el.content]):
            if all(self.__check_elem(item) for item in el.content):
                return (True)
        
        elif type(el) == Ul or type(el) == Ol and all([type(item) == Li for item in el.content]):
            if (len(el.content) > 0 and all(self.__check_elem(it) for it in el.content)):
                return (True)
        elif type(el) == Tr and len(el.content) > 0 and \
            all([isinstance(item, (Th, Td)) for item in el.content]) and\
            all([type(el.content[0]) == type(item) for item in el.content]) and\
            all([self.__check_elem(item) for item in el.content]):
                return (True)
        elif type(el) == Table and all([type(item) == Tr for item in el.content]) and\
            all([self.__check_elem(item) for item in el.content]):
            return (True)
        return False

    def is_value(self) -> bool:
        return (self.__check_elem(self.instance))
    
    def write_to_file(self, file_name:str) -> None:
        with open(file_name, 'w') as file:
            file.write(self.__str__())


if __name__ == '__main__':

    err_out = open("error.log",'a')
    success_out = open ('success.log', 'a')       

    try:
        wrong = Page("jo..")
        print(wrong)
    except Exception as e:
        print('case: Page("jo..")')
        print(e)

    try:
        right = Page(None)
        print(right.is_value())
    except Exception as e:
        print('case: Page(None)')
        print(e)
    
    available = (Html, Head, Body,
        Title, Meta, Img, Table, Th, Tr, Td,
        Ul, Ol, Li, H1, H2, P, Div, Span, Hr, Br, Text)
    count = 0

    def ran(count):
        count += 1
        if count % 2 == 0:
            return Td
        else:
            return Th

    configurator = {
        Html : [Head, Body],
        Head : [Title],
        Body : [H1, H2, Div, Table, Ul, Ol, Span, Text],
        Title : [Text],
        Meta: [None],
        Img: [None],
        Table: [Tr],
        Th: [Text],
        Tr: [ran(count)],
        Td: [Text],
        Ul: [Li],
        Ol: [Li],
        Li: [Text],
        H1: [Text],
        H2: [Text],
        P: [Text],
        Div : [H1, H2, Div, Table, Ul, Ol, Span, Text],
        Span:[Text],
        Hr:[None],
        Br:[None]
    }

    def generator(el:Elem) -> None:
        if len(el.content) == 0:
            el.add_content([item() if item != Text else Text('Default')\
                for item in configurator[type(el)]  if item != None])
        # print(el)
        for it in el.content:
            if type(it) is not Text:
                if type(el) == Div or type(el) == Body and type(it) == Div:
                    it.add_content(Text('Default'))
                else:
                    generator(it)

    def success(item_type) -> None:
        str_res= "Case: Page({})".format(item_type)
        state = "Format is correct!"
        print(str_res)
        print(state)
        success_out.write("{0}\t{1}\n{2}\n\n\n".format(str_res, state, str(p)))

    def error(item_type):
        str_res= "Case: Page({})".format(item_type)
        state = "Error format"
        print(str_res)
        print(state)
        err_out.write("{0}\t{1}\n{2}\n\n\n".format(str_res, state, str(p)))
    

    print("==============HTML================")
    ing = Html()
    generator(ing)
    page = Page(ing)
    print(page.is_value())
    page.write_to_file("to_file")
    print(page)

    print("==============DIV================")
    d = Div()
    generator(d)
    n = Page(d)
    n.write_to_file("div")
    copy_instances = []
    print(d)


    #copy instances full of content
    for key in configurator:
        item = key()
        print(key)
        generator(item)
        copy_instances.append(item)
    
    for key in configurator:
        i = 0
        
        for copy in configurator:
            item:Elem = key()
            content = copy_instances[i]
            i += 1
            item.add_content(content)
            p = Page(item)
            result = p.is_value()
            if result:
                success(type(item))
            else:
                error(item)
            print(p)
      
    err_out.close()
    success_out.close()