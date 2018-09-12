# import sys
# from user_interface import Interface
# from ladder import Ladder
#
# def generate_html_table():
#     ladder = Ladder()
#     html_table = "<table><tr><th>Name</th><th>Rank</th></tr>"
#
#
#     for x in ladder.table:
#         html_table+="<tr><td>"+
#




import os
import glob
from jinja2 import Environment, FileSystemLoader
from ladder import Ladder


class HTML_Generator:

    # Create the jinja2 environment.
    def __init__(self):
        current_directory = os.path.dirname(os.path.abspath(__file__))
        env = Environment(loader=FileSystemLoader(current_directory))

    templates = glob.glob('*.j2')
    ladder = Ladder("ladder_state")

    def render_template(self, filename):
        html = ""
        for p in ladder.table:
            html+="\t<tr>\n"
            html+="\t\t<td>" + p.name + "</td>\n"
            html+="\t\t<td>" + str(ladder.table.index(p) + 1) + "</td>\n"
            html+= "\t</tr>\n"

        print html

        return self.env.get_template(filename).render(
            generated_table=html,
        )

    for f in templates:
        rendered_string = render_template(f)
        f = open(ladder.ladder_name + ".html", "w+")
        f.truncate(0)
        f.write(rendered_string)
        print "HTML File has been generated"

if __name__ == "__main__":
    HTML_Generator()