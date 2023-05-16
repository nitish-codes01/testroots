contents = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title></title>
</head>
<body>
    <table border="1" colspan="10">
        <thead>
            <tr>
                <th>Id</th>
                <th>Name</th>
                <th>Phone</th>
            </tr>
        </thead>
        <tbody>
            {% for n in abc %}
            <tr>
                <td>{{forloop.counter}}</td>
                <td>{{n.name}}</td>
                <td>{{n.phone}}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
</body>
</html>'''