
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'DATE DOLAR EQUALS HOUR ID LQUESTION NORMSTRING NUMBER QUOTATION_MARKS RQUESTION TCARNET TCARRERA TCORREO TCREDITOS TDESCRIPCION TDPI TEDAD TELEMENT TELEMENTS TESTADO TFECHA THORA TITEM TMATERIA TNOMBRE TPASSWORD TTYPEstatement : LQUESTION TELEMENTS RQUESTION elementos LQUESTION DOLAR TELEMENTS RQUESTIONelementos : elementos elemento\n                 | elemento\n    elemento : LQUESTION TELEMENT  tipoElemento RQUESTION items LQUESTION DOLAR TELEMENT RQUESTIONtipoElemento : TTYPE EQUALS NORMSTRING\n    items : items item\n    items : item\n    item : LQUESTION TITEM tipeItem EQUALS valueItem DOLAR RQUESTION\n    valueItem : NORMSTRING\n                 | NUMBER\n                 tipeItem : TCARNET\n                | TDPI\n                | TNOMBRE\n                | TCARRERA\n                | TPASSWORD\n                | TCREDITOS\n                | TEDAD\n                | TDESCRIPCION\n                | TMATERIA\n                | TFECHA\n                | THORA\n                | TESTADO\n                | TCORREO\n                '
    
_lr_action_items = {'LQUESTION':([0,4,6,7,10,14,18,19,24,45,47,],[2,5,9,-3,-2,17,23,-7,-6,-4,-8,]),'$end':([1,21,],[0,-1,]),'TELEMENTS':([2,13,],[3,16,]),'RQUESTION':([3,11,16,20,41,46,],[4,14,21,-5,45,47,]),'TELEMENT':([5,9,39,],[8,8,41,]),'TTYPE':([8,],[12,]),'DOLAR':([9,23,42,43,44,],[13,39,46,-9,-10,]),'EQUALS':([12,25,26,27,28,29,30,31,32,33,34,35,36,37,38,],[15,40,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,]),'NORMSTRING':([15,40,],[20,43,]),'TITEM':([17,23,],[22,22,]),'TCARNET':([22,],[26,]),'TDPI':([22,],[27,]),'TNOMBRE':([22,],[28,]),'TCARRERA':([22,],[29,]),'TPASSWORD':([22,],[30,]),'TCREDITOS':([22,],[31,]),'TEDAD':([22,],[32,]),'TDESCRIPCION':([22,],[33,]),'TMATERIA':([22,],[34,]),'TFECHA':([22,],[35,]),'THORA':([22,],[36,]),'TESTADO':([22,],[37,]),'TCORREO':([22,],[38,]),'NUMBER':([40,],[44,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,],[1,]),'elementos':([4,],[6,]),'elemento':([4,6,],[7,10,]),'tipoElemento':([8,],[11,]),'items':([14,],[18,]),'item':([14,18,],[19,24,]),'tipeItem':([22,],[25,]),'valueItem':([40,],[42,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> LQUESTION TELEMENTS RQUESTION elementos LQUESTION DOLAR TELEMENTS RQUESTION','statement',8,'p_statement_group','Syntactic.py',17),
  ('elementos -> elementos elemento','elementos',2,'p_elementos_group','Syntactic.py',21),
  ('elementos -> elemento','elementos',1,'p_elementos_group','Syntactic.py',22),
  ('elemento -> LQUESTION TELEMENT tipoElemento RQUESTION items LQUESTION DOLAR TELEMENT RQUESTION','elemento',9,'p_elemento','Syntactic.py',32),
  ('tipoElemento -> TTYPE EQUALS NORMSTRING','tipoElemento',3,'p_tipoElemento','Syntactic.py',40),
  ('items -> items item','items',2,'p_items','Syntactic.py',45),
  ('items -> item','items',1,'p_items_2','Syntactic.py',50),
  ('item -> LQUESTION TITEM tipeItem EQUALS valueItem DOLAR RQUESTION','item',7,'p_item','Syntactic.py',55),
  ('valueItem -> NORMSTRING','valueItem',1,'p_valueItem','Syntactic.py',88),
  ('valueItem -> NUMBER','valueItem',1,'p_valueItem','Syntactic.py',89),
  ('tipeItem -> TCARNET','tipeItem',1,'p_tipeItem','Syntactic.py',94),
  ('tipeItem -> TDPI','tipeItem',1,'p_tipeItem','Syntactic.py',95),
  ('tipeItem -> TNOMBRE','tipeItem',1,'p_tipeItem','Syntactic.py',96),
  ('tipeItem -> TCARRERA','tipeItem',1,'p_tipeItem','Syntactic.py',97),
  ('tipeItem -> TPASSWORD','tipeItem',1,'p_tipeItem','Syntactic.py',98),
  ('tipeItem -> TCREDITOS','tipeItem',1,'p_tipeItem','Syntactic.py',99),
  ('tipeItem -> TEDAD','tipeItem',1,'p_tipeItem','Syntactic.py',100),
  ('tipeItem -> TDESCRIPCION','tipeItem',1,'p_tipeItem','Syntactic.py',101),
  ('tipeItem -> TMATERIA','tipeItem',1,'p_tipeItem','Syntactic.py',102),
  ('tipeItem -> TFECHA','tipeItem',1,'p_tipeItem','Syntactic.py',103),
  ('tipeItem -> THORA','tipeItem',1,'p_tipeItem','Syntactic.py',104),
  ('tipeItem -> TESTADO','tipeItem',1,'p_tipeItem','Syntactic.py',105),
  ('tipeItem -> TCORREO','tipeItem',1,'p_tipeItem','Syntactic.py',106),
]
