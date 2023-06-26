def flatten(schema,prefix=  None):
  '''
  Return a list of fields of a given schema, including nested fields in a strucType 
  '''
    fields = []
    for field in schema.fields:
        name = prefix + '.' + field.name if prefix else field.name
        dtype = field.dataType
        if isinstance(dtype, StructType):
            fields += flatten(dtype, prefix=name)
        else:
            fields.append(name)
 
    return fields
