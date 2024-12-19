from model_utils.models import TimeStampedModel

class BaseModel(TimeStampedModel):
    ORDERING = ("-created",)

    class Meta:
        abstract = True

    @property
    def added_on(self):
        return self.created

    @property
    def updated_on(self):
        return self.modified
