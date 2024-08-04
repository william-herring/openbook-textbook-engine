import json
from pathlib import Path
import re
import markdown
from os import listdir, remove
from os.path import isfile, join
import shutil
import glob


def build_pdf(html_file, outdir):
    pass


def build_html(options, workingdir, outdir):
    # Check embeds
    def replace_embeds(html_in: str):
        embed_pattern = re.compile(r"\[\[embed\([^)]*\)\]\]", re.IGNORECASE)
        html_out = html_in
        for e in re.findall(embed_pattern, html_out):
            link = e[8:-3]
            html_out = html_out.replace(e, f'<br><iframe src={link}></iframe></br')

        return html_out

    def find_questions(md_in: str):
        question_symbol = "[[question]]"
        answer_pattern = re.compile(r"\[\[answers\(.*\)\]\]", re.IGNORECASE)
        questions_map = {}
        rest = md_in

        while rest.find(question_symbol) != -1:
            start_question = rest.find(question_symbol) + 12
            answer_match = re.search(answer_pattern, rest)
            end_question = answer_match.start()

            questions_map[rest[start_question:end_question]] = ['answer']

            rest = rest[answer_match.end() + 1:]

    title = options['metadata']['title']
    pages_numbers_options = options['book']['page_numbers']
    book = workingdir + '/book'
    templates_path = str(Path(__file__).parent.resolve()) + '/export_templates'
    pages_html = []
    questions = {}

    # Delete existing build
    files = glob.glob(outdir + '/html/*')
    for f in files:
        remove(f)

    chapters = []
    page_index = 0
    page_number = 1
    # Pre-content
    with open(book + '/pre-content.md', 'r') as file:
        pages = file.read().split("[[pg]]")
        for page in pages:
            html = markdown.markdown(page, output_format='html')
            html = replace_embeds(html)

            for header in re.findall(r'(?<=(^#)\s).*', page):
                chapters.append((header, page_index))

            out = open(outdir + f'/html/{page_index}.html', 'w')
            if pages_numbers_options['book/' + 'pre-content.md'] == 'roman':
                roman_numerals = ['i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix', 'x']
                p = f"<html><link rel='stylesheet' href='{templates_path}/css/standard.css'><body><div id='page-content' class='page'>{html}</div><div class='page-number'><p>{roman_numerals[page_index]}</p></div></body></html>"
                pages_html.append(p)
                out.write(p)
            elif pages_numbers_options['book/' + 'pre-content.md'] == 'numerical':
                p = f"<html><body><div id='page-content' class='page'>{html}<div class='page-number'><p>{page_index + 1}</p></div></div></body></html>"
                pages_html.append(p)
                out.write(p)
                page_number += 1
            page_index += 1
    file.close()

    # Chapters
    chapter_files = [f for f in listdir(book + '/chapters') if
                     isfile(join(book + '/chapters', f))]
    chapter_files = [i for i in chapter_files if i.endswith('.md')]
    for chapter in chapter_files:
        with open(book + '/chapters/' + chapter) as file:
            pages = file.read().split("[[pg]]")
            for page in pages:
                find_questions(page)
                html = markdown.markdown(page, output_format='html')
                html = replace_embeds(html)

                for header in re.findall(r'(?<=(^#)\s).*', page):
                    chapters.append((header, page_index))

                out = open(outdir + f'/html/{page_index}.html', 'w')
                p = f"<html><link rel='stylesheet' href='{templates_path}/css/standard.css'><body><div id='page-content' class='page'>{html}<div class='page-number'><p>{page_number}</p></div></div></body></html>"
                pages_html.append(p)
                out.write(p)
                page_index += 1
                page_number += 1
            file.close()

    # Book reader
    shutil.copyfile(templates_path + '/html/index.html', outdir + '/html/index.html')
    with open(outdir + '/html/index.html', 'r+') as file:
        content = file.read()
        file.seek(0)
        content = content.replace('[title]', title)
        content = content.replace('[styles_path]', f'{templates_path}/css/standard.css')
        content = content.replace('[current_page]', pages_html[0])
        content = content.replace('[pages]', str(pages_html))
        file.write(content)
        file.truncate()
        file.close()

    with open(outdir + '/data.json', 'w') as file:
        data = {
            'pages': page_number,
            'chapters': chapters,
            'questions': None
        }
        file.write(json.dumps(data))
        file.close()
