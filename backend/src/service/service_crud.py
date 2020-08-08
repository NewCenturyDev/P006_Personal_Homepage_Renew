class CrudService():
  dao = None
  def getList(self):
    try:
      return self.dao.select()
    except Exception as error:
      raise error
  def create(self, entity):
    try:
      return self.dao.insert(entity)
    except Exception as error:
      raise error
  def modify(self, entity):
    try:
      return self.dao.update(entity)
    except Exception as error:
      raise error
  def delete(self, entityID):
    try:
      return self.dao.delete(entityID)
    except Exception as error:
      raise error
