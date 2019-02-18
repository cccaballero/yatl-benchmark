import timeit

from jinja2 import  Environment, FileSystemLoader, Template
from yatl import render


file_loader = FileSystemLoader('jinja2_templates')
env = Environment(loader=file_loader)

def render_jinja():
    template = env.get_template('page.html')
    output = template.render(name='bar', title='foo')
    # print(output)


def render_jinja_slow():
    # file_loader = FileSystemLoader('jinja2_templates')
    env = Environment(loader=file_loader)
    template = env.get_template('page.html')
    output = template.render(name='bar', title='foo')
    # print(output)


def render_jinja_no_file():
    template = Template('Hello {{ name }}!')
    output = template.render(name='John Doe')
    # print(output)


def render_yatl():
    output = render(path='yatl_templates', filename='yatl_templates/page.html', context=dict(name='bar', title='foo'))
    # print(output)


def render_yatl_no_file():
    output = render('Hello {{=name}}!', context=dict(name='bar', title='foo'))
    # print(output)

if __name__ == '__main__':
    print('\ncode#Testing hello world\n')

    print('Single iteration')
    print('jinja2', timeit.timeit(render_jinja_no_file, number=1))
    print('yatl  ', timeit.timeit(render_yatl_no_file, number=1))

    print('\nmultiple iterations')
    print('jinja2', timeit.timeit(render_jinja_no_file, number=10000))
    print('yatl  ', timeit.timeit(render_yatl_no_file, number=10000))


    print('\n\n#Testing from file\n')

    print('Single iteration')
    print('jinja2', timeit.timeit(render_jinja, number=1))
    print('yatl  ', timeit.timeit(render_yatl, number=1))


    print('\nmultiple iterations')
    print('jinja2', timeit.timeit(render_jinja, number=10000))
    print('yatl  ', timeit.timeit(render_yatl, number=10000))


    print('\n\nNow if we include all steps in jinja\n\n')

    print('Single iteration')
    print('jinja2', timeit.timeit(render_jinja_slow, number=1))
    print('yatl  ', timeit.timeit(render_yatl, number=1))


    print('\nmultiple iterations')
    print('jinja2', timeit.timeit(render_jinja_slow, number=10000))
    print('yatl  ', timeit.timeit(render_yatl, number=10000))