import sys

def parse_line(line: str):
    el = line.replace(" = ", ", ").split(', ')
    result = dict((value.strip().split(":") for value in el[1:]))
    return (el[0],result)

def get_html_index(head, body, scripts):
    template = """<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Periodic Table</title>
    {head}
</head>

<body>
    {body}
    {scripts}
</body>

</html>\n"""
    return (template.format(head=head, body=body, scripts=scripts))

def get_element_tr(name:str, element: dict):
    result = """
            <td class="filled" style="border: 1px solid black">
                <ul>
                    <li>{number}</li>
                    <li>{symbol}</li>
                    <li>
                        <h4>{name}</h4>
                    </li>
                    <li>{molar}</li>
                    <li>{electron}</li>
                </ul>
            </td>"""
    return (result.format(
        name=name,
        number=element['number'],
        symbol=element['small'].strip(),
        molar=element['molar'],
        electron=element['electron']
    ))

def write_in_table(d):
    body = "<table>"
    counter = 0
    td = ""
    for (k, v) in d.items():
        while counter != (int)(v['position']):
                td += "\n\t\t\t<td></td>"
                counter += 1
                #print(counter, (int)(v['position']))
        if v['position'] == (str)(counter):
            td += get_element_tr(k, v)
            counter += 1
        if counter == 18:
            counter = 0
            body += f"\n\t\t<tr>{td}\n\t\t</tr>"
            td = ""
    body+= "\n\t</table>"
    return body

def write_style():
    return ("""
    <style>
        td {
            min-width: 100px;
            padding: 10px;
        }

        ul {
            list-style-type: none;
            margin: 0;
            padding: 0;
        }

        li:nth-child(2) {
            font-size: 42px;
        }

        td.filled:hover {
            cursor: pointer;
            transform: scale(1.015);
            background-color: #ffff99;
        }

        li:last-child {
            font-size: 14px;
        }

        table td.filled {
            background-color: #eee;
        }

        table tr {
            transition: all 1s ease-in-out;
        }

        table tr.slide-out {
            transform: translateX(100%);
        }
    </style>""")

def write_scripts():
    return ("""<script>
        const rows = Array.from(document.querySelectorAll('tr'));

        function slideOut(row) {
            row.classList.add('slide-out');
        }

        function slideIn(row, index) {
            setTimeout(function() {
                row.classList.remove('slide-out');
            }, (index + 5) * 200);
        }
        rows.forEach(slideOut);
        rows.forEach(slideIn);
    </script>""")

def main():
    with open("periodic_table.txt", 'r') as file:
        list = file.readlines()
    d = dict(parse_line(line) for line in list)
    body = write_in_table(d)
    head = write_style()
    script = write_scripts()
    with open("periodic_table.html",'w') as out:
        out.write(get_html_index(head, body, script))

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        with sys.stderr as cerr:
            print(e, file=cerr)
        pass
