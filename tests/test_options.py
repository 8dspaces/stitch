from textwrap import dedent
from stitch.stitch import Stitch


class TestOptions:

    def test_defaults(self):
        s = Stitch('')
        assert s.warning
        assert s.on_error == 'continue'
        assert s.to == 'html'
        assert s.standalone

    def test_override(self):
        doc = dedent('''\
        ---
        title: My Title
        standalone: False
        warning: False
        on_error: raise
        abstract: |
          This is the abstract.

          It consists of two paragraphs.
        ---

        # Hail and well met
        ''')
        s = Stitch('')
        s.stitch(doc)

        assert s.standalone is False
        assert s.warning is False
        assert s.on_error == 'raise'
        assert getattr(s, 'abstract', None) is None

