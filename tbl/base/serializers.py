from rest_framework import serializers


class BaseSerializer(serializers.ModelSerializer):

    id = serializers.CharField(source="uuid", read_only=True)

    def __init__(self, *args, **kwargs):
        """
        Controls dynamic inclusion/exclusion of fields and sets read-only fields.
        Usage:
            - fields: Specify fields to include.
            - exclude: Specify fields to exclude.
            - read_only_fields: Specify fields as read-only.
        """
        fields = kwargs.pop("fields", None)
        exclude = kwargs.pop("exclude", None)
        read_only_fields = kwargs.pop("read_only_fields", None)

        super().__init__(*args, **kwargs)

        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

        if exclude is not None:
            for field_name in exclude:
                self.fields.pop(field_name, None)

        if read_only_fields is not None:
            for field_name in read_only_fields:
                try:
                    self.fields[field_name].read_only = True
                except KeyError:
                    pass

    class Meta:
        abstract = True
