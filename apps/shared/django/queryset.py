from django.db.models import Manager, QuerySet


class BaseQuerySet(QuerySet):
    def delete(self):
        self.update(is_delete=True)


class DeleteManager(Manager):
    def get_queryset(self) -> QuerySet:
        return BaseQuerySet(self.model).filter(is_delete=False)
