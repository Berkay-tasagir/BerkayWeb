HTML_FILES = [
    'about.html',
    'internships.html',
    'links.html',
    'devlog.html',
]


def read_html(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()


def test_header_tags_match():
    for html in HTML_FILES:
        content = read_html(html)
        opens = content.count('<header>')
        closes = content.count('</header>')
        assert opens == closes, f'{html}: header tag mismatch'


def test_no_blendert_alt_text():
    for html in HTML_FILES:
        content = read_html(html)
        assert 'alt="blendert"' not in content, f'{html}: alt text should not be "blendert"'
