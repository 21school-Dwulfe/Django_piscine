#!/usr/bin/python3

class Text(str):
    def __str__(self):
        return super().__str__().replace('\n', '\n<br />\n')

class Elem:
   
    class ElementIncorrect(Exception):
        def __init__(self, reason: str = '') -> None:
            super().__init__("ElementIncorrect: {reason}".format(reason=reason))

    def __init__(self, tag:str=None, attr:dict = None, content:list = None, tag_type:str = None) -> None:
        if tag is None: self.tag = 'div'
        elif type(tag) is not str:
            raise self.ElementIncorrect("tag must be a string") 
        else: self.tag = tag
        if attr is None: self.attr = {}
        elif type(attr) is not dict:
            raise self.ElementIncorrect("attr must be a dictionary") 
        else: self.attr = attr
        if content is None: self.content = []
        elif type(content) is not list:
            self.content = [content]
        else:
            self.content = content
        if tag_type is None: self.tag_type = 'double'
        else: self.tag_type = tag_type
        if self.tag_type != 'double' and self.tag_type != 'simple':
            raise self.ElementIncorrect('Available tag types: double, simple')      

    def __str__(self) -> str:
        result = ''
        if self.tag_type == 'double':
            result = "<{tag}{attr}>{content}</{close_tag}>".format(
                tag=self.tag,
                attr=self.__make_attr(),
                content=self.__make_content(),
                close_tag=self.tag
            )
        elif self.tag_type == 'simple':
            result = "<{tag}{attr}/>".format(
                tag=self.tag,
                attr=self.__make_attr()               
            )
        return result

    def __make_attr(self) -> str:
        result = ''
        for pair in sorted(self.attr.items()):
            result += ' ' + str(pair[0]) + '="' + str(pair[1]) + '"'
        return result

    def __make_content(self) -> str:
        result = '\n'
        if len(self.content) == 0:
            return ""
        for elem in self.content:
            if (len(str(elem)) != 0):
                result += "{elem}\n".format(elem=elem)
        result = "  ".join(line for line in result.splitlines(True))
        if len(result.strip()) == 0:
            return ''
        return result

    def add_content(self, content) -> None:
        if not Elem.check_type(content):
            raise Elem.ValidationError
        if type(content) == list:
            self.content += [elem for elem in content if elem != Text('')]
        elif content != Text(''):
            self.content.append(content)

    @staticmethod
    def check_type(content) -> bool:
        return (isinstance(content, Elem) or type(content) == Text or
                (type(content) == list and all([type(elem) == Text or
                                                isinstance(elem, Elem)
                                                for elem in content])))

def test() -> None:
    title = Elem('title', None, Text('"Hello ground!"'))
    head = Elem('head', None, title)
    h1 = Elem('h1', None, Text('"Oh no, not again!"'))
    img = Elem('img', {'src': 'http://i.imgur.com/pfp3T.jpg'}, None, 'simple')
    body = Elem('body')
    body.add_content([h1, img])
    html = Elem('html')
    html.add_content([head, body])
    print(html)
    html = Elem('html', content=[
                Elem('head', content=Elem(
                    'title', content=Text('"Hello ground!"'))),
                Elem('body', content=[Elem('h1', content=Text('"Oh no, not again!"')),
                                      Elem('img', {'src': 'http://i.imgur.com/pfp3T.jpg'}, tag_type='simple')])])
    with open("result.html", 'w') as output:
        output.write(html.__str__())
    print(html)
    pass

if __name__ == '__main__':
    try:
        test()
    except Exception as e:
        print(e)
