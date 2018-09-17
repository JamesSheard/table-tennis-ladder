from quik import FileLoader


class HtmlGenerator:
    def __init__(self, league_name, table):
        self.league_name = league_name
        self.table = table
        self.html = self.build_html()

    def build_html(self):
        loader = FileLoader('html')
        template = loader.load_template('ladder_template.html')
        players = []

        for name in self.table:
            players.append({'name': name,
                            'rank': self.table.index(name) + 1})

        return template.render(locals(), loader=loader).encode('utf-8')

    def write_html(self):
        with open("html_output/" + self.league_name + '.html', 'w') as f:
            f.truncate(0)
            f.writelines(self.html)
