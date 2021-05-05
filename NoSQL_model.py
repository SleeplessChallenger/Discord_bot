from replit import db as replDB


class dbClass:
  def __init__(self, db, respond):
    self.db = db
    self.respond = respond
    self.words = {'ebullient': ['happy'], 'severe': ['strict']}
    self.default_words = {'happy': ['Chin up!', 'Hang in!', '大丈夫'],
                          'grim': ['sad', 'depressed', 'unhappy',
                                   'angry', 'ireful']}

  @classmethod
  def dbInit(cls, name=None, respond=True):
    if name is None:
      return cls(replDB, respond)
    else:
      return cls(name, respond)

  def update_ebullient(self, ebul_phr):
    # at first check if the key in DB
    if 'ebullient' in self.words:
      ebullient = self.words['ebullient']
      ebullient.append(ebul_phr)
      # save that altered list
      # to the DB
      self.words['ebullient'] = ebullient
    else:
      self.words['ebullient'] = [ebul_phr]

  def delete_ebullient(self, idx):
    ebullient = self.words['ebullient']
    if idx < len(ebullient):
      value = ebullient[idx]
      del ebullient[idx]
      self.words['ebullient'] = ebullient
      return value
