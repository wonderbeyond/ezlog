try:
    from taggit.models import Tag, TaggedItem
    def tags_for(target=None):
        '''get tags(tagged by taggit) for specific app and model'''
        if not target:
            tags = Tag.objects.all()
        else:
            app, model = [v.lower() for v in target.split('.', 1)]
            tis = TaggedItem.objects.all()
            
            if app:
                tis = tis.filter(content_type__app_label=app)
            if model:
                tis = tis.filter(content_type__model=model)

            tag_ids = tis.values_list('tag_id', flat=True)
            tags = Tag.objects.filter(id__in=tag_ids)
        return tags

    def tags_for_model(model):
        '''get tags(tagged by taggit) for specific model'''
        return tags_for('.%s' % model)

    def tags_for_app(app):
        '''get tags(tagged by taggit) for specific app'''
        return tags_for('%s.' % app)

except ImportError:
    pass
