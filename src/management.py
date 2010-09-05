"""
Given a model and a list, create those objects if they aren`t in datastore already.
"""
def initialize(model, list):
    for item in list:
        args = dict(**item)
        for key in item:
            try: args[key] = item[key]() 
            except: args[key] = item[key]
        try:
            model.objects.get(**args)
        except:
            model(**args).save()