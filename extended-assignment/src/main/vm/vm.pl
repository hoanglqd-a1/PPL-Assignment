%main program


reduce_prog([Var,Func,Stmt]) :-
		create_env(Var,env([[]],false),Env1),
		create_env(Func,Env1,Env2),
		Env2 = env(E2,_),
		reduce_stmt(config(Stmt,env([[]|E2],_)),_).
											
%check if X has been declared in the first list of the environment
has_declared(X,[id(X,_,_,_)|_],_) :- !.
has_declared(X,[_|L],R) :- has_declared(X,L,R).

%check if X has been defined in the nested list of the environment
has_defined(X,env([[id(X,_,_,_)|_]|_],_)):- !.
has_defined(X,env([[_|Tail]|LTail],Env)):- has_defined(X,env([Tail|LTail],Env)).
has_defined(X,env([[]|LTail],Env)):- has_defined(X,env(LTail,Env)).

%create a symbol table from the list of variable or constant declarations
create_env([],Env,Env).

create_env([var(X,Y)|_],env([_],_),_):- is_builtin(X,_),!,throw(redeclare_identifier(var(X,Y))).
create_env([var(X,Y)|_],env([L1|_],_),_):- has_declared(X,L1,_),!,throw(redeclare_identifier(var(X,Y))).
create_env([var(X,Y)|L],env([L1|L2],T),L3):- create_env(L,env([[id(X,var,Y,nil)|L1]|L2],T),L3).

create_env([const(X,Y)|_],env([_],_),_):- is_builtin(X,_),!,throw(redeclare_identifier(const(X,Y))).
create_env([const(X,Y)|_],env([L1|_],_),_):- has_declared(X,L1,_),!,throw(redeclare_identifier(const(X,Y))).
create_env([const(X,Y)|L],env([L1|L2],T),L3):- reduce_all(config(Y,env([L1|L2],T)),config(V,env([L1|L2],T))),type(V,Type),create_env(L,env([[id(X,const,Type,V)|L1]|L2],T),L3).

create_env([func(I,P,R,B)|_],env([_],_),_):- is_builtin(I,_),!,throw(redeclare_function(func(I,P,R,B))).
create_env([func(I,P,R,B)|_],env([L1|_],_),_):- has_declared(I,L1,_),!,throw(redeclare_function(func(I,P,R,B))).
create_env([func(I,P,R,B)|L],env([L1|L2],T),L3):- create_env(L,env([[id(I,func,[P,R,B],nil)|L1]|L2],T),L3),create_env(P,env([[]],false),_).

create_env([proc(I,P,B)|_],env([_],_),_):- is_builtin(I,_),!,throw(redeclare_procedure(proc(I,P,B))).
create_env([proc(I,P,B)|_],env([L1|_],_),_):- has_declared(I,L1,_),!,throw(redeclare_procedure(proc(I,P,B))).
create_env([proc(I,P,B)|L],env([L1|L2],T),L3):- create_env(L,env([[id(I,proc,P,B)|L1]|L2],T),L3),create_env(P,env([[]],false),_).

create_env([par(X,Y)|_],env([L1|_],_),_):- has_declared(X,L1,_),!,throw(redeclare_identifier(par(X,Y))).
create_env([par(X,Y)|L],env([L1|L2],T),L3):- create_env(L,env([[id(X,par,Y,nil)|L1]|L2],T),L3).
create_env([],E,[],E):- !.
create_env([par(X,Y)|L],env([L1|L2],T),[V|VTail],L3):- create_env(L,env([[id(X,par,Y,V)|L1]|L2],T),VTail,L3).

% reduce_stmt/2
reduce_stmt(config([],Env),Env) :- !.

reduce_stmt(config([var(Name,Type)|_],Env),_) :- 
		Env = env([L1|_],_),has_declared(Name,L1,_),
		!,throw(redeclare_identifier(var(Name,Type))).
reduce_stmt(config([var(Name,Type)|STail],Env),F) :-
		Env = env([ETail|LETail],_),
		reduce_stmt(config(STail,env([[id(Name,var,Type,nil)|ETail]|LETail],_)),F).

reduce_stmt(config([const(Name,Expr)|_],Env),_) :- 
		Env = env([L1|_],_),has_declared(Name,L1,_),
		!,throw(redeclare_identifier(const(Name,Expr))).
reduce_stmt(config([const(Name,Expr)|STail],Env),L) :-
		Env = env([L1|L2],T),
		reduce_all(config(Expr,Env),config(Value,Env)),
		type(Value,Type),
		reduce_stmt(config(STail,env([[id(Name,const,Type,Value)|L1]|L2],T)),L).

reduce_stmt(config([call(Name,[Expr])|Tail],Env1),T) :- is_builtin(Name,_),!,
		reduce_all(config(Expr,Env1),config(Value,Env2)),
		p_call_builtin(Name,[Value]),
		reduce_stmt(config(Tail,Env2),T).
reduce_stmt(config([call(Name,Exprs)|STail],Env),T) :-
		Env = env(E,_),
		last(E,EL),
		(getprocedure(Name,EL,Proc) -> true; throw(undeclare_procedure(call(Name,Exprs)))),
		Proc = id(Name,proc,Params,Body),
		(length(Params,L),length(Exprs,L) -> true; throw(wrong_number_of_argument(call(Name,Exprs)))),
		calculateArgs(Exprs,Env,Values,Env1),
		Env1 = env(E1,_),
		create_env(Params,env([[]|E1],_),Values,Env2),
		reduce_stmt(config(Body,Env2),Env3),
		Env3 = env([_|ETail3],_),
		reduce_stmt(config(STail,env(ETail3,_)),T).

reduce_stmt(config([assign(Name,Expr)|STail],Env),T) :-
		has_defined(Name,Env),!,
		reduce_all(config(Expr,Env),config(Value,Env1)),
		find_and_assign(assign(Name,Value),Env1,Env2),
		reduce_stmt(config(STail,Env2),T).
reduce_stmt(config([assign(Name,Expr)|_],_),_) :- throw(undeclare_identifier(assign(Name,Expr))).

reduce(config(sub(E),Env),config(R,Env)) :- 
		reduce_all(config(E,Env),config(V,Env)),
		R is -V.
reduce(config(add(E1,E2),Env),config(R,Env)) :-
		reduce_all(config(E1,Env),config(V1,Env)),
		reduce_all(config(E2,Env),config(V2,Env)),
		R is V1+V2.
reduce(config(sub(E1,E2),Env),config(R,Env)) :-
		reduce_all(config(E1,Env),config(V1,Env)),
		reduce_all(config(E2,Env),config(V2,Env)),
		R is V1-V2.
reduce(config(times(E1,E2),Env),config(R,Env)) :-
		reduce_all(config(E1,Env),config(V1,Env)),
		reduce_all(config(E2,Env),config(V2,Env)),
		R is V1*V2.
reduce(config(rdiv(E1,E2),Env),config(R,Env)) :-
		reduce_all(config(E1,Env),config(V1,Env)),
		reduce_all(config(E2,Env),config(V2,Env)),
		R is V1/V2.
reduce(config(call(Name,Exprs),Env),config(R,Env4)):-
		Env = env(E,_),
		last(E,EL),
		(getfunction(Name,EL,Func) -> true; throw(undeclare_function(call(Name,Exprs)))),
		Func = id(Name,func,[Params,Ret,Body],_),
		(length(Params,L),length(Exprs,L) -> true; throw(wrong_number_of_argument(call(Name,Exprs)))),
		calculateArgs(Exprs,Env,Values,Env1),
		Env1 = env(E1,_),
		create_env(Params,env([[]|E1],_),Values,Env2),
		reduce_stmt(config(Body,Env2),Env3),
		Env3 = env(E3,_),
		last(E3,Global),
		(getfunction(Name,Global,Func1); throw(undeclare_function(call(Name,Exprs)))),
		Func1 = id(Name,func,[_,Ret,_],Value),
		(type(Value,Ret) -> true; throw(type_mismatch(call(Name,Exprs)))),
		R = Value,
		E3 = [_|ETail3],
		Env4 = env(ETail3,_) .
reduce(config(I,Env),config(R,Env)):-
		getvalue(I,Env,R).

reduce_all(config(V,Env),config(V,Env)):- (integer(V);float(V);string(V);boolean(V)),!.
reduce_all(config(E,Env),config(E2,Env2)):-
		reduce(config(E,Env),config(E1,Env1)),!,
		reduce_all(config(E1,Env1),config(E2,Env2)).





boolean(true).
boolean(false).
type(X,integer):- integer(X),!.
type(X,real):- float(X),!.
type(X,string):- string(X),!.
type(X,bool):- boolean(X),!.

matchType(func,[_,Ret,_],Value) :- type(Value,Ret),!.
matchType(Kind,Type,Value) :- Kind \= const, type(Value,Type),!.
find_and_assign(assign(Name, Value), Env1, Env2) :-
		Env1 = env([[id(Name, Kind, Type, _    )| Tail]| LTail], _),
		Env2 = env([[id(Name, Kind, Type, Value)| Tail]| LTail], _),
		(
			Kind \= const; throw(cannot_assign(assign(Name, Value)))
		),(
			matchType(Kind, Type, Value),!;
			throw(type_mismatch(assign(Name, Value)))
		).
find_and_assign(assign(Name,Value),Env1,Env2) :-
		Env1 = env([[Id|Tail1]|LTail1],_),
		Env2 = env([[Id|Tail2]|LTail2],_),
		!,find_and_assign(assign(Name,Value),env([Tail1|LTail1],_),env([Tail2|LTail2],_)).
find_and_assign(assign(Name,Value),Env1,Env2) :-
		Env1 = env([[]|LTail1],_),
		Env2 = env([[]|LTail2],_),
		!,find_and_assign(assign(Name,Value),env(LTail1,_),env(LTail2,_)).

getprocedure(Name, [id(Name, proc, P, B)|_], id(Name, proc, P, B)) :- !.
getprocedure(Name, [_|T], Proc) :-
		getprocedure(Name, T, Proc).

getfunction(Name, [id(Name, func, PRB, V)|_], id(Name, func, PRB, V)) :- !.
getfunction(Name, [_|T], Func) :-
		getfunction(Name, T, Func),!.

getvalue(I, Env, R) :-
		Env = env([[id(I, _, _, R)|_]|_], _),
		!,
		(R \= nil -> true; throw(undeclare_identifier(I))).
getvalue(I, env([[_|T]|TT], _), R) :-
		!,
		getvalue(I, env([T|TT], _), R).
getvalue(I, env([[]|TT], _), R) :-
		!,
		getvalue(I, env(TT, _), R).
getvalue(I, env([[]], _), _) :-
    	throw(undeclare_identifier(I)).

calculateArgs([], Env, [], Env) :- !.
calculateArgs([Expr|ETail], Env, [Value|VTail], Env2) :-
    reduce_all(config(Expr, Env), config(Value, Env1)),
    calculateArgs(ETail, Env1, VTail, Env2).