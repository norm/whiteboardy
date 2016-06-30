from datetime import datetime

from flourish.generators import (
    IndexAtomGenerator,
    IndexGenerator,
    PageGenerator,
)


class Homepage(IndexGenerator):
    template_name = 'homepage.html'


class PublishedPagesAtomGenerator(IndexAtomGenerator):
    def get_objects(self, filter):
        _now = datetime.now()
        _filtered = self.flourish.sources.filter(published__lt=_now)
        _filtered = _filtered.filter(**filter)

        if self.order_by:
            _filtered = _filtered.order_by(self.order_by)

        return _filtered


URLS = (
    (
        '/',
        'homepage',
        Homepage.as_generator()
    ),
    (
        '/#slug',
        'page-detail',
        PageGenerator.as_generator()
    ),
    (
        '/index.atom',
        'atom-feed',
        PublishedPagesAtomGenerator.as_generator(),
    ),
    (
        '/#category/',
        'category-index',
        IndexGenerator.as_generator()
    ),
)
