# -*- coding: utf-8 -*-

def generate_html(enhavo):

    env = jinja2.Environment()
    env.filters['markdown'] = lambda text: jinja2.Markup(md(text))
    env.trim_blocks = True
    env.lstrip_blocks = True
    env.loader=jinja2.FileSystemLoader('html/templates/')

    rendered = env.get_template('index.html').render(enhavo=enhavo)
    with open('html/output/index.html', 'w') as f:
        f.write(rendered.encode('utf-8'))
