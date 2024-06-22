from pathlib import Path
import re
import markdown
from os import listdir
from os.path import isfile, join


def build_pdf(html_file, outdir):
    pass


def build_html(options, workingdir, outdir):
    # Check embeds
    def replace_embeds(html_in):
        embed_pattern = re.compile(r"\[\[embed\([^)]*\)\]\]", re.IGNORECASE)
        html_out = html_in
        for e in re.findall(embed_pattern, html_out):
            link = e[8:-3]
            html_out = html_out.replace(e, f'<br><iframe src={link}></iframe></br')

        return html_out

    title = options['metadata']['title']
    pages_numbers_options = options['book']['page_numbers']
    book = workingdir + '/book'
    templates_path = str(Path(__file__).parent.resolve()) + '/export_templates'

    page_index = 000
    page_number = 1
    # Pre-content
    with open(book + '/pre-content.md', 'r') as file:
        pages = file.read().split("[[pg]]")
        for page in pages:
            html = markdown.markdown(page, output_format='html')
            html = replace_embeds(html)

            out = open(outdir + f'/html/{page_index}.html', 'w')
            if pages_numbers_options['book/' + 'pre-content.md'] == 'roman':
                roman_numerals = ['i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix', 'x']
                out.write(
                    f"<html><link rel='stylesheet' href='{templates_path}/css/standard.css'><body><div id='page-content' class='page'>{html}</div><div style='position: fixed; bottom: 0; right: 0; margin-right: 20px;'><p>{roman_numerals[page_index]}</p></div></body></html>")
            elif pages_numbers_options['book/' + 'pre-content.md'] == 'numerical':
                out.write(
                    f"<html><body><div id='page-content' class='page'>{html}<div class='page-number'><p>{page_index + 1}</p></div></div></body></html>")
                page_number += 1
            page_index += 1

    # Chapters
    chapter_files = [f for f in listdir(book + '/chapters') if
                     isfile(join(book + '/chapters', f))]
    chapter_files = [i for i in chapter_files if i.endswith('.md')]
    for chapter in chapter_files:
        with open(book + '/chapters/' + chapter) as file:
            pages = file.read().split("[[pg]]")
            for page in pages:
                html = markdown.markdown(page, output_format='html')
                html = replace_embeds(html)

                out = open(outdir + f'/html/{page_index}.html', 'w')
                out.write(
                    f"<html><link rel='stylesheet' href='{templates_path}/css/standard.css'><body><div id='page-content' class='page'>{html}<div class='page-number'><p>{page_number}</p></div></div></body></html>")
                page_index += 1
                page_number += 1

    # Book reader
