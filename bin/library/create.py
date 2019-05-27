"""
This css.py file create a file .css for index.html

@author Vicentini Elia, Olivieri Matteo, Gandini Simone
@version 1.0
"""

something = ['/* File .css */\n', '/* @author Vicentini Elia, Olivieri Matteo, Gandini Simone */\n', '\n'
             'h1, p, td { \n', '       font-family: arial; \n', '}\n', '\n', 'th { \n', '       font-family: arial; \n',
             '       font-style: bold; \n', '}\n']


def css():
    """ This function create .css file """

    file = open('files\css.css', 'w')
    file.writelines(something)
    file.close()

    return 0


def html(match_list, disciplines_list, disciplines):
    """ This function create .html file """

    strings1 = ['<!DOCTYPE html> \n', '<html> \n', '<head> \n', '<title>Tabella Matchmaking</title> \n',
                '<link rel="stylesheet" type="text/css" href="files\css.css"> \n', '</head> \n']

    strings2 = ['<body> \n', '<h1>Matchmaking Table</h1> \n', '<p>Matchmaking system created by <i>Gandini Simone</i>,'
                '<i>Vicentini Elia</i>, <i>Olivieri Matteo</i> for <b>', 'Fornace Studio</b>.</p> \n']

    strings3 = ['<table border = 1> \n <tr>\n <td> </td>']

    file = open('Matchmaking table.html', 'w')

    file.writelines(strings1)
    file.writelines(strings2)
    file.writelines(strings3)

    for i in range(disciplines):
        file.write('<th>' + disciplines_list[i] + '</th>')
    file.write('</tr>')

    for h in range(len(match_list)):
        file.write('<td>' + ' Turno ' + str(h + 1) + '</td>')
        for j in range(len(match_list[h])):
            file.write('<td> Squadra ' + str(match_list[h][j][0]) + '\n vs \n Squadra ' + str(match_list[h][j][1]) +
                       '</td>\n')
        file.write('</tr>')

    file.write('</table>')

    file.close()

    return 0


if __name__ == '__main__':
    create_css()
