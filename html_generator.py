from quik import FileLoader, Template

loader = FileLoader('html')
template = loader.load_template('ladder_template.html')

players = [{'name': 'Matt', 'rank': 1},
            {'name': 'Rob', 'rank': 2},
            {'name': 'Mike', 'rank': 3},
            {'name': 'James', 'rank': 4}]

group = "Hermes"
# html = template.render(players,
#                       loader=loader).encode('utf-8')
html = template.render(locals(), loader=loader).encode('utf-8')

with open(group + '.html', 'w') as f:
    f.writelines(html)