head="""
    <style>
        table{
            margin:0;
            padding:0;
            overflow:hidden;
        }
        td {
            border: 1px solid rgb(194, 22, 22);
            padding: 10px;

        }
        
        
        table tr {
            transition: all 1s ease-in-out;
        }

        table tr.slide-out {
            transform: translateX(105%);
        }
    </style>"""
body="""<h1>CV</h1>
    <table>
        <thead>
            <tr>
                <th colspan="2">Crazy resume</th>
            </tr>
        </thead>
        <tr>
            <td>
                <ul>
                    <li>C</li>
                    <li>C++</li>
                    <li>Java</li>
                    <li>C#</li>
                </ul>
            </td>
            <td>
                <ol>
                    <li>Javascript</li>
                    <li>Python</li>
                </ol>
            </td>
        </tr>
        <tr>
            <td>Могу копать</td>
            <td style="border:2px solid #424242;">Могу не копать</td>
        </tr>
    </table>"""
scripts="""<script>
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
    </script>"""