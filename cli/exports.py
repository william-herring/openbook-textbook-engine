import markdown
from os import listdir
from os.path import isfile, join


def build_pdf(html_file, outdir):
    pass


def build_html(options, workingdir, outdir):
    title = options['metadata']['title']
    pages_numbers_options = options['book']['page_numbers']
    book = workingdir + '/book'

    page_index = 0
    # Pre-content
    with open(book + '/pre-content.md', 'r') as file:
        pages = file.read().split("\\\\pg\\\\")
        for page in pages:
            html = markdown.markdown(page, output_format='html')
            out = open(outdir + f'/html/{page_index}.html', 'w')
            if pages_numbers_options['book/' + 'pre-content.md'] == 'roman':
                roman_numerals = ['i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix', 'x']
                out.write(f"<html><body><div id='page-content' class='page'>{html}</div><div style='position: fixed; bottom: 0; right: 0; margin-right: 20px;'><p>{roman_numerals[page_index]}</p></div></body></html>")
            elif pages_numbers_options['book/' + 'pre-content.md'] == 'numerical':
                out.write(f"<html><body><div id='page-content' class='page'>{html}</div><div style='position: fixed; bottom: 0; right: 0; margin-right: 20px;'><p>{page_index + 1}</p></div></body></html>")
            page_index += 1

    # Chapters
    page_number = 1
    chapter_files = [f for f in listdir(book + '/chapters') if
                     isfile(join(book + '/chapters', f))]
    chapter_files = [i for i in chapter_files if i.endswith('.md')]
    for chapter in chapter_files:
        with open(book + '/chapters/' + chapter) as file:
            pages = file.read().split("\\\\pg\\\\")
            for page in pages:
                html = markdown.markdown(page, output_format='html')
                out = open(outdir + f'/html/{page_index}.html', 'w')
                out.write(f"<html><body><div id='page-content' class='page'>{html}<div style='position: fixed; bottom: 0; right: 0; margin-right: 20px;'><p>{page_number}</p></div></div></body></html>")
                page_index += 1
                page_number += 1
