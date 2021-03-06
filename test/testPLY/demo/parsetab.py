
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND CLOSE_B COLUMN_FUNCTION_NAME COMMA DIVIDE EQUALITY FROM_T GREATER_THAN LESS_THAN MINUS NOT NUMBER OPEN_B OR PLUS SELECT_T SEMICOLON TIMES WHERE_TSQLselect : SELECT_T COLUMN_FUNCTION_NAME FROM_T COLUMN_FUNCTION_NAME SEMICOLON\n                 | SELECT_T TIMES  FROM_T COLUMN_FUNCTION_NAME SEMICOLON\n                 | SELECT_T function FROM_T COLUMN_FUNCTION_NAME SEMICOLON\n                 | SELECT_T COLUMN_FUNCTION_NAME FROM_T COLUMN_FUNCTION_NAME WHERE_T condition SEMICOLON\n                 | SELECT_T TIMES  FROM_T COLUMN_FUNCTION_NAME WHERE_T condition SEMICOLON\n                 | SELECT_T function FROM_T COLUMN_FUNCTION_NAME WHERE_T condition SEMICOLON\n                 | SELECT_T columnlist FROM_T COLUMN_FUNCTION_NAME SEMICOLON\n                 | SELECT_T columnlist FROM_T COLUMN_FUNCTION_NAME WHERE_T condition SEMICOLON\n    condition : COLUMN_FUNCTION_NAME EQUALITY       expression\n                 | COLUMN_FUNCTION_NAME LESS_THAN      expression\n                 | COLUMN_FUNCTION_NAME GREATER_THAN   expression\n    expression : expression PLUS         expression\n                  | expression MINUS        expression\n                  | expression TIMES        expression\n                  | expression DIVIDE       expression\n                  | expression AND          expression\n                  | expression OR           expression\n                  | NOT                     expression\n                  | NUMBERfunction : COLUMN_FUNCTION_NAME OPEN_B COLUMN_FUNCTION_NAME CLOSE_B \n    columnlist : COLUMN_FUNCTION_NAME\n               | COLUMN_FUNCTION_NAME COMMA columnlist\n    '
    
_lr_action_items = {'AND':([42,43,44,45,46,53,54,55,56,57,58,],[-19,47,47,47,47,47,47,47,47,47,47,]),'NOT':([35,36,37,41,47,48,49,50,51,52,],[41,41,41,41,41,41,41,41,41,41,]),'CLOSE_B':([17,],[24,]),'TIMES':([2,42,43,44,45,46,53,54,55,56,57,58,],[3,-19,51,51,51,51,51,51,51,51,51,51,]),'$end':([1,20,23,25,27,34,38,39,40,],[0,-2,-3,-1,-7,-5,-6,-4,-8,]),'OPEN_B':([5,],[10,]),'WHERE_T':([13,14,18,19,],[21,22,26,28,]),'DIVIDE':([42,43,44,45,46,53,54,55,56,57,58,],[-19,50,50,50,50,50,50,50,50,50,50,]),'FROM_T':([3,4,5,6,15,16,24,],[7,8,11,12,-21,-22,-20,]),'GREATER_THAN':([30,],[36,]),'SELECT_T':([0,],[2,]),'COMMA':([5,15,],[9,9,]),'OR':([42,43,44,45,46,53,54,55,56,57,58,],[-19,48,48,48,48,48,48,48,48,48,48,]),'COLUMN_FUNCTION_NAME':([2,7,8,9,10,11,12,21,22,26,28,],[5,13,14,15,17,18,19,30,30,30,30,]),'SEMICOLON':([13,14,18,19,29,31,32,33,42,43,44,45,46,53,54,55,56,57,58,],[20,23,25,27,34,38,39,40,-19,-9,-11,-10,-18,-16,-17,-13,-15,-14,-12,]),'EQUALITY':([30,],[35,]),'MINUS':([42,43,44,45,46,53,54,55,56,57,58,],[-19,49,49,49,49,49,49,49,49,49,49,]),'LESS_THAN':([30,],[37,]),'PLUS':([42,43,44,45,46,53,54,55,56,57,58,],[-19,52,52,52,52,52,52,52,52,52,52,]),'NUMBER':([35,36,37,41,47,48,49,50,51,52,],[42,42,42,42,42,42,42,42,42,42,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'condition':([21,22,26,28,],[29,31,32,33,]),'function':([2,],[4,]),'SQLselect':([0,],[1,]),'expression':([35,36,37,41,47,48,49,50,51,52,],[43,44,45,46,53,54,55,56,57,58,]),'columnlist':([2,9,],[6,16,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> SQLselect","S'",1,None,None,None),
  ('SQLselect -> SELECT_T COLUMN_FUNCTION_NAME FROM_T COLUMN_FUNCTION_NAME SEMICOLON','SQLselect',5,'p_SQLselect','parsesql.py',87),
  ('SQLselect -> SELECT_T TIMES FROM_T COLUMN_FUNCTION_NAME SEMICOLON','SQLselect',5,'p_SQLselect','parsesql.py',88),
  ('SQLselect -> SELECT_T function FROM_T COLUMN_FUNCTION_NAME SEMICOLON','SQLselect',5,'p_SQLselect','parsesql.py',89),
  ('SQLselect -> SELECT_T COLUMN_FUNCTION_NAME FROM_T COLUMN_FUNCTION_NAME WHERE_T condition SEMICOLON','SQLselect',7,'p_SQLselect','parsesql.py',90),
  ('SQLselect -> SELECT_T TIMES FROM_T COLUMN_FUNCTION_NAME WHERE_T condition SEMICOLON','SQLselect',7,'p_SQLselect','parsesql.py',91),
  ('SQLselect -> SELECT_T function FROM_T COLUMN_FUNCTION_NAME WHERE_T condition SEMICOLON','SQLselect',7,'p_SQLselect','parsesql.py',92),
  ('SQLselect -> SELECT_T columnlist FROM_T COLUMN_FUNCTION_NAME SEMICOLON','SQLselect',5,'p_SQLselect','parsesql.py',93),
  ('SQLselect -> SELECT_T columnlist FROM_T COLUMN_FUNCTION_NAME WHERE_T condition SEMICOLON','SQLselect',7,'p_SQLselect','parsesql.py',94),
  ('condition -> COLUMN_FUNCTION_NAME EQUALITY expression','condition',3,'p_condition','parsesql.py',99),
  ('condition -> COLUMN_FUNCTION_NAME LESS_THAN expression','condition',3,'p_condition','parsesql.py',100),
  ('condition -> COLUMN_FUNCTION_NAME GREATER_THAN expression','condition',3,'p_condition','parsesql.py',101),
  ('expression -> expression PLUS expression','expression',3,'p_expression','parsesql.py',106),
  ('expression -> expression MINUS expression','expression',3,'p_expression','parsesql.py',107),
  ('expression -> expression TIMES expression','expression',3,'p_expression','parsesql.py',108),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression','parsesql.py',109),
  ('expression -> expression AND expression','expression',3,'p_expression','parsesql.py',110),
  ('expression -> expression OR expression','expression',3,'p_expression','parsesql.py',111),
  ('expression -> NOT expression','expression',2,'p_expression','parsesql.py',112),
  ('expression -> NUMBER','expression',1,'p_expression','parsesql.py',113),
  ('function -> COLUMN_FUNCTION_NAME OPEN_B COLUMN_FUNCTION_NAME CLOSE_B','function',4,'p_function','parsesql.py',117),
  ('columnlist -> COLUMN_FUNCTION_NAME','columnlist',1,'p_columnlist','parsesql.py',122),
  ('columnlist -> COLUMN_FUNCTION_NAME COMMA columnlist','columnlist',3,'p_columnlist','parsesql.py',123),
]
