from types import SimpleNamespace
from urllib.parse import parse_qs, urlparse
import funcs

def test_state_urls_are_unique_and_keep_filters():
    urls = funcs.GetLinks()
    assert len(urls) == len(set(urls))
    states = {parse_qs(urlparse(url).query)['s'][0] for url in urls}
    assert {'CA','NY','TX','DC','PR'} <= states
    assert all(parse_qs(urlparse(url).query)['l'] == ['92 93 94'] for url in urls)

def test_pagination_skips_previous_and_expands_relative_links(monkeypatch):
    html = '<div id="ctl00_cphCollegeNavBody_ucResultsMain_divPagingControls" style="text-align:right" class="colorful"><a href="?pg=1">Previous</a><a href="?pg=2">2</a><a href="?pg=3">3</a></div>'
    calls = []
    def get(url):
        calls.append(url)
        return SimpleNamespace(content=html.encode())
    monkeypatch.setattr(funcs.requests, 'get', get)
    assert funcs.GetPageLinks('https://example.test') == ['https://nces.ed.gov/collegenavigator/?pg=2','https://nces.ed.gov/collegenavigator/?pg=3']
    assert calls == ['https://example.test']

def test_empty_pagination_returns_no_links(monkeypatch):
    monkeypatch.setattr(funcs.requests, 'get', lambda url: SimpleNamespace(content=b'<div id="ctl00_cphCollegeNavBody_ucResultsMain_divPagingControls" style="text-align:right" class="colorful"></div>'))
    assert funcs.GetPageLinks('https://example.test') == []
