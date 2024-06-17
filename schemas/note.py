def noteEntity(item):
    return {
        'id': str(item['_id']),
        'title': item['title'],
        'content': item['content'],
        'desc': item['desc'],
        'important': item['important']
    }
def notesEntity(items)->list:
    return [noteEntity(item) for item in items]