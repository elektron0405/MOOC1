import datetime
from haystack import indexes
from MOOC.models import Department, Course


class CourseIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name')
    university = indexes.CharField(model_attr='university')
    instructor = indexes.CharField(model_attr='instructor')
    startDate = indexes.DateTimeField(model_attr='startDate')

    def get_model(self):
        return Course

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(startDate__lte=datetime.datetime.now())

class DepartmentIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    deptName = indexes.CharField(model_attr='deptName')
    deptCode = indexes.CharField(model_attr='deptCode')
	
    def get_model(self):
	return Department
