import markdown
from os import listdir
from os.path import isfile, join

def get_pdf(html_file, outdir):
    pass


def get_html(options, workingdir, outdir):
    title = options['metadata']['title']
    pages_numbers_options = options['book']['page_numbers']
    book = workingdir + '/book'

    page_index = 0
    # Pre-content
    with open(book + '/pre-content.md', 'r') as file:
        pages = file.read().split(repr("\\pg\\"))
        for page in pages:
            html = markdown.markdown(page, output_format='html')
            out = open(outdir + f'/html/{page_index}')
            out.write(html)
            page_index += 1

    # Chapters
    chapter_files = [f for f in listdir(workingdir + '/book/chapters') if isfile(join(workingdir + '/book/chapters', f))]
    for chapter in chapter_files:
        break
